import re


class Fact:

    def __init__(self, start, relation, end):
        self.start = start
        self.relation = relation
        self.end = end

    @classmethod
    def from_edge(cls, edge):
        start = cls.__remove_id_prefix(edge['start']['term'])
        relation = edge['rel']['label']
        end = cls.__remove_id_prefix(edge['end']['term'])
        return cls(start, relation, end)

    def __remove_id_prefix(term):
        id_prefix_regex = r'\/c\/.*?\/'
        return re.sub(id_prefix_regex, '', term)