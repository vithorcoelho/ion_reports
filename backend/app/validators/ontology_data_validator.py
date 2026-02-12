"""Validator for ontology data integrity and structure.

This module provides validation functionality for ontology data structures,
ensuring data integrity, uniqueness constraints, and proper formatting before
loading into knowledge graphs.
"""

from typing import Any


class OntologyDataValidator:
    """Validates ontology data represented as a dictionary where each key is an entity type and the value is a list of entities.

    The validator ensures:
      - Each entity type's value is a list.
      - Each entity in the list contains a unique 'id' field.
      - No duplicate IDs exist within the same entity type.

    It also includes a helper method to check if a given reference ID exists anywhere in the ontology data.
    """

    def __init__(self, data: dict[str, Any]):
        """Initializes the validator with the provided data."""
        self.data = data
        self.errors: list[str] = []

    def validate(self) -> tuple[bool, list[str]]:
        """Validates ontology data, ensuring that each entity type is a list, each entity has an 'id' field,
        and there are no duplicate IDs within the same entity type.
        """
        for entity_type, entities in self.data.items():
            if not isinstance(entities, list):
                self.errors.append(f"'{entity_type}' must be a list.")
                continue

            seen_ids = set()
            for i, entity in enumerate(entities):
                entity_id = entity.get("id")
                if not entity_id:
                    self.errors.append(f"{entity_type}[{i}] is missing 'id'.")
                elif entity_id in seen_ids:
                    self.errors.append(
                        f"Duplicated ID '{entity_id}' in '{entity_type}'."
                    )
                else:
                    seen_ids.add(entity_id)

        return len(self.errors) == 0, self.errors

    def _exists(self, ref_id: str, target_entity_type: str) -> bool:
        """Checks if there is any entity with the given reference ID in any entity type in the data.
        Returns True if the ID is found, otherwise False.
        """
        for entities in self.data.values():
            if isinstance(entities, list):
                if any(e.get("id") == ref_id for e in entities):
                    return True
        return False
