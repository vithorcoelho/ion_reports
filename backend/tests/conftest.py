"""Test configuration and fixtures for the IonNutri application."""

from datetime import date

import pytest
from fastapi.testclient import TestClient
from pydantic import BaseModel

from app.core.config import settings
from app.domain.kg_result import (
    Contraindication,
    Intervention,
    KGResult,
    Manifestation,
    MetaboliteInfo,
    PathwayImpact,
    RecommendedFood,
    RecommendedSupplement,
    ReferenceRange,
    ScientificEvidence,
    SupplementDosage,
)

# Schemas de domínio retornados pelo LLM
from app.domain.report import (
    ClosingNoteContent,
    DeficiencyItem,
    DeficiencyRecommendationSectionWrapper,
    ExamItem,
    ExamsRecommendationSectionWrapper,
    FindingItem,
    FindingsSection,
    FoodItem,
    FoodRecommendationSectionWrapper,
    GeneralGuidelinesContent,
    LifestyleItem,
    LifestyleRecommendationSectionWrapper,
    NutritionalRecs,
    RecommendationsSection,
    SummaryContent,
    SupplementItem,
    SupplementRecommendationSectionWrapper,
)
from app.main import app
from app.schemas.exam import Metabolite, TNMExamData
from app.schemas.patient_anamnesis import (
    AlcoholConsumption,
    ContextFactors,
    IonNutriAnamnesis,
    Medication,
    PersonalData,
    PhysicalActivity,
    Sleep,
)
from app.services.llm.llm_service import OpenRouterLLMService
from app.services.report.strategy_factory import StrategyFactory
from app.services.report_coordinator import ReportCoordinator


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture
def sample_exam_data():
    """Provide example data for tests."""
    return TNMExamData(
        patient_id="PAT001",
        exam_date=date.today(),
        metabolites=[
            Metabolite(
                name="Glucose",
                value=95.5,
            ),
            Metabolite(
                name="Cholesterol",
                value=220.0,
            ),
            Metabolite(
                name="Vitamin_B12",
                value=150.0,
            ),
        ],
    )


@pytest.fixture
def sample_anamnesis():
    """Provide example anamnesis data for tests."""
    return IonNutriAnamnesis(
        patient_id="PAT001",
        anamnesis_type="ionnutri",
        objective="Melhorar saúde metabólica",
        personal_data=PersonalData(
            age=35, gender="F", weight=65.0, height=1.65, bmi=23.9
        ),
        context_factors=ContextFactors(
            medical_history=["hipertensão leve"],
            intolerances=["lactose"],
            physical_activity=PhysicalActivity(
                type="caminhada", frequency="3x por semana", intensity="moderada"
            ),
            sleep=Sleep(quality="boa", hours=8.0, issues=[]),
            alcohol_consumption=AlcoholConsumption(
                frequency="2x por semana", amount="1 taça"
            ),
            medications=[Medication(name="Losartana", frequency="1x/dia", dosage=None)],
            stress_level="moderado",
        ),
        family_history={"pai": "hipertensão", "mãe": "diabetes tipo 2"},
        environmental_exposure={"agrotóxicos": "baixa", "metais_pesados": "nenhuma"},
    )


