"""Define typed dictionaries for reference ranges and metabolites."""

from typing import TypedDict


class ReferenceRange(TypedDict):
    """Represent a reference range with minimum, maximum and unit values."""

    min: float | None
    max: float | None
    unit: str


class Metabolite(TypedDict):
    """Represent a metabolite with its name and associated ranges."""

    name: str
    ranges: list[str]
