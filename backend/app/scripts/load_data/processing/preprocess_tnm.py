"""Processes patient exam data.

This script reads an Excel file containing metabolite scores for multiple individuals,
standardizes metabolite names using a canonical map, and structures the data in JSON format
to be loaded into the knowledge graph.
"""

import logging
import os
from typing import Any

import pandas as pd

from app.scripts.load_data.utils.constants import NAME_MAP
from app.scripts.load_data.utils.file_handler import read_data_file, save_to_json
from app.scripts.load_data.utils.text_processing import (
    extract_numeric_value,
    generate_slug,
)

logger = logging.getLogger(__name__)


def process_patient_data(df: pd.DataFrame) -> list[dict[str, Any]]:
    """Structures patient data into a list of JSON dictionaries.

    For each patient in the DataFrame, this function:
    - Extracts the sample ID.
    - Iterates over metabolite columns.
    - Normalizes the metabolite name using `NAME_MAP`.
    - Generates a standardized ID for the metabolite.
    - Formats the output as a JSON object containing exam data.
    """
    data_columns = {"SampleID"}
    metabolite_columns = [
        col for col in df.columns if col not in data_columns and pd.notna(col)
    ]

    patients_list = []
    for _, row in df.iterrows():
        patient_id = str(row["SampleID"]).strip()
        metabolites = []

        for col_name in metabolite_columns:
            value = extract_numeric_value(row[col_name])
            if value is not None:
                raw_name = str(col_name).strip()

                # Use the centralized map to get the canonical name
                canonical_name = NAME_MAP.get(raw_name, raw_name)
                metabolite_id = f"metabolito-{generate_slug(canonical_name)}"

                metabolites.append(
                    {
                        "id": metabolite_id,
                        "name": canonical_name,
                        "value": value,
                        "unit": "μM",
                    }
                )

        patient_exam = {
            "exam_data": {
                "patient_id": patient_id,
                "exam_date": "2025-07-02T00:00:00Z",
                "metabolites": metabolites,
            }
        }
        patients_list.append(patient_exam)

    return patients_list


def main():
    """Orchestrates the preprocessing flow for patient data.

    Defines input and output file paths, reads the data file,
    processes it, and saves the result in JSON format.
    """
    base_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    output_dir = os.path.join(os.path.dirname(__file__), "..", "processed_data")
    os.makedirs(output_dir, exist_ok=True)

    input_path = os.path.join(base_dir, "Anexo 06B.xlsx")
    output_path = os.path.join(output_dir, "patient_scores_ionnutri.json")

    try:
        df = read_data_file(input_path)
        processed_patients = process_patient_data(df)
        save_to_json(processed_patients, output_path)
    except (FileNotFoundError, ValueError) as e:
        logger.error(f"ERROR: {e}")


if __name__ == "__main__":
    main()
