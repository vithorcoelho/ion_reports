"""Unit tests for ontology data processing."""

import pandas as pd

from app.scripts.load_data.processing.process_ontology import (
    process_ontology_data,
    safe_get,
)


def test_safe_get_with_valid_value():
    """Test safe_get returns the value when it exists."""
    row = pd.Series({"test_column": "test_value"})
    result = safe_get(row, "test_column")
    assert result == "test_value"


def test_safe_get_with_nan_value():
    """Test safe_get returns default value when value is NaN."""
    row = pd.Series({"test_column": float("nan")})
    result = safe_get(row, "test_column", "default")
    assert result == "default"


def test_safe_get_with_none_value():
    """Test safe_get returns default value when value is None."""
    row = pd.Series({"test_column": None})
    result = safe_get(row, "test_column", "default")
    assert result == "default"


def test_safe_get_with_empty_string():
    """Test safe_get returns empty string when value is empty string."""
    row = pd.Series({"test_column": ""})
    result = safe_get(row, "test_column")
    assert result == ""


def test_safe_get_strips_whitespace():
    """Test safe_get strips whitespace from values."""
    row = pd.Series({"test_column": "  test_value  "})
    result = safe_get(row, "test_column")
    assert result == "test_value"


def test_process_ontology_data_complete_flow(sample_ontology_dataframe):
    """Test the complete ontology processing flow with comprehensive data."""
    result = process_ontology_data(sample_ontology_dataframe)

    # Check basic structure
    expected_keys = {
        "metabolites",
        "metabolic_pathways",
        "manifestations",
        "interventions",
        "foods",
        "supplements",
        "contextual_factors",
        "scientific_evidence",
    }
    assert set(result.keys()) == expected_keys

    assert len(result["metabolites"]) == 3
    metabolite_names = [m["name"] for m in result["metabolites"]]
    assert "Glucose" in metabolite_names
    assert "Iron" in metabolite_names
    assert "Vitamin D" in metabolite_names

    assert len(result["metabolic_pathways"]) == 3
    pathway_names = [p["name"] for p in result["metabolic_pathways"]]
    assert "Glycolysis" in pathway_names
    assert "Iron Metabolism" in pathway_names
    assert "Vitamin D Synthesis" in pathway_names

    assert len(result["manifestations"]) == 6

    assert len(result["interventions"]) == 6

    assert len(result["foods"]) == 6
    assert len(result["supplements"]) == 6

    assert len(result["scientific_evidence"]) == 6


def test_process_ontology_data_empty_dataframe(empty_dataframe):
    """Test processing an empty DataFrame returns empty structure."""
    result = process_ontology_data(empty_dataframe)

    # Should return empty structure
    assert len(result["metabolites"]) == 0
    assert len(result["metabolic_pathways"]) == 0
    assert len(result["manifestations"]) == 0
    assert len(result["interventions"]) == 0
    assert len(result["foods"]) == 0
    assert len(result["supplements"]) == 0
    assert len(result["scientific_evidence"]) == 0


def test_process_ontology_data_single_metabolite(single_metabolite_dataframe):
    """Test processing a single metabolite with complete data."""
    result = process_ontology_data(single_metabolite_dataframe)

    assert len(result["metabolites"]) == 1
    assert result["metabolites"][0]["name"] == "Glucose"
    assert result["metabolites"][0]["definition"] == "Primary energy source"
    assert result["metabolites"][0]["food_sources"] == "Carbohydrates"

    assert len(result["metabolic_pathways"]) == 1
    assert result["metabolic_pathways"][0]["name"] == "Glycolysis"
    assert result["metabolic_pathways"][0]["definition"] == "Energy production pathway"

    assert len(result["manifestations"]) == 1
    assert len(result["interventions"]) == 1

    assert len(result["foods"]) == 1
    assert len(result["supplements"]) == 1

    assert len(result["scientific_evidence"]) == 1


