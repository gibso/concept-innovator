import re

class MentalSpace:

    def __init__(self, name, facts):
        self.name = name
        self.facts = facts

    @property
    def involved_concepts(self):

        def remove_id_prefix(term):
            id_prefix_regex = r'\/c\/.*?\/'
            return re.sub(id_prefix_regex, '', term)

        start_concepts = list(map(lambda fact: remove_id_prefix(fact['start']['term']), self.facts))
        end_concepts = list(map(lambda fact: remove_id_prefix(fact['end']['term']), self.facts))

        start_concepts.extend(end_concepts)
        all_concepts = start_concepts

        # convert to set and back to list, to get unique values
        return list(set(all_concepts))