from orpheus_specifier.conceptnet_adapter import ConceptnetAdapter
from orpheus_specifier.fact import Fact, InvalidFact
import functools
import tempfile


class MentalSpace(object):

    def __init__(self, name):
        self.name = name

    @property
    @functools.lru_cache()
    def facts(self):
        facts = []
        related_edges = ConceptnetAdapter.find_all_related_edges_for(self.name)
        for edge in related_edges:
            try:
                facts.append(Fact(edge))
            except InvalidFact as error:
                print(error)
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
        for relation in ConceptnetAdapter.RELATIONS:
            spec += f'        {relation} : Concept * Concept\n'
        spec += 'end\n'
        return spec

    @property
    def local_spec(self):
        spec = f'spec {self.name.capitalize()} = Global then\n    ops\n'
        for concept in self.involved_concepts:
            spec += f'        {concept} : Concept\n'
        for index, fact in enumerate(self.facts):
            spec += f'    . {fact.relation}({fact.start},{fact.end})  %(Ax-{fact.relation}{index}:p:{fact.priority})% \n'
        spec += 'end\n'
        return spec

    @property
    def spec(self):
        return f'{self.global_spec}\n{self.local_spec}'

    @property
    def casl_file(self):
        casl_file = tempfile.NamedTemporaryFile(suffix=f'-{self.name}.casl', delete=False)
        casl_file.write(self.spec.encode())
        casl_file.close()
        return casl_file