def test_process_ontology_data_metabolite_without_pathway(
    metabolite_without_pathway_dataframe,
):
    """Test processing a metabolite that has no pathway information."""
    result = process_ontology_data(metabolite_without_pathway_dataframe)

    assert len(result["metabolites"]) == 1
    assert result["metabolites"][0]["name"] == "Unknown Metabolite"

    assert len(result["metabolites"][0]["metabolic_pathway"]) == 0

    assert len(result["metabolic_pathways"]) == 0

    assert len(result["manifestations"]) == 1
    assert len(result["interventions"]) == 1


def test_process_ontology_data_missing_metabolite_column():
    """Test processing when metabolite column is missing."""
    data = {"OTHER_COLUMN": ["Value1", "Value2"]}
    df = pd.DataFrame(data)
    result = process_ontology_data(df)

    assert len(result["metabolites"]) == 0
    assert len(result["metabolic_pathways"]) == 0
    assert len(result["manifestations"]) == 0
    assert len(result["interventions"]) == 0
    assert len(result["foods"]) == 0
    assert len(result["supplements"]) == 0
    assert len(result["scientific_evidence"]) == 0


def test_process_ontology_data_duplicate_metabolites():
    """Test that duplicate metabolites are handled correctly."""
    data = {
        "METABÓLITOS TNM": ["Glucose", "Glucose", "Iron"],
        "VIAS TNM": ["Glycolysis", "Pentose Phosphate", "Iron Metabolism"],
        "DEFINIÇÃO METABÓLITOS": ["Energy source", "Energy source", "Oxygen transport"],
        "FONTE ALIMENTAR / OBS.": ["Carbs", "Carbs", "Red meat"],
        "DEFINIÇÃO VIAS": ["Energy pathway", "Energy pathway", "Iron pathway"],
        "SINAIS E SINTOMAS: NÍVEIS BAIXOS": ["Fatigue", "Fatigue", "Anemia"],
        "CAUSA: NÍVEIS BAIXOS METABÓLITOS": [
            "Low energy",
            "Low energy",
            "Iron deficiency",
        ],
        "CONDUTA ALIMENTAÇÃO: NÍVEIS BAIXOS": ["Eat carbs", "Eat carbs", "Eat meat"],
        "CONDUTA SUPLEMENTAÇÃO: NÍVEIS BAIXOS": [
            "Take B vitamins",
            "Take B vitamins",
            "Take iron",
        ],
        "REFERÊNCIAS": ["Study A", "Study B", "Study C"],
    }
    df = pd.DataFrame(data)
    result = process_ontology_data(df)

    assert len(result["metabolites"]) == 2

    glucose_metabolite = next(
        m for m in result["metabolites"] if m["name"] == "Glucose"
    )
    assert len(glucose_metabolite["metabolic_pathway"]) == 2

    assert len(result["metabolic_pathways"]) == 3


def test_process_ontology_data_high_and_low_levels():
    """Test that both high and low level manifestations are processed."""
    data = {
        "METABÓLITOS TNM": ["Glucose"],
        "VIAS TNM": ["Glycolysis"],
        "DEFINIÇÃO METABÓLITOS": ["Energy source"],
        "FONTE ALIMENTAR / OBS.": ["Carbs"],
        "DEFINIÇÃO VIAS": ["Energy pathway"],
        "SINAIS E SINTOMAS: NÍVEIS BAIXOS": ["Fatigue"],
        "CAUSA: NÍVEIS BAIXOS METABÓLITOS": ["Low energy"],
        "CONDUTA ALIMENTAÇÃO: NÍVEIS BAIXOS": ["Eat carbs"],
        "CONDUTA SUPLEMENTAÇÃO: NÍVEIS BAIXOS": ["Take B vitamins"],
        "SINAIS E SINTOMAS: NÍVEIS ALTOS": ["Hyperglycemia"],
        "CAUSA: NÍVEIS ALTOS METABÓLITOS": ["High blood sugar"],
        "CONDUTA ALIMENTAÇÃO: NÍVEIS ALTOS": ["Reduce carbs"],
        "CONDUTA SUPLEMENTAÇÃO: NÍVEIS ALTOS": ["Monitor sugar"],
        "REFERÊNCIAS": ["Study A"],
    }
    df = pd.DataFrame(data)
    result = process_ontology_data(df)

    assert len(result["manifestations"]) == 2

    assert len(result["interventions"]) == 2

    manifestation_types = [m["type"] for m in result["manifestations"]]
    assert "LowLevel" in manifestation_types
    assert "HighLevel" in manifestation_types

    intervention_types = [i["type"] for i in result["interventions"]]
    assert "LowLevel" in intervention_types
    assert "HighLevel" in intervention_types


