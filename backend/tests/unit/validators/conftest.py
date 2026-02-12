"""Test configuration and fixtures for validator tests."""

import pytest


@pytest.fixture
def valid_metabolite_data():
    """Include a metabolic pathway and a metabolite associated with it."""
    return {
        "metabolic_pathways": [{"id": "p1"}],
        "metabolites": [{"id": "m1", "metabolic_pathway": "p1"}],
    }


@pytest.fixture
def missing_id_data():
    """Validate missing 'id' in a metabolite."""
    return {"metabolites": [{"name": "Metabolite A"}]}


@pytest.fixture
def duplicate_id_data():
    """'id' duplication."""
    return {"metabolites": [{"id": "m1"}, {"id": "m1"}]}
