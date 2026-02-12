"""Utility functions and classes for prompt handling.

This module provides utilities for safe text encoding, joining lists of items,
and configuration dataclasses for prompt management across different plugins.
"""

from dataclasses import dataclass
from typing import Any

from app.core.logging import logger


@dataclass
class PromptConfig:
    """Configuration class for prompt generation.

    Attributes:
        context_sections (list[str]): Sections to include in the prompt context.
        objective (str): The objective description for the prompt.
        additional_context (dict[str, Any] | None): Additional context data.
        system_prompt (str | None): Custom system prompt override.

    """

    context_sections: list[str]
    objective: str
    additional_context: dict[str, Any] | None = None
    system_prompt: str | None = None


def safe_encode(text: str) -> str:
    """Ensure text is properly UTF-8 encoded and remove problematic characters.

    Args:
        text (str): The text to encode safely.

    Returns:
        str: UTF-8 encoded text with problematic characters removed.

    """
    if not text:
        return ""
    try:
        return text.encode("utf-8", errors="ignore").decode("utf-8")
    except Exception as e:
        logger.warning(f"Error encoding text: {str(e)}")
        return str(text)


def safe_join(items: list) -> str:
    """Join list items into a string with safe encoding handling.

    Args:
        items (list): List of items to join.

    Returns:
        str: Joined string with newline separators.

    """
    safe_items = []
    for item in items:
        try:
            safe_item = safe_encode(str(item))
            safe_items.append(safe_item)
        except Exception as e:
            logger.warning(f"Error processing item: {str(e)}")
            continue
    return "\n".join(safe_items)
