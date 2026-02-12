"""Main module to load ontology data files into the Neo4j database when run as a module."""

import asyncio
import sys
from .main import main

if __name__ == "__main__":
    asyncio.run(main())
