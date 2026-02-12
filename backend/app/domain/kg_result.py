"""Knowledge Graph result domain models.

This module contains Pydantic models representing the results from knowledge graph queries,
including metabolite information, interventions, recommendations, and scientific evidence.
"""

from typing import Any

from pydantic import BaseModel, Field


class ReferenceRange(BaseModel):
    """Reference range for metabolite values."""

    min: float = Field(..., description="Minimum reference value")
    max: float = Field(..., description="Maximum reference value")


class MetaboliteInfo(BaseModel):
    """Information about a metabolite and its status."""

    name: str = Field(..., description="Name")
    value: float = Field(..., description="Value")
    status: str = Field(
        ...,
        description="Status: deficit_severo, deficit_moderado, excesso_moderado, excesso_severo",
    )
    description: str = Field(default="", description="description")
    reference_range: ReferenceRange = Field(..., description="reference range")
    category: str = Field(default="", description="category")


class Manifestation(BaseModel):
    """Clinical manifestation related to metabolite alteration."""

    metabolite: str = Field(..., description="Target Name")
    status: str = Field(..., description="Status")
    description: str = Field(..., description="Description")
    type: str = Field(default="", description="Type")
    severity: str = Field(default="", description="Severity")
    affected_system: str = Field(default="", description="Affected")
    physiological_mechanism: str = Field(default="", description="Mechanism")


class Intervention(BaseModel):
    """Recommended intervention for metabolite correction."""

    metabolite: str = Field(..., description="Target metabolite")
    type: str = Field(..., description="Type")
    description: str = Field(..., description="Description")
    priority: str = Field(default="medium", description="Level")
    recommended_duration: str = Field(default="", description="Recommended duration")
    expected_results: str = Field(default="", description="Expected")
    is_contraindicated: bool = Field(default=False, description="Contraindicated")
    contraindication_reason: str = Field(
        default="", description="Reason for contraindication"
    )
    medication_interaction: str = Field(
        default="", description="Interacting medication"
    )


class RecommendedFood(BaseModel):
    """Food recommendation for metabolite correction."""

    metabolite: str = Field(..., description="Target metabolite")
    name: str = Field(..., description="Food")
    food_group: str = Field(default="", description="Food group")
    main_nutrients: list[str] = Field(
        default_factory=list, description="Main nutrients"
    )
    recommended_portion: str = Field(default="", description="Recommended portion")
    consumption_frequency: str = Field(default="", description="Consumption Frequency")


class SupplementDosage(BaseModel):
    """Supplement dosage information."""

    minimum: float = Field(..., description="Minimum dosage")
    maximum: float = Field(..., description="Maximum dosage")
    unit: str = Field(default="mg", description="Dosage unit")


class RecommendedSupplement(BaseModel):
    """Supplement recommendation for metabolite correction."""

    metabolite: str = Field(..., description="Target metabolite")
    name: str = Field(..., description="Supplement")
    active_composition: str = Field(default="", description="Active Composition")
    dosage: SupplementDosage | None = Field(
        default=None, description="Dosage information"
    )
    administration_form: str = Field(default="", description="Administration")


class PathwayImpact(BaseModel):
    """Metabolic pathway affected by metabolite alteration."""

    metabolite: str = Field(..., description="Related metabolite")
    name: str = Field(..., description="Pathway")
    definition: str = Field(default="", description="Pathway definition")
    biological_function: str = Field(default="", description="Biological function")
    clinical_importance: str = Field(default="", description="Clinical relevance")


class ScientificEvidence(BaseModel):
    """Scientific evidence supporting metabolite relationships."""

    metabolite: str = Field(..., description="Related metabolite")
    title: str = Field(..., description="Title")
    authors: str = Field(default="", description="Authors")
    year: str = Field(default="", description="Publication year")
    doi: str = Field(default="", description="DOI or URL")
    study_type: str = Field(default="", description="Type of study")
    evidence_level: str = Field(default="", description="Evidence quality level")


class Contraindication(BaseModel):
    """Contraindication information for interventions."""

    intervention: str = Field(..., description="Intervention")
    metabolite: str = Field(..., description="Metabolite")
    reason: str = Field(..., description="Contraindication reason")
    type: str = Field(
        ..., description="Type: medical_history or medication_interaction"
    )


