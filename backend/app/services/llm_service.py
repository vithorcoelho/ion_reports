"""LLM service for generating structured content from medical data."""

from typing import TypeVar

import mlflow
from mlflow.tracing.fluent import start_span
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletionMessageParam
from pydantic import BaseModel, ValidationError

from app.core.config import settings
from app.core.logging import logger
from app.domain.kg_result import KGResult
from app.domain.report import (
    ClosingNoteContent,
    DeficiencyRecommendationSectionWrapper,
    ExamsRecommendationSectionWrapper,
    FoodRecommendationSectionWrapper,
    GeneralGuidelinesContent,
    LifestyleRecommendationSectionWrapper,
    SummaryContent,
    SupplementRecommendationSectionWrapper,
)
from app.plugins.prompts.prompt_utils import safe_encode, safe_join
from app.schemas.exam import TNMExamData
from app.schemas.patient_anamnesis import PatientAnamnesis

T = TypeVar("T", bound=BaseModel)


def get_mock_response(user_prompt: str, schema: type) -> BaseModel:  # pragma: no cover
    """Generate basic mock responses for testing when LLM is disabled.

    Args:
        user_prompt (str): The user prompt (unused in mock responses).
        schema (type): The Pydantic schema type to generate mock data for.

    Returns:
        BaseModel: A mock response instance of the specified schema.

    Raises:
        ValueError: If no mock is defined for the given schema type.

    """
    try:
        # Criar dados mock específicos para cada tipo de schema
        if schema is SummaryContent:
            return schema(content="Resumo mock gerado automaticamente.")
        elif schema is GeneralGuidelinesContent:
            return schema(content="Diretrizes gerais mock geradas automaticamente.")
        elif schema is ClosingNoteContent:
            return schema(content="Nota de encerramento mock gerada automaticamente.")
        elif schema is FoodRecommendationSectionWrapper:
            return schema(items=[])
        elif schema is LifestyleRecommendationSectionWrapper:
            return schema(items=[])
        elif schema is SupplementRecommendationSectionWrapper:
            return schema(items=[])
        elif schema is DeficiencyRecommendationSectionWrapper:
            return schema(items=[])
        elif schema is ExamsRecommendationSectionWrapper:
            return schema(items=[])
        else:
            # Para outros schemas, tentar criar com dados vazios
            if hasattr(schema, "model_validate"):
                return schema.model_validate({})
            else:
                return schema()
    except Exception as e:
        logger.error(f"Erro ao criar mock para schema {schema}: {e}")
        raise ValueError(f"Mock não definido para o schema: {schema}") from e