@pytest.fixture
def llm_section_based_side_effect():
    """Retorna uma função side_effect assíncrona para mockar call_llm."""

    async def mock_call_llm_side_effect(
        user_prompt: str,
        schema: type[BaseModel] | None = None,
        temperature: float = 0.3,
        max_tokens: int = 4096,
        system_prompt: str | None = None,
        **kwargs,
    ):
        if schema == SummaryContent:
            return SummaryContent(content="Resumo gerado pelo LLM para o paciente.")
        elif schema == FindingsSection:
            return FindingsSection(
                items=[
                    FindingItem(
                        status="NORMAL",
                        description="Um achado mockado importante.",
                        metabolite="Metabólito Teste",
                        implications=["Implicação mockada 1", "Implicação mockada 2"],
                        metabolite_status={
                            "status": "NORMAL",
                            "cor": "Verde",
                            "classificacao": "Dentro da Faixa de Referência",
                            "score": 3,
                            "analise": "Níveis dentro da faixa de referência considerada adequada.",
                        },
                    )
                ],
                conclusion="Conclusão mockada para a de Achados.",
            )
        elif schema == FoodRecommendationSectionWrapper:
            # Provide a default mock response for any FoodRecommendationSectionWrapper request
            if "energetics" in user_prompt.lower() or "energia" in user_prompt.lower():
                return FoodRecommendationSectionWrapper(
                    items=[
                        FoodItem(
                            name="Mock Carboidrato",
                            quantity="100g",
                            frequency="diariamente",
                            observation="fonte de energia",
                        )
                    ]
                )
            elif (
                "constructors" in user_prompt.lower()
                or "construtores" in user_prompt.lower()
                or "protein" in user_prompt.lower()
            ):
                return FoodRecommendationSectionWrapper(
                    items=[
                        FoodItem(
                            name="Mock Proteína",
                            quantity="50g",
                            frequency="diariamente",
                            observation="para músculos",
                        )
                    ]
                )
            elif (
                "regulators" in user_prompt.lower()
                or "reguladores" in user_prompt.lower()
                or "vitamin" in user_prompt.lower()
            ):
                return FoodRecommendationSectionWrapper(
                    items=[
                        FoodItem(
                            name="Mock Vegetal Folhoso",
                            quantity="1 porção",
                            frequency="diariamente",
                            observation="vitaminas e minerais",
                        )
                    ]
                )
            elif "fats" in user_prompt.lower() or "gorduras" in user_prompt.lower():
                return FoodRecommendationSectionWrapper(
                    items=[
                        FoodItem(
                            name="Mock Azeite",
                            quantity="1 colher",
                            frequency="diariamente",
                            observation="gordura saudável",
                        )
                    ]
                )
            else:
                # Default fallback for any unrecognized food recommendation request
                return FoodRecommendationSectionWrapper(
                    items=[
                        FoodItem(
                            name="Mock Alimento Geral",
                            quantity="variável",
                            frequency="variável",
                            observation="alimento geral mockado",
                        )
                    ]
                )
        elif schema == LifestyleRecommendationSectionWrapper:
            return LifestyleRecommendationSectionWrapper(
                items=[
                    LifestyleItem(
                        category="Exercício",
                        description="Caminhada leve 30 min",
                        rationale="Saúde cardiovascular",
                    )
                ]
            )
        elif schema == SupplementRecommendationSectionWrapper:
            return SupplementRecommendationSectionWrapper(
                items=[
                    SupplementItem(
                        name="Mock Suplemento Vit D",
                        dosage="2000 UI",
                        frequency="1x ao dia",
                        purpose="Níveis adequados de Vit D",
                        observation="mocked supp",
                    )
                ]
            )
        elif schema == DeficiencyRecommendationSectionWrapper:
            return DeficiencyRecommendationSectionWrapper(
                items=[
                    DeficiencyItem(
                        nutrient="Vitamina D",
                        description="Baixos níveis de Vitamina D",
                        symptoms=["Fadiga"],
                        recommendations=["Suplementação"],
                    )
                ]
            )
        elif schema == ExamsRecommendationSectionWrapper:
            return ExamsRecommendationSectionWrapper(
                items=[
                    ExamItem(
                        name="Exame de Imagem",
                        purpose="Para avaliar xyz",
                        urgency="Média",
                    )
                ]
            )
        elif schema == GeneralGuidelinesContent:
            return GeneralGuidelinesContent(
                content="Siga as orientações do nutricionista."
            )
        elif schema == ClosingNoteContent:
            return ClosingNoteContent(
                content="Relatório gerado automaticamente pelo sistema TNM."
            )
        elif schema == RecommendationsSection:
            return RecommendationsSection(
                nutritional=NutritionalRecs(
                    energetics=[
                        FoodItem(
                            name="Mock Alimento Energético",
                            quantity="100g",
                            frequency="diariamente",
                            observation="alimento energético mockado",
                        )
                    ],
                    constructors=[
                        FoodItem(
                            name="Mock Alimento Construtor",
                            quantity="50g",
                            frequency="diariamente",
                            observation="alimento construtor mockado",
                        )
                    ],
                    regulators=[
                        FoodItem(
                            name="Mock Alimento Regulador",
                            quantity="1 porção",
                            frequency="diariamente",
                            observation="alimento regulador mockado",
                        )
                    ],
                    fats=[
                        FoodItem(
                            name="Mock Alimento Gordura",
                            quantity="1 colher",
                            frequency="diariamente",
                            observation="gordura saudável mockada",
                        )
                    ],
                ),
                lifestyle=[
                    LifestyleItem(
                        category="Exercício",
                        description="Caminhada leve 30 min",
                        rationale="Saúde cardiovascular",
                    )
                ],
                supplements=[
                    SupplementItem(
                        name="Mock Suplemento",
                        dosage="1000mg",
                        frequency="1x ao dia",
                        purpose="Suplementação mockada",
                        observation="suplemento mockado",
                    )
                ],
            )
        elif schema is None:
            # Return markdown content when no schema is specified
            return "# Relatório de Avaliação Nutricional\n\n## Dados do Paciente\n- **ID do Paciente:** PAT001\n- **Objetivo:** Melhorar saúde nutricional\n\n## Resumo\nResumo gerado pelo LLM para o paciente.\n\n## Achados\nConclusão mockada para a seção de Achados.\n\n## Recomendações\n### Suplementos\n- Mock Suplemento: 1000mg, 1x ao dia\n\n### Alimentos\n- Mock Carboidrato: 100g diariamente\n- Mock Proteína: 150g diariamente"
        else:
            raise ValueError(
                f"Mock de resposta LLM não definido para o schema: {schema.__name__}"
            )

    return mock_call_llm_side_effect


