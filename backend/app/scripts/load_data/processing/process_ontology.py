"""Process ontology data module."""

import io
import logging
import os
import re
from typing import Any

import msoffcrypto
import pandas as pd

from app.scripts.load_data.utils.file_handler import save_to_json
from app.scripts.load_data.utils.text_processing import (
    clean_text,
    generate_slug,
    remove_common_prefixes,
)

logger = logging.getLogger(__name__)


def safe_get(row: pd.Series, column_name: str, default: Any = "") -> Any:
    """Safely gets a value from a DataFrame row, handling nulls."""
    value = row.get(column_name)
    return default if pd.isna(value) else str(value).strip()


def _initialize_ontology_structure() -> tuple[dict[str, Any], dict[str, set]]:
    """Initialize the ontology structure and tracking sets."""
    ontology: dict[str, Any] = {
        "metabolites": [],
        "metabolic_pathways": [],
        "manifestations": [],
        "interventions": [],
        "foods": [],
        "supplements": [],
        "contextual_factors": [],
        "scientific_evidence": [],
    }

    processed_items: dict[str, set] = {
        "pathways": set(),
        "foods": set(),
        "supplements": set(),
        "factors": set(),
        "evidence": set(),
        "manifestations": set(),
        "interventions": set(),
    }

    return ontology, processed_items


def _process_metabolite(
    row: pd.Series, metabolites_map: dict, pathway_id: str | None
) -> tuple[str, str]:
    """Process a single metabolite from a DataFrame row."""
    metabolite_name = safe_get(row, "METABÓLITOS TNM")
    if not metabolite_name:
        return "", ""

    # Clean metabolite name - remove the marker text
    if (
        " - Em negrito são os que faltam colocar as referencias a partir daqui e abaixo"
        in metabolite_name
    ):
        metabolite_name = metabolite_name.replace(
            " - Em negrito são os que faltam colocar as referencias a partir daqui e abaixo",
            "",
        )

    metabolite_id = f"metabolito-{generate_slug(metabolite_name)}"

    # Add or update metabolite in map
    if metabolite_id not in metabolites_map:
        metabolites_map[metabolite_id] = {
            "id": metabolite_id,
            "name": metabolite_name,
            "definition": clean_text(safe_get(row, "DEFINIÇÃO METABÓLITOS")),
            "food_sources": clean_text(safe_get(row, "FONTE ALIMENTAR / OBS.")),
            "metabolic_pathway": [pathway_id] if pathway_id else [],
            "manifestations": [],
        }
    elif pathway_id and pathway_id not in metabolites_map[metabolite_id].get(
        "metabolic_pathway", []
    ):
        metabolites_map[metabolite_id]["metabolic_pathway"].append(pathway_id)

    return metabolite_id, metabolite_name


def _process_metabolic_pathway(
    row: pd.Series,
    ontology: dict[str, Any],
    processed_items: dict[str, set],
    pathway_name: str,
    pathway_id: str | None,
) -> None:
    """Process a single metabolic pathway."""
    if pathway_id and pathway_id not in processed_items["pathways"]:
        processed_items["pathways"].add(pathway_id)
        ontology["metabolic_pathways"].append(
            {
                "id": pathway_id,
                "name": pathway_name,
                "definition": clean_text(safe_get(row, "DEFINIÇÃO VIAS")),
            }
        )


def _process_food_and_supplements(
    row: pd.Series, ontology: dict[str, Any], intervention_id: str, level_type: str
) -> tuple[str | None, str | None]:
    """Process food and supplement interventions for a given level."""
    food_id = None
    supplement_id = None

    # Process food conduct
    food_text = clean_text(safe_get(row, f"CONDUTA ALIMENTAÇÃO: NÍVEIS {level_type}"))
    if food_text:
        food_text = remove_common_prefixes(food_text)
        food_id = f"food-{intervention_id}"
        ontology["foods"].append(
            {
                "id": food_id,
                "description": food_text,
            }
        )

    # Process supplement conduct
    supplement_text = clean_text(
        safe_get(row, f"CONDUTA SUPLEMENTAÇÃO: NÍVEIS {level_type}")
    )
    if supplement_text:
        supplement_text = remove_common_prefixes(supplement_text)
        supplement_id = f"supplement-{intervention_id}"
        ontology["supplements"].append(
            {
                "id": supplement_id,
                "description": supplement_text,
            }
        )

    return food_id, supplement_id


