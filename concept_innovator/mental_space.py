from concept_innovator import conceptnet_adapter
from concept_innovator.fact import Fact


class MentalSpace:

    def __init__(self, name, facts):
        self.name = name
        self.facts = facts

    @classmethod
    def extract_for_central_concept(cls, central_concept):
        all_edges = []
        for relation in conceptnet_adapter.RELATIONS:
            edges = conceptnet_adapter.find_edges_for(central_concept, relation)
            all_edges.extend(edges)
        facts = list(map(lambda edge: Fact.from_edge(edge), all_edges))
        return MentalSpace(central_concept, facts)

    @property
    def involved_concepts(self):
        start_concepts = list(map(lambda fact: fact.start, self.facts))
        end_concepts = list(map(lambda fact: fact.end, self.facts))

        start_concepts.extend(end_concepts)
        all_concepts = start_concepts

        # convert to set and back to list, to get unique values
        return list(set(all_concepts))
