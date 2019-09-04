import requests
import random

RELATIONS = [
    'RelatedTo',
    'FormOf',
    'IsA',
    'PartOf',
    'HasA',
    'UsedFor',
    'CapableOf',
    'AtLocation',
    'Causes',
    'HasSubevent',
    'HasFirstSubevent',
    'HasLastSubevent',
    'HasPrerequisite',
    'HasProperty',
    'MotivatedByGoal',
    'ObstructedBy',
    'Desires',
    'CreatedBy',
    'Synonym',
    'Antonym',
    'DistinctFrom',
    'DerivedFrom',
    'SymbolOf',
    'DefinedAs',
    'MannerOf',
    'LocatedNear',
    'HasContext',
    'SimilarTo',
    'EtymologicallyRelatedTo',
    'EtymologicallyDerivedFrom',
    'CausesDesire',
    'MadeOf',
    'ReceivesAction',
    'ExternalURL'
]


class Node:
    @classmethod
    def find(self, id):
        return requests.get(f'http://api.conceptnet.io/{id}').json()

    @classmethod
    def find_by_label(cls, label):
        return requests.get(f'http://api.conceptnet.io/c/en/{label}').json()


def find_two_random_types_of(label):
    node = Node.find_by_label(label)

    concept_types = requests.get(f'http://api.conceptnet.io/query?end={node["@id"]}&rel=/r/IsA').json()
    results_count = len(concept_types['edges'])
    random_indexes = []
    for i in range(2):
        random_indexes.append(random.randrange(0, results_count))
    return list(map(lambda i: concept_types['edges'][i]['start'], random_indexes))


def find_edges_for(concept, relation):
    print(f'get "{relation}"-relations for "{concept}"-node')
    relations_to_node = requests.get(f'http://api.conceptnet.io/query?start=/c/en/{concept}&rel=/r/{relation}').json()
    return relations_to_node['edges']


def concept_exists(concept):
    return Node.find_by_label(concept)
