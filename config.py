import os

_max_facts_per_relation = os.environ.get("MAX_FACTS_PER_RELATION")
MAX_FACTS_PER_RELATION = int(_max_facts_per_relation) if _max_facts_per_relation else None