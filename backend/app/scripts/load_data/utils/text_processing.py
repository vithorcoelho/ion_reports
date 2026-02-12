"""Módulo com funções utilitárias para processamento e limpeza de texto.

Inclui funcionalidades para extrair valores numéricos, normalizar nomes
(slugify) e limpar strings de espaços extras ou caracteres indesejados.
"""

import re
import unicodedata


def clean_text(text: str) -> str | None:
    """Limpa uma string, removendo espaços múltiplos e quebras de linha.

    Args:
        text (str): O texto a ser limpo.

    Returns:
        Optional[str]: O texto limpo ou o valor original se não for uma string.

    """
    if isinstance(text, str):
        return re.sub(r"\s+", " ", text).strip()
    return text


def extract_numeric_value(text: str) -> float | None:
    """Extrai um valor numérico de uma string no formato 'Resultado: ...'.

    A função busca por um padrão específico, substitui vírgulas por pontos
    e converte o resultado para float.

    Args:
        text (str): A string da qual o valor será extraído.

    Returns:
        Optional[float]: O valor numérico extraído ou None se não for encontrado.

    """
    match = re.search(r"Resultado:\s*([0-9.,]+)", str(text))
    if match:
        value_str = match.group(1).replace(",", ".")
        try:
            return float(value_str)
        except ValueError:
            return None
    return None


def generate_slug(text: str) -> str:
    """Gera um 'slug' a partir de uma string, sem precisar de bibliotecas externas."""
    if not isinstance(text, str):
        text = str(text)
    text = (
        unicodedata.normalize("NFKD", text.lower())
        .encode("ascii", "ignore")
        .decode("ascii")
    )
    text = re.sub(r"[^a-z0-9-]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text


def parse_list_from_string(text: str) -> list[str]:
    """Extrai itens de uma string que representa uma lista (separada por ',', ';', ou quebra de linha)."""
    if not isinstance(text, str) or not text.strip():
        return []
    text = text.replace(";", ",").replace("\n", ",")
    items = [item.strip() for item in text.split(",") if item.strip()]
    return items


def remove_common_prefixes(text: str) -> str:
    """Remove prefixos comuns de textos de recomendações alimentares e suplementares."""
    if not isinstance(text, str):
        return text

    prefixes_to_remove = [
        r"^Alimentos recomendados:\s*",
        r"^Suplementos recomendados:\s*",
        r"^Recomendações:\s*",
        r"^Conduta:\s*",
    ]

    for prefix_pattern in prefixes_to_remove:
        text = re.sub(prefix_pattern, "", text, flags=re.IGNORECASE)

    return text.strip()
