"""Unit tests for ontology data validation."""

from app.validators.ontology_data_validator import OntologyDataValidator


def test_valid_ontology_data(valid_metabolite_data):
    """Test ontology validation."""
    validator = OntologyDataValidator(valid_metabolite_data)
    is_valid, errors = validator.validate()

    assert is_valid is True
    assert errors == []


def test_missing_id(missing_id_data):
    """Test validation of missing id."""
    validator = OntologyDataValidator(missing_id_data)
    is_valid, errors = validator.validate()

    assert is_valid is False
    assert "metabolites[0] is missing 'id'." in errors


def test_duplicate_id(duplicate_id_data):
    """Test validation if there is a duplicate id."""
    validator = OntologyDataValidator(duplicate_id_data)
    is_valid, errors = validator.validate()

    assert is_valid is False
    assert "Duplicated ID 'm1' in 'metabolites'." in errors
