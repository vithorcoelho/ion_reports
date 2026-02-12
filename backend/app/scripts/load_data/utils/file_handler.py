"""Utility module for file handling.

Provides functions to read data from different formats (CSV, Excel) and
to save structured data in JSON format.
"""

import json
import logging
import os
from typing import Any

import pandas as pd

logger = logging.getLogger(__name__)


def read_data_file(path: str) -> pd.DataFrame:
    """Read a CSV or Excel file and return a pandas DataFrame.

    The first line of the file is used as the column header.
    """
    if not os.path.exists(path):
        logger.error(f"File not found at: {path}")
        raise FileNotFoundError(f"File not found at: {path}")

    extension = os.path.splitext(path)[1].lower()
    if extension == ".csv":
        # Uses "utf-8-sig" encoding to avoid BOM issues
        df_raw = pd.read_csv(path, encoding="utf-8-sig")
    elif extension in [".xlsx", ".xls"]:
        df_raw = pd.read_excel(path)
    else:
        logger.error("Unsupported file format. Use CSV, XLSX, or XLS.")
        raise ValueError("Unsupported file format. Use CSV, XLSX, or XLS.")

    df_raw.columns = df_raw.columns.str.strip()
    return df_raw


def save_to_json(data: list[dict[str, Any]], output_path: str) -> None:
    """Save a list of dictionaries to a JSON file with readable formatting.

    Recursively replaces NaN or None values with 'sem informação' before saving.
    """

    def replace_nan_with_text(obj: Any) -> Any:
        """Recursively replaces NaN or None values in objects with 'sem informação'."""
        if isinstance(obj, float) and pd.isna(obj):
            return "sem informação"
        if isinstance(obj, dict):
            return {k: replace_nan_with_text(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [replace_nan_with_text(i) for i in obj]
        return obj

    cleaned_data = replace_nan_with_text(data)
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(cleaned_data, f, ensure_ascii=False, indent=2)
        logger.info(f"Data successfully saved to '{output_path}'")
    except Exception as e:
        logger.error(f"Error saving data to JSON: {e}")
