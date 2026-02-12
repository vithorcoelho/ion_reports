"""Unit tests for IonNutri prompt generation."""

from app.domain.kg_result import KGResult
from app.plugins.prompts.ionnutri_prompts import IonNutriPrompts


def test_get_deficiencies_prompt_generates_correct_format(
    sample_anamnesis, sample_exam_data, mock_knowledge_query_configured
):
    """Testa se get_deficiencies_prompt gera um prompt correto para a seção 'deficiencies'."""
    kg_result = mock_knowledge_query_configured.execute_unified_query.return_value
    prompts = IonNutriPrompts()
    system_prompt, user_prompt = prompts.get_deficiencies_prompt(
        sample_exam_data, sample_anamnesis, kg_result
    )

    assert isinstance(system_prompt, str)
    assert isinstance(user_prompt, str)
    assert "PAT001" in user_prompt
    assert "DADOS DO PACIENTE" in user_prompt
    assert "DADOS METABÓLICOS" in user_prompt
    assert "medicina nutricional" in system_prompt.lower()

    # Verifica se contém os dados metabólicos esperados
    assert "L-carnitina" in user_prompt or "Alterações:" in user_prompt


def test_get_nutrition_prompt_generates_correct_format_with_section_name(
    sample_anamnesis, sample_exam_data, mock_knowledge_query_configured
):
    """Testa se get_nutrition_prompt gera um prompt correto para uma seção nutricional específica."""
    kg_result = mock_knowledge_query_configured.execute_unified_query.return_value
    prompts = IonNutriPrompts()
    section_name = "energetics"
    system_prompt, user_prompt = prompts.get_nutrition_prompt(
        sample_exam_data, sample_anamnesis, kg_result, section_name
    )

    assert isinstance(system_prompt, str)
    assert isinstance(user_prompt, str)
    assert "DADOS DO PACIENTE" in user_prompt
    assert "DADOS METABÓLICOS" in user_prompt
    assert "carboidratos" in user_prompt.lower()


def test_ionnutri_prompts_handles_empty_kg_data(
    sample_anamnesis, sample_exam_data, mocker
):
    """Testa se os métodos de prompt do IonNutriPrompts lidam corretamente com KGResult vazio."""
    empty_kg = KGResult(
        metabolite_info=[],
        manifestations=[],
        recommended_interventions=[],
        foods=[],
        supplements=[],
        pathway_impacts=[],
        scientific_evidence=[],
        contraindications=[],
    )

    prompts = IonNutriPrompts()

    # Testando get_findings_prompt com KG vazio
    sys_prompt, user_prompt = prompts.get_findings_prompt(
        sample_exam_data, sample_anamnesis, empty_kg
    )
    assert "DADOS DO PACIENTE" in user_prompt
    assert "DADOS METABÓLICOS" in user_prompt
    assert "Nenhuma via afetada detectada" in user_prompt
    assert "Nenhuma manifestação registrada" in user_prompt

    # Testando get_deficiencies_prompt com KG vazio
    sys_prompt, user_prompt = prompts.get_deficiencies_prompt(
        sample_exam_data, sample_anamnesis, empty_kg
    )
    assert "DADOS DO PACIENTE" in user_prompt
    assert "DADOS METABÓLICOS" in user_prompt

    # Testando get_nutrition_prompt com KG vazio
    sys_prompt, user_prompt = prompts.get_nutrition_prompt(
        sample_exam_data, sample_anamnesis, empty_kg, "energetics"
    )
    assert "DADOS DO PACIENTE" in user_prompt
    assert "DADOS METABÓLICOS" in user_prompt


def test_get_lifestyle_prompt_generates_correct_format(
    sample_anamnesis, sample_exam_data, mock_knowledge_query_configured
):
    """Testa se get_lifestyle_prompt gera um prompt correto para a seção 'lifestyle'."""
    kg_result = mock_knowledge_query_configured.execute_unified_query.return_value
    prompts = IonNutriPrompts()

    system_prompt, user_prompt = prompts.get_lifestyle_prompt(
        sample_exam_data, sample_anamnesis, kg_result
    )

    assert isinstance(system_prompt, str)
    assert isinstance(user_prompt, str)
    assert "DADOS DO PACIENTE" in user_prompt
    assert "DADOS METABÓLICOS" not in user_prompt
    assert "medicina nutricional" in system_prompt.lower()
