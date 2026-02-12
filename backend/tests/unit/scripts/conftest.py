"""Test configuration and fixtures for scripts tests."""

import pandas as pd
import pytest


@pytest.fixture
def sample_ontology_dataframe():
    """Return a sample DataFrame with ontology data for testing."""
    data = {
        "METABÓLITOS TNM": ["Glucose", "Iron", "Vitamin D"],
        "VIAS TNM": ["Glycolysis", "Iron Metabolism", "Vitamin D Synthesis"],
        "DEFINIÇÃO METABÓLITOS": [
            "Primary energy source",
            "Oxygen transport",
            "Bone health",
        ],
        "FONTE ALIMENTAR / OBS.": ["Carbohydrates", "Red meat", "Sunlight, fatty fish"],
        "DEFINIÇÃO VIAS": [
            "Energy production pathway",
            "Iron processing pathway",
            "Vitamin D production pathway",
        ],
        "SINAIS E SINTOMAS: NÍVEIS BAIXOS": [
            "Fatigue and weakness",
            "Anemia symptoms",
            "Bone pain",
        ],
        "CAUSA: NÍVEIS BAIXOS METABÓLITOS": [
            "Low energy levels",
            "Iron deficiency",
            "Vitamin D deficiency",
        ],
        "CONDUTA ALIMENTAÇÃO: NÍVEIS BAIXOS": [
            "Increase carbohydrate intake",
            "Eat more red meat",
            "Increase fatty fish consumption",
        ],
        "CONDUTA SUPLEMENTAÇÃO: NÍVEIS BAIXOS": [
            "Take vitamin B complex",
            "Take iron supplements",
            "Take vitamin D supplements",
        ],
        "SINAIS E SINTOMAS: NÍVEIS ALTOS": [
            "Hyperglycemia symptoms",
            "Iron overload symptoms",
            "Vitamin D toxicity symptoms",
        ],
        "CAUSA: NÍVEIS ALTOS METABÓLITOS": [
            "High blood sugar",
            "Iron excess",
            "Vitamin D excess",
        ],
        "CONDUTA ALIMENTAÇÃO: NÍVEIS ALTOS": [
            "Reduce carbohydrate intake",
            "Reduce red meat consumption",
            "Reduce fatty fish consumption",
        ],
        "CONDUTA SUPLEMENTAÇÃO: NÍVEIS ALTOS": [
            "Monitor blood sugar",
            "Monitor iron levels",
            "Monitor vitamin D levels",
        ],
        "REFERÊNCIAS": [
            "1) Study A - Glucose metabolism\n2) Study B - Energy pathways",
            "3) Study C - Iron metabolism\n4) Study D - Anemia treatment",
            "5) Study E - Vitamin D synthesis\n6) Study F - Bone health",
        ],
    }
    return pd.DataFrame(data)


@pytest.fixture
def empty_dataframe():
    """Return an empty DataFrame for testing edge cases."""
    return pd.DataFrame()


@pytest.fixture
def single_metabolite_dataframe():
    """Return a DataFrame with a single metabolite for focused testing."""
    data = {
        "METABÓLITOS TNM": ["Glucose"],
        "VIAS TNM": ["Glycolysis"],
        "DEFINIÇÃO METABÓLITOS": ["Primary energy source"],
        "FONTE ALIMENTAR / OBS.": ["Carbohydrates"],
        "DEFINIÇÃO VIAS": ["Energy production pathway"],
        "SINAIS E SINTOMAS: NÍVEIS BAIXOS": ["Fatigue"],
        "CAUSA: NÍVEIS BAIXOS METABÓLITOS": ["Low energy"],
        "CONDUTA ALIMENTAÇÃO: NÍVEIS BAIXOS": ["Eat more carbs"],
        "CONDUTA SUPLEMENTAÇÃO: NÍVEIS BAIXOS": ["Take B vitamins"],
        "REFERÊNCIAS": ["Study A - Glucose metabolism"],
    }
    return pd.DataFrame(data)


@pytest.fixture
def metabolite_without_pathway_dataframe():
    """Return a DataFrame with a metabolite that has no pathway."""
    data = {
        "METABÓLITOS TNM": ["Unknown Metabolite"],
        "VIAS TNM": [""],
        "DEFINIÇÃO METABÓLITOS": ["Unknown function"],
        "FONTE ALIMENTAR / OBS.": ["Unknown sources"],
        "DEFINIÇÃO VIAS": [""],
        "SINAIS E SINTOMAS: NÍVEIS BAIXOS": ["Unknown symptoms"],
        "CAUSA: NÍVEIS BAIXOS METABÓLITOS": ["Unknown cause"],
        "CONDUTA ALIMENTAÇÃO: NÍVEIS BAIXOS": ["Unknown diet"],
        "CONDUTA SUPLEMENTAÇÃO: NÍVEIS BAIXOS": ["Unknown supplements"],
        "REFERÊNCIAS": [""],
    }
    return pd.DataFrame(data)