def test_process_ontology_data_scientific_evidence_formatting():
    """Test that scientific evidence references are properly formatted."""
    data = {
        "METABÓLITOS TNM": ["Glucose"],
        "VIAS TNM": ["Glycolysis"],
        "DEFINIÇÃO METABÓLITOS": ["Energy source"],
        "FONTE ALIMENTAR / OBS.": ["Carbs"],
        "DEFINIÇÃO VIAS": ["Energy pathway"],
        "SINAIS E SINTOMAS: NÍVEIS BAIXOS": ["Fatigue"],
        "CAUSA: NÍVEIS BAIXOS METABÓLITOS": ["Low energy"],
        "CONDUTA ALIMENTAÇÃO: NÍVEIS BAIXOS": ["Eat carbs"],
        "CONDUTA SUPLEMENTAÇÃO: NÍVEIS BAIXOS": ["Take B vitamins"],
        "REFERÊNCIAS": [
            "1) Study A - Glucose metabolism\n2) Study B - Energy pathways"
        ],
    }
    df = pd.DataFrame(data)
    result = process_ontology_data(df)

    assert len(result["scientific_evidence"]) == 2

    assert result["scientific_evidence"][0]["title"] == "Study A - Glucose metabolism"
    assert result["scientific_evidence"][1]["title"] == "Study B - Energy pathways"

    assert result["scientific_evidence"][0]["id"].startswith(
        "evidencia-metabolito-glucose-"
    )
    assert result["scientific_evidence"][1]["id"].startswith(
        "evidencia-metabolito-glucose-"
    )


def test_process_ontology_data_empty_cells():
    """Test processing when some cells contain empty values."""
    data = {
        "METABÓLITOS TNM": ["Glucose", "Iron"],
        "VIAS TNM": ["Glycolysis", ""],
        "DEFINIÇÃO METABÓLITOS": ["Energy source", "Oxygen transport"],
        "FONTE ALIMENTAR / OBS.": ["Carbs", "Red meat"],
        "DEFINIÇÃO VIAS": ["Energy pathway", ""],
        "SINAIS E SINTOMAS: NÍVEIS BAIXOS": ["Fatigue", ""],
        "CAUSA: NÍVEIS BAIXOS METABÓLITOS": ["Low energy", "Iron deficiency"],
        "CONDUTA ALIMENTAÇÃO: NÍVEIS BAIXOS": ["Eat carbs", "Eat meat"],
        "CONDUTA SUPLEMENTAÇÃO: NÍVEIS BAIXOS": ["Take B vitamins", "Take iron"],
        "REFERÊNCIAS": ["Study A", ""],
    }
    df = pd.DataFrame(data)
    result = process_ontology_data(df)

    assert len(result["metabolites"]) == 2
    assert len(result["metabolic_pathways"]) == 1
    assert result["metabolic_pathways"][0]["name"] == "Glycolysis"
    assert len(result["manifestations"]) == 1
    assert len(result["interventions"]) == 1
    assert len(result["scientific_evidence"]) == 1