class LLMService:
    """Service for interacting with language models to generate structured content.

    This class provides methods for calling LLM APIs with structured output,
    generating prompts from medical data, and handling mock responses when
    LLM functionality is disabled.

    Attributes:
        model_name (str): Human-readable name of the model.
        model_id (str): Identifier used for API calls.
        api_key (str): API key for authentication.
        client (AsyncOpenAI): OpenAI client instance.

    """

    def __init__(
        self,
        model_name: str,
        model_id: str,
        api_key: str | None = None,
        router_api: str | None = None,
    ):
        """Initialize the LLM service.

        Args:
            model_name (str): Human-readable name of the model.
            model_id (str): Model identifier for API calls.
            api_key (str, optional): API key for authentication.
            router_api (str, optional): Base URL for the API router.

        Raises:
            ValueError: If api_key or router_api is not provided.

        """
        if not api_key:
            raise ValueError(
                "A chave da API (api_key) é obrigatória e não foi fornecida."
            )
        if not router_api:
            raise ValueError(
                "A URL da API (router_api) é obrigatória e não foi fornecida."
            )
        self.model_name = model_name
        self.model_id = model_id
        self.api_key = api_key
        self.client = AsyncOpenAI(api_key=self.api_key, base_url=router_api)

    @mlflow.trace(name="call_llm_api", span_type="llm")
    async def call_llm_api(
        self,
        user_prompt: str,
        schema: type | None,
        system_prompt: str | None = None,
        temperature: float = 0.3,
        max_tokens: int = 4096,
        **kwargs,
    ) -> BaseModel | str:
        """Call the LLM API with optional structured output parsing.

        Args:
            user_prompt (str): The user message to send to the model.
            schema (type | None): Pydantic model class for structured output, or None for plain text.
            system_prompt (str, optional): Optional system prompt.
            temperature (float, optional): Sampling temperature. Defaults to 0.3.
            max_tokens (int, optional): Maximum tokens to generate. Defaults to 4096.
            **kwargs: Additional keyword arguments.

        Returns:
            BaseModel | str: Validated response matching the schema, or plain text if schema is None.

        Raises:
            ValueError: If validation fails or API call errors occur.

        """
        # Utilizar mocks quando o LLM estiver desabilitado
        if not settings.ENABLE_LLM:
            if schema is None:
                return "Mock markdown response generated when LLM is disabled."
            dummy_response = get_mock_response(user_prompt, schema)
            return dummy_response

        try:
            messages: list[ChatCompletionMessageParam] = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt.strip()})
            messages.append({"role": "user", "content": user_prompt})

            logger.debug(
                f"Calling LLM API with model: {self.model_id}, user prompt length: {len(user_prompt)}"
            )

            if schema is None:
                # For plain text responses (like markdown), use regular completions
                completion = await self.client.chat.completions.create(
                    model=self.model_id,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                response_content = completion.choices[0].message.content
                if response_content is None:
                    raise ValueError("LLM returned None response")
                return response_content
            else:
                # For structured responses, use parse
                completion = await self.client.beta.chat.completions.parse(
                    model=self.model_id,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    response_format=schema,
                )
                validated_response = completion.choices[0].message.parsed
                if validated_response is None:
                    raise ValueError("LLM returned None response")
                return validated_response

        except ValidationError as e:
            error_msg = (
                f"LLM response failed Pydantic validation for schema {schema}: {e}"
            )
            logger.error(f"[VALIDATION ERROR]: {error_msg}")
            raise ValueError(error_msg) from e
        except Exception as e:
            error_msg = (
                f"Cannot query model '{self.model_name}' or process response: {str(e)}"
            )
            logger.error(f"[API ERROR]: {error_msg}")
            raise ValueError(error_msg) from e

    def generate_prompt(
        self,
        section: str,
        exam_data: TNMExamData,
        anamnesis: PatientAnamnesis,
        kg_data: KGResult,
    ) -> str:
        """Generate prompts for each report section based on knowledge graph data.

        Args:
            section (str): The report section name.
            exam_data (TNMExamData): Examination data.
            anamnesis (PatientAnamnesis): Patient anamnesis data.
            kg_data (KGResult): Knowledge graph query results.

        Returns:
            str: Formatted prompt string for the LLM.

        """
        with start_span(name=f"{section} Prompt"):
            altered_metabs = safe_join(
                [
                    f"- {m.name} ({m.status} - valor: {m.value}, referência: {m.reference_range.min} a {m.reference_range.max})"
                    for m in kg_data.metabolite_info
                ]
            )

            manifestations = safe_join(
                [
                    f"- {m.description} ({m.affected_system}, gravidade: {m.severity})"
                    for m in kg_data.manifestations
                    if m.description
                ]
            )

            interventions = safe_join(
                [
                    f"- {i.type}: {i.description} (prioridade: {i.priority})"
                    for i in kg_data.recommended_interventions
                    if i.description
                ]
            )

            foods = safe_join(
                [
                    f"- {f.name} ({f.food_group}, frequência: {f.consumption_frequency})"
                    for f in kg_data.foods
                    if f.name
                ]
            )

            supplements = safe_join(
                [
                    f"- {s.name} ({s.active_composition}, dose: {s.dosage.minimum}–{s.dosage.maximum} {s.dosage.unit})"
                    for s in kg_data.supplements
                    if s.name and s.dosage is not None
                ]
            )

        pathways = safe_join(
            [
                f"- {p.name}: {p.clinical_importance}"
                for p in kg_data.pathway_impacts
                if p.name
            ]
        )

        medications_list = []
        medications_formatted_list = []
        if anamnesis.context_factors.medications:
            for m in anamnesis.context_factors.medications:
                if hasattr(m, "name"):
                    medications_list.append(m.name)
                    if (
                        hasattr(m, "status")
                        and hasattr(m, "value")
                        and hasattr(m, "unit")
                        and hasattr(m, "reference_range")
                        and hasattr(m.reference_range, "min")
                        and hasattr(m.reference_range, "max")
                    ):
                        medications_formatted_list.append(
                            f"- {m.name} (status: {m.status}, valor: {m.value}, referência: {m.reference_range.min} a {m.reference_range.max})"
                        )
                    else:
                        medications_formatted_list.append(
                            f"- {m.name} (detalhes indisponíveis)"
                        )
                elif isinstance(m, str):
                    medications_list.append(m)
                    medications_formatted_list.append(f"- {m}")
                else:
                    logger.warning(
                        f"Unexpected item in medications list: {m} (type: {type(m)}). Skipping for context summary and detailed list."
                    )

            medications_str = (
                ", ".join(medications_list) if medications_list else "Nenhuma"
            )
            medications_detailed = safe_join(medications_formatted_list)

            context_summary = safe_encode(
                f"""
                Idade: {anamnesis.personal_data.age}
                Gênero: {anamnesis.personal_data.gender}
                IMC: {anamnesis.personal_data.bmi}
                Atividade física: {anamnesis.context_factors.physical_activity.intensity}
                Histórico médico: {", ".join(anamnesis.context_factors.medical_history)}
                Medicações: {medications_str} # Use the safely joined string here
                Intolerâncias: {", ".join(anamnesis.context_factors.intolerances)}
                """
            )

            prompt = f"""
                SISTEMA: Especialista em medicina nutricional - SEÇÃO {section.upper()}
                PACIENTE: {exam_data.patient_id}
                OBJETIVO CLÍNICO: {anamnesis.objective}
                CONTEXTO DO PACIENTE:
                {context_summary.strip()}
                METABÓLITOS ALTERADOS:
                {altered_metabs or "Nenhum alterado detectado."}
                MANIFESTAÇÕES CLÍNICAS:
                {manifestations or "Nenhuma manifestação registrada."}
                INTERVENÇÕES RECOMENDADAS:
                {interventions or "Nenhuma intervenção identificada."}
                ALIMENTOS RECOMENDADOS:
                {foods or "Nenhum alimento específico recomendado."}
                SUPLEMENTOS RECOMENDADOS:
                {supplements or "Nenhum suplemento específico recomendado."}
                VIAS METABÓLICAS AFETADAS:
                {pathways or "Nenhuma via afetada detectada."}
                MEDICAÇÕES EM USO (DETALHADO):
                {medications_detailed or "Nenhuma medicação detalhada."}
                RESPOSTA: Gerar conteúdo para a seção "{section}", com base nas informações clínicas e metabólicas acima.
                """

            return safe_encode(prompt)

        # Fallback (should never reach here)
        return f"Error: Could not generate prompt for section '{section}'"