def _process_manifestation_and_intervention(
    row: pd.Series,
    ontology: dict[str, Any],
    processed_items: dict[str, set],
    metabolite_id: str,
    pathway_slug: str,
    level_type: str,
    level_name: str,
    type_name: str,
    metabolites_map: dict[str, Any],
) -> None:
    """Process manifestations and interventions for a specific level (high/low)."""
    symptoms = safe_get(row, f"SINAIS E SINTOMAS: NÍVEIS {level_type}")
    if not symptoms:
        return

    manifestation_id = f"manifestacao-{level_name}-{metabolite_id}-{pathway_slug}"
    intervention_id = f"intervencao-{level_name}-{metabolite_id}-{pathway_slug}"

    # Process manifestation
    if manifestation_id not in processed_items["manifestations"]:
        processed_items["manifestations"].add(manifestation_id)
        ontology["manifestations"].append(
            {
                "id": manifestation_id,
                "description": clean_text(symptoms),
                "type": f"{type_name}Level",
                "metabolite": metabolite_id,
                "causes": clean_text(
                    safe_get(row, f"CAUSA: NÍVEIS {level_type} METABÓLITOS")
                ),
                "intervention": intervention_id,
            }
        )

        # Add manifestation to metabolite
        if metabolite_id in metabolites_map:
            metabolites_map[metabolite_id]["manifestations"].append(manifestation_id)

    # Process intervention
    if intervention_id not in processed_items["interventions"]:
        processed_items["interventions"].add(intervention_id)

        food_id, supplement_id = _process_food_and_supplements(
            row, ontology, intervention_id, level_type
        )

        # Add intervention with references to foods and supplements
        ontology["interventions"].append(
            {
                "id": intervention_id,
                "type": f"{type_name}Level",
                "description": f"Conduta alimentar ou suplementar para níveis {level_name} do metabólito.",
                "manifestation": manifestation_id,
                "foods": [food_id] if food_id else [],
                "supplements": [supplement_id] if supplement_id else [],
            }
        )


def _process_scientific_evidence(
    row: pd.Series, ontology: dict[str, Any], metabolite_id: str, pathway_slug: str
) -> None:
    """Process scientific evidence references for a metabolite."""
    referencias = safe_get(row, "REFERÊNCIAS", "")
    lista_referencias = [ref.strip() for ref in referencias.split("\n") if ref.strip()]

    for i, ref_text in enumerate(lista_referencias):
        ref_text_clean = re.sub(r"^\d+\)\s*", "", ref_text)
        ref_id = f"evidencia-{metabolite_id}-{pathway_slug}-{i}"
        ontology["scientific_evidence"].append(
            {"id": ref_id, "title": ref_text_clean, "metabolite": metabolite_id}
        )


def process_ontology_data(df: pd.DataFrame) -> dict[str, Any]:
    """Convert ontology DataFrame to a structured JSON dictionary.

    Treats food and supplement interventions as unique entities.
    """
    ontology, processed_items = _initialize_ontology_structure()
    metabolites_map: dict[str, Any] = {}

    # Iterate over each row in the DataFrame to build ontology entities
    for _, row in df.iterrows():
        # Process metabolite
        metabolite_id, metabolite_name = _process_metabolite(row, metabolites_map, None)
        if not metabolite_id:
            continue

        # Get pathway information
        pathway_name = safe_get(row, "VIAS TNM")
        pathway_id = f"via-{generate_slug(pathway_name)}" if pathway_name else None
        pathway_slug = generate_slug(pathway_name or "geral")

        # Update metabolite with pathway if not already added
        if pathway_id and pathway_id not in metabolites_map[metabolite_id].get(
            "metabolic_pathway", []
        ):
            metabolites_map[metabolite_id]["metabolic_pathway"].append(pathway_id)

        # Process metabolic pathway
        if pathway_name:
            _process_metabolic_pathway(
                row, ontology, processed_items, pathway_name, pathway_id
            )

        # Process low level manifestations and interventions
        _process_manifestation_and_intervention(
            row,
            ontology,
            processed_items,
            metabolite_id,
            pathway_slug,
            "BAIXOS",
            "baixos",
            "Low",
            metabolites_map,
        )

        # Process high level manifestations and interventions
        _process_manifestation_and_intervention(
            row,
            ontology,
            processed_items,
            metabolite_id,
            pathway_slug,
            "ALTOS",
            "altos",
            "High",
            metabolites_map,
        )

        # Process scientific evidence references
        _process_scientific_evidence(row, ontology, metabolite_id, pathway_slug)

    ontology["metabolites"] = list(metabolites_map.values())
    return ontology


def decrypt_and_read_excel(file_path: str, password: str) -> pd.DataFrame:
    """Decrypts and reads a password-protected Excel file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found:'{file_path}'")

    decrypted_buffer = io.BytesIO()
    with open(file_path, "rb") as f:
        office_file = msoffcrypto.OfficeFile(f)
        office_file.load_key(password=password)
        office_file.decrypt(decrypted_buffer)

    decrypted_buffer.seek(0)
    return pd.read_excel(decrypted_buffer, engine="openpyxl")


def main():
    """Orchestrate the ontology processing workflow.

    - Read and decrypt the Excel file
    - Process the data into hierarchical JSON
    - Save the result to disk
    """
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, "..", "data"))
    output_dir = os.path.abspath(os.path.join(script_dir, "..", "processed_data"))
    os.makedirs(output_dir, exist_ok=True)

    input_path = os.path.join(base_dir, "Anexo 4.xlsx")
    output_path = os.path.join(output_dir, "ontology.json")
    file_password = "241224"

    try:
        logger.info(f"Reading and decrypting the file:'{input_path}'...")
        df = decrypt_and_read_excel(input_path, file_password)

        df.columns = df.columns.str.strip()

        logger.info("Processing ontology data into hierarchical JSON format...")
        processed_ontology = process_ontology_data(df)

        save_to_json(processed_ontology, output_path)
        logger.info(f"Processing complete! Ontology saved in: '{output_path}'")

    except FileNotFoundError as e:
        logger.error(f"AFile not found. {e}")
    except msoffcrypto.exceptions.InvalidKeyError:
        logger.error(f"Incorrect password for file '{input_path}'.")
    except Exception as e:
        logger.error(f"Unexpected ERROR during processing: {e}")


if __name__ == "__main__":
    main()
