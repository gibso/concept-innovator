import os

_max_facts_per_relation = os.environ.get('MAX_FACTS_PER_RELATION')
MAX_FACTS_PER_RELATION = int(_max_facts_per_relation) if _max_facts_per_relation else None

_valid_fact_languages = os.environ.get('VALID_FACT_LANGUAGES')
VALID_FACT_LANGUAGES = _valid_fact_languages.split(',') if _valid_fact_languages else ['de', 'en']

CONCEPTNET_HOST = os.environ.get('CONCEPTNET_HOST')
if not CONCEPTNET_HOST:
    raise Exception('Please specify env variable CONCEPTNET_HOST')
