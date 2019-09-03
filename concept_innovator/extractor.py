from concept_innovator import conceptnet_adapter
from concept_innovator.mental_space import MentalSpace


def extract_mental_space_for(central_concept):
    print(f'start collecting facts for concept: "{central_concept}')
    mental_space_facts = []
    for relation in conceptnet_adapter.RELATIONS:
        print(f'get facts with relation "{relation}"')
        related_facts = conceptnet_adapter.find_facts_for(central_concept, relation)
        mental_space_facts.extend(related_facts)
    return MentalSpace(central_concept, mental_space_facts)