class KGResult(BaseModel):
    """Complete result from TNM knowledge graph query."""

    metabolite_info: list[MetaboliteInfo] = Field(
        default_factory=list, description="Information about altered metabolites"
    )
    manifestations: list[Manifestation] = Field(
        default_factory=list,
        description="Clinical manifestations related to metabolite alterations",
    )
    recommended_interventions: list[Intervention] = Field(
        default_factory=list,
        description="Recommended interventions for metabolite correction",
    )
    foods: list[RecommendedFood] = Field(
        default_factory=list, description="Recommended foods for metabolite support"
    )
    supplements: list[RecommendedSupplement] = Field(
        default_factory=list,
        description="Recommended supplements for metabolite support",
    )
    pathway_impacts: list[PathwayImpact] = Field(
        default_factory=list, description="Metabolic pathways affected by alterations"
    )
    scientific_evidence: list[ScientificEvidence] = Field(
        default_factory=list,
        description="Scientific evidence supporting recommendations",
    )
    contraindications: list[Contraindication] = Field(
        default_factory=list,
        description="Contraindications for recommended interventions",
    )
    error: str | None = Field(default=None, description="Error message if query failed")

    @classmethod
    def create_error_result(cls, error_message: str) -> "KGResult":
        """Create a TNMResult with error information."""
        return cls(error=error_message)

    @classmethod
    def from_kg_data(cls, kg_data: dict[str, Any]) -> "KGResult":
        """Create TNMResult from knowledge graph raw data."""
        try:

            def safe_parse_list(model_class, data_list, required_field=None):
                parsed_items = []
                seen_items = set()  # Track seen items to avoid duplicates

                # Define unique identifier fields for each model class
                unique_field_map = {
                    MetaboliteInfo: "name",
                    Manifestation: "description",
                    Intervention: "description",
                    RecommendedFood: "name",
                    RecommendedSupplement: "name",
                    PathwayImpact: "name",
                    ScientificEvidence: "title",
                }

                # Get the unique field for this model class
                unique_field = unique_field_map.get(model_class, required_field)

                for item in data_list:
                    try:
                        # Skip empty items or items missing required fields
                        if not item or (
                            required_field and not item.get(required_field)
                        ):
                            continue

                        # Create a unique identifier for deduplication
                        if unique_field:
                            unique_id = item.get(unique_field, "")
                            if unique_id in seen_items:
                                continue
                            seen_items.add(unique_id)

                        # Handle special cases for nested models
                        if model_class == MetaboliteInfo:
                            # Ensure reference_range is properly structured
                            if (
                                "reference_range_min" in item
                                or "reference_range_max" in item
                            ):
                                item["reference_range"] = {
                                    "min": item.get("reference_range_min", 0),
                                    "max": item.get("reference_range_max", 0),
                                }

                        elif model_class == RecommendedSupplement:
                            # Ensure dosage is properly structured
                            if any(
                                key in item
                                for key in [
                                    "minimum_dosage",
                                    "maximum_dosage",
                                    "dosage_unit",
                                ]
                            ):
                                item["dosage"] = {
                                    "minimum": item.get("minimum_dosage", 0),
                                    "maximum": item.get("maximum_dosage", 0),
                                    "unit": item.get("dosage_unit", "mg"),
                                }

                        if hasattr(model_class, "model_validate"):
                            parsed_items.append(model_class.model_validate(item))
                        else:
                            parsed_items.append(model_class.parse_obj(item))

                    except Exception as e:
                        print(f"Warning: Failed to parse {model_class.__name__}: {e}")
                        continue

                return parsed_items

            # Parse each data type using the helper function
            metabolite_info = safe_parse_list(
                MetaboliteInfo, kg_data.get("metabolite_info", []), "name"
            )
            manifestations = safe_parse_list(
                Manifestation, kg_data.get("manifestations", []), "description"
            )
            interventions = safe_parse_list(
                Intervention, kg_data.get("interventions", []), "description"
            )
            foods = safe_parse_list(RecommendedFood, kg_data.get("foods", []), "name")
            supplements = safe_parse_list(
                RecommendedSupplement, kg_data.get("supplements", []), "name"
            )
            pathways = safe_parse_list(
                PathwayImpact, kg_data.get("pathways", []), "name"
            )
            evidence = safe_parse_list(
                ScientificEvidence, kg_data.get("evidence", []), "title"
            )

            # Handle contraindications from interventions
            contraindications_data = []
            for intervention in kg_data.get("interventions", []):
                if intervention.get("contraindicated"):
                    contraindications_data.append(
                        {
                            "intervention": intervention.get("description", ""),
                            "metabolite": intervention.get("metabolite", ""),
                            "reason": intervention.get("contraindication_reason", ""),
                            "type": (
                                "medical_history"
                                if intervention.get("contraindication_reason")
                                else "medication_interaction"
                            ),
                        }
                    )

            contraindications = safe_parse_list(
                Contraindication, contraindications_data
            )

            return cls(
                metabolite_info=metabolite_info,
                manifestations=manifestations,
                recommended_interventions=interventions,
                foods=foods,
                supplements=supplements,
                pathway_impacts=pathways,
                scientific_evidence=evidence,
                contraindications=contraindications,
            )

        except Exception as e:
            return cls.create_error_result(
                f"Error processing knowledge graph data: {str(e)}"
            )