@pytest.fixture
def mock_llm_service_configured(mocker, llm_section_based_side_effect):
    """Mock configurado do LLM Service com retorno controlado de call_llm."""
    mock_llm_service = mocker.MagicMock(spec=OpenRouterLLMService)

    # Note: generate_prompt is not available in OpenRouterLLMService

    mock_llm_service.call_llm = mocker.AsyncMock(
        side_effect=llm_section_based_side_effect
    )

    # Also mock the call_llm method used by the Strategy Pattern
    # Create adapter to handle both 'prompt' and 'user_prompt' parameters
    async def call_llm_adapter(
        user_prompt: str | None = None, prompt: str | None = None, schema=None, **kwargs
    ):
        # Handle both old 'prompt' and new 'user_prompt' parameter names
        actual_prompt = user_prompt or prompt
        return await llm_section_based_side_effect(
            user_prompt=actual_prompt, schema=schema, **kwargs
        )

    mock_llm_service.call_llm = mocker.AsyncMock(side_effect=call_llm_adapter)

    return mock_llm_service


@pytest.fixture
def mock_knowledge_query_configured(mocker):
    """Mock configured for Neo4jKnowledgeQuery with a specific TNMResult result."""
    mock_knowledge_query = mocker.AsyncMock()

    mock_kg_result = KGResult(
        metabolite_info=[
            MetaboliteInfo(
                name="L-carnitina",
                value=25.0,
                status="deficit_severo",
                description="Metabólito L-carnitina apresenta status deficit_severo",
                reference_range=ReferenceRange(min=30.0, max=100.0),
            )
        ],
        manifestations=[
            Manifestation(
                metabolite="L-carnitina",
                status="deficit_severo",
                description="Fadiga muscular severa",
                type="Sintoma",
                severity="Severa",
            )
        ],
        recommended_interventions=[
            Intervention(
                metabolite="L-carnitina",
                type="Suplementação",
                description="Suplementar com L-carnitina",
                priority="Alta",
            )
        ],
        foods=[
            RecommendedFood(
                metabolite="L-carnitina",
                name="Carne vermelha",
                food_group="Proteínas",
                consumption_frequency="Moderada",
            )
        ],
        supplements=[
            RecommendedSupplement(
                metabolite="L-carnitina",
                name="L-Carnitina Tartarato",
                active_composition="L-Carnitina",
                dosage=SupplementDosage(minimum=500, maximum=2000, unit="mg"),
            )
        ],
        pathway_impacts=[
            PathwayImpact(
                metabolite="L-carnitina",
                name="Beta-oxidação",
                clinical_importance="Essencial para produção de energia a partir de gorduras",
            )
        ],
        scientific_evidence=[
            ScientificEvidence(
                metabolite="L-carnitina",
                title="Eficácia da L-carnitina na fadiga",
                study_type="Revisão Sistemática",
            )
        ],
        contraindications=[
            Contraindication(
                intervention="Alguma intervenção X",
                metabolite="L-carnitina",
                reason="Condição Y",
                type="medical_history",
            )
        ],
        deficiencies=[
            DeficiencyItem(
                nutrient="L-carnitina",
                description="Deficiência severa de L-carnitina, exigindo suplementação imediata.",
                symptoms=["Fadiga extrema", "Fraqueza muscular severa"],
                recommendations=["Suplementação de L-carnitina"],
                severity="severa",
            )
        ],
    )
    mock_knowledge_query.execute_unified_query.return_value = mock_kg_result

    return mock_knowledge_query


