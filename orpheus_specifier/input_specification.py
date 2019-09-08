from orpheus_specifier.mental_space import MentalSpace


class InputSpecification(MentalSpace):

    def __init__(self, concepts):
        super().__init__('-'.join(concepts))
        mental_spaces = []
        for concept in concepts:
            mental_spaces.append(MentalSpace(concept))
        self.mental_spaces = mental_spaces

    @property
    def facts(self):
        all_facts = []
        for mental_space in self.mental_spaces:
            all_facts.extend(mental_space.facts)
        return all_facts

    @property
    def local_spec(self):
        spec = ''
        for mental_space in self.mental_spaces:
            spec += mental_space.local_spec + '\n'
        return spec[:-1]
