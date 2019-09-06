from concept_innovator import conceptnet_adapter
from concept_innovator.fact import Fact
import functools
import tempfile


class MentalSpace(object):

    def __init__(self, name):
        self.name = name

    @property
    @functools.lru_cache()
    def facts(self):
        all_edges = []
        for relation in conceptnet_adapter.RELATIONS:
            edges = conceptnet_adapter.find_edges_for(self.name, relation)
            all_edges.extend(edges)
        facts = list(map(lambda edge: Fact.from_edge(edge), all_edges))
        return facts

    @property
    def involved_concepts(self):
        start_concepts = list(map(lambda fact: fact.start, self.facts))
        end_concepts = list(map(lambda fact: fact.end, self.facts))

        start_concepts.extend(end_concepts)
        all_concepts = start_concepts

        # convert to set and back to list, to get unique values
        return list(set(all_concepts))

    @property
    def global_spec(self):
        spec = f'spec Global = \n    generated type Concept ::='
        for concept in self.involved_concepts:
            spec += f' {concept} |'
        spec = spec[:-2] + '\n    preds\n'
        for relation in conceptnet_adapter.RELATIONS:
            spec += f'        {relation} : Concept * Concept\n'
        spec += 'end\n'
        return spec

    @property
    def local_spec(self):
        spec = f'spec {self.name.capitalize()} = Global then\n    ops\n'
        for concept in self.involved_concepts:
            spec += f'        {concept} : Concept\n'
        for fact in self.facts:
            spec += f'    . {fact.relation}({fact.start},{fact.end})\n'
        spec += 'end\n'
        return spec

    @property
    def spec(self):
        return f'{self.global_spec}\n{self.local_spec}'

    @property
    def casl_file(self):
        casl_file = tempfile.NamedTemporaryFile(suffix=f'-{self.name}.casl')
        casl_file.write(self.spec.encode())
        return casl_file