@pytest.fixture
def strategy_factory():
    """Provide a real StrategyFactory instance for tests."""
    return StrategyFactory()


@pytest.fixture
def mock_kg_service_for_strategies(mocker):
    """Mock KG service specifically for strategy testing."""
    mock_kg = mocker.Mock()

    async def mock_get_knowledge_data(exam_data, anamnesis):
        # Return mock KG result
        return KGResult()

    mock_kg.get_knowledge_data = mocker.AsyncMock(side_effect=mock_get_knowledge_data)
    return mock_kg


@pytest.fixture
def feature_flags_plugins():
    """Feature flags configured for plugins mode."""
    flags = settings
    flags.REPORT_GENERATION_MODE = "plugins"
    flags.USE_STRATEGY_PATTERN = False
    flags.ENABLE_MLFLOW_TRACING = True
    flags.ENABLE_KNOWLEDGE_GRAPH_CACHING = True
    return flags


@pytest.fixture
def feature_flags_strategy():
    """Feature flags configured for strategy mode."""
    flags = settings
    flags.REPORT_GENERATION_MODE = "strategy"
    flags.USE_STRATEGY_PATTERN = True
    flags.ENABLE_MLFLOW_TRACING = True
    flags.ENABLE_KNOWLEDGE_GRAPH_CACHING = True
    return flags


@pytest.fixture
def report_coordinator_plugins(
    mocker,
    mock_llm_service_configured,
    mock_knowledge_query_configured,
    feature_flags_plugins,
):
    """Return a ReportCoordinator instance configured for plugins mode."""
    # Mock feature flags to use plugins mode
    mock_feature_flags = mocker.patch(
        "app.services.report_coordinator.get_feature_flags"
    )
    mock_feature_flags.return_value.use_strategy_pattern = False
    return ReportCoordinator(
        llm_service=mock_llm_service_configured,
        knowledge_query=mock_knowledge_query_configured,
    )


@pytest.fixture
def report_coordinator_strategy(
    mocker,
    strategy_factory,
    mock_llm_service_configured,
    mock_kg_service_for_strategies,
    feature_flags_strategy,
):
    """Return a ReportCoordinator instance configured for strategy mode."""
    # Mock feature flags to use strategy mode
    mock_feature_flags = mocker.patch(
        "app.services.report_coordinator.get_feature_flags"
    )
    mock_feature_flags.return_value.use_strategy_pattern = True
    return ReportCoordinator(
        strategy_factory=strategy_factory,
        kg_service=mock_kg_service_for_strategies,
        base_llm_service=mock_llm_service_configured,
        prompt_registry=None,
        config_path="strategy_config.yaml",
    )


@pytest.fixture
def report_coordinator(
    report_coordinator_strategy,
):
    """Return default ReportCoordinator fixture using strategy mode for backward compatibility."""
    return report_coordinator_strategy


@pytest.fixture
def mock_mlflow(mocker):
    """Mock MLflow tracking functionality."""
    mocker.patch("mlflow.set_tracking_uri")
    mocker.patch("mlflow.set_experiment")
    mocker.patch("mlflow.log_params")
    mocker.patch("mlflow.log_metric")
    mocker.patch("mlflow.log_text")
    mocker.patch("mlflow.trace")
    mocker.patch("mlflow.MlflowClient")
    mocker.patch("mlflow.trace", side_effect=lambda *args, **kwargs: lambda func: func)
    # Mock the experiment creation to avoid the "Could not find experiment" error
    mock_experiment = mocker.MagicMock()
    mock_experiment.experiment_id = "test_experiment_id"
    mocker.patch("mlflow.get_experiment", return_value=mock_experiment)
    mocker.patch("mlflow.get_experiment_by_name", return_value=mock_experiment)
    # Mock start_run to return a context manager that doesn't fail
    mock_run = mocker.MagicMock()
    mock_run.__enter__ = mocker.MagicMock(return_value=mock_run)
    mock_run.__exit__ = mocker.MagicMock(return_value=None)
    mocker.patch("mlflow.start_run", return_value=mock_run)
    # Retorna None só para satisfazer o Pytest, se quiser pode retornar os mocks também
    return
