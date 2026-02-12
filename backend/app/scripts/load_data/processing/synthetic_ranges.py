"""Generates and processes reference ranges for metabolites.

This script reads a CSV file containing clinical intervals (scores from 1 to 5)
for each metabolite, normalizes their names, and structures the data in a JSON format
that can be merged with the main ontology. The goal is to enrich metabolite nodes in the graph
with their respective normality ranges.
"""

import os
from typing import Any

import pandas as pd

from app.scripts.load_data.types import Metabolite, ReferenceRange
from app.scripts.load_data.utils.constants import NAME_MAP
from app.scripts.load_data.utils.file_handler import read_data_file, save_to_json
from app.scripts.load_data.utils.text_processing import generate_slug

# Mapping of status to column name pairs in the new CSV format
COLUMN_MAP = {
    "DEFICIT_SEVERO": ("deficit_severo_min", "deficit_severo_max"),
    "DEFICIT_MODERADO": ("deficit_moderado_min", "deficit_moderado_max"),
    "NORMAL": ("normal_min", "normal_max"),
    "EXCESSO_MODERADO": ("excesso_moderado_min", "excesso_moderado_max"),
    "EXCESSO_SEVERO": ("excesso_severo_min", "excesso_severo_max"),
}


def process_reference_ranges(df: pd.DataFrame) -> dict[str, list[dict[str, Any]]]:
    """Process the DataFrame of ranges and convert it to a structured JSON format."""
    ontology_data: dict[str, list[ReferenceRange] | list[Metabolite]] = {
        "reference_ranges": [],
        "metabolites": [],
    }

    for _, row in df.iterrows():
        original_name = str(row["Metabolitos"]).strip()
        canonical_name = NAME_MAP.get(original_name, original_name)
        metabolite_id = f"metabolito-{generate_slug(canonical_name)}"
        range_id = f"range-{metabolite_id}"

        range_node = {
            "id": range_id,
            "name": f"Clinical interval for {canonical_name}",
            "unit": "μM",  # Assuming all values are in μM based on the data
        }

        # Add min/max values for each score using the new column structure
        for status, (min_col, max_col) in COLUMN_MAP.items():
            min_val = row[min_col] if pd.notna(row[min_col]) else None
            max_val = row[max_col] if pd.notna(row[max_col]) else None

            # Convert to float if not None
            if min_val is not None:
                try:
                    min_val = float(min_val)
                except (ValueError, TypeError):
                    min_val = None

            if max_val is not None:
                try:
                    max_val = float(max_val)
                except (ValueError, TypeError):
                    max_val = None

            range_node[f"{status.lower()}_min"] = min_val
            range_node[f"{status.lower()}_max"] = max_val

        ontology_data["reference_ranges"].append(range_node)

        # Create a corresponding metabolite node to facilitate graph loading
        ontology_data["metabolites"].append(
            {
                "id": metabolite_id,
                "name": canonical_name,
                "reference_range": [range_id],
            }
        )

    return ontology_data


def main():
    """Orchestrates the flow for generating reference ranges."""
    base_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    output_dir = os.path.join(os.path.dirname(__file__), "..", "processed_data")
    os.makedirs(output_dir, exist_ok=True)

    input_path = os.path.join(base_dir, "ionnutri_metabolite_ranges.csv")
    output_path = os.path.join(output_dir, "ontology_with_ranges.json")

    try:
        print(f"Reading data file from: {input_path}")
        df = read_data_file(input_path)
        print("Processing reference ranges...")
        processed_ranges = process_reference_ranges(df)
        print(f"Saving processed data to: {output_path}")
        save_to_json(processed_ranges, output_path)
        print("Processing completed successfully.")
    except (FileNotFoundError, ValueError, KeyError) as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
