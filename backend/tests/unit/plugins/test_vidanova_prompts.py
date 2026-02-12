"""Unit tests for VidaNova prompt generation."""

from app.plugins.prompts.vidanova_prompts import VidaNovaPrompts


def test_get_summary_prompt_returns_brief_summary(
    sample_exam_data_novavida, sample_anamnesis_vida_novavida, sample_kg_result
):
    """Test that get_summary_prompt returns valid prompts with expected content."""
    prompts = VidaNovaPrompts()
    system_prompt, user_prompt = prompts.get_summary_prompt(
        sample_exam_data_novavida, sample_anamnesis_vida_novavida, sample_kg_result
    )

    assert isinstance(system_prompt, str)
    assert isinstance(user_prompt, str)
    assert len(user_prompt) > 0
    assert any(
        term in user_prompt.lower()
        for term in ["resumo", "metabolismo", "performance", "energia"]
    )


def test_get_findings_prompt_returns_clinical_findings_request(
    sample_exam_data_novavida, sample_anamnesis_vida_novavida, sample_kg_result
):
    """Test that get_findings_prompt returns valid clinical findings prompts."""
    prompts = VidaNovaPrompts()
    system_prompt, user_prompt = prompts.get_findings_prompt(
        sample_exam_data_novavida, sample_anamnesis_vida_novavida, sample_kg_result
    )

    assert isinstance(system_prompt, str)
    assert isinstance(user_prompt, str)
    assert (
        "principais achados clínicos" in user_prompt or "achados" in user_prompt.lower()
    )
    assert "dados metabólicos" in user_prompt


def test_get_diet_suggestions_prompt_returns_string(
    sample_exam_data_novavida, sample_anamnesis_vida_novavida, sample_kg_result
):
    """Test that get_diet_suggestions_prompt returns valid diet prompts."""
    prompts = VidaNovaPrompts()
    system_prompt, user_prompt = prompts.get_diet_suggestions_prompt(
        sample_exam_data_novavida, sample_anamnesis_vida_novavida, sample_kg_result
    )

    assert isinstance(system_prompt, str)
    assert isinstance(user_prompt, str)
    assert len(user_prompt) > 0
    assert any(
        term in user_prompt.lower()
        for term in ["dieta", "alimentos", "carnívoro", "vegetariano", "vegano"]
    )


def test_get_supplement_prompt_returns_string(
    sample_exam_data_novavida, sample_anamnesis_vida_novavida, sample_kg_result
):
    """Test that get_supplements_prompt returns valid supplement prompts."""
    prompts = VidaNovaPrompts()
    system_prompt, user_prompt = prompts.get_supplements_prompt(
        sample_exam_data_novavida, sample_anamnesis_vida_novavida, sample_kg_result
    )

    assert isinstance(system_prompt, str)
    assert isinstance(user_prompt, str)
    assert len(user_prompt) > 0
    assert any(
        term in user_prompt.lower()
        for term in ["suplementa", "performance", "energia", "recupera", "muscular"]
    )


def test_get_training_prompt_returns_training_recommendations(
    sample_exam_data_novavida, sample_anamnesis_vida_novavida, sample_kg_result
):
    """Test that get_training_prompt returns valid training recommendation prompts."""
    prompts = VidaNovaPrompts()
    system_prompt, user_prompt = prompts.get_training_prompt(
        sample_exam_data_novavida, sample_anamnesis_vida_novavida, sample_kg_result
    )

    assert isinstance(system_prompt, str)
    assert isinstance(user_prompt, str)
    assert len(user_prompt) > 0
    assert any(
        term in user_prompt.lower()
        for term in ["treino", "força", "hiit", "exercício", "massa"]
    )
