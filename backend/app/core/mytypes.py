"""Custom type definitions for the IonNutri application.

This module contains type aliases and custom type definitions used throughout
the application, particularly for complex return types and data structures.
"""

# Define o alias de tipo para o retorno de _get_common_context
# 8 strings: altered_metabs, manifestations, interventions, foods,
# supplements, pathways, context_summary (add: medications_detailed_str)
CommonContext = tuple[str, str, str, str, str, str, str, str]
