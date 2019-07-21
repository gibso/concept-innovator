import requests
import random

def find(id):
    return requests.get(f'http://api.conceptnet.io/{id}').json()


def find_two_random_types_of(concept):
    concept_types = requests.get(f'http://api.conceptnet.io/query?end=/c/en/{concept}&rel=/r/IsA').json()
    results_count = len(concept_types['edges'])
    random_indexes = []
    for i in range(2):
        random_indexes.append(random.randrange(0, results_count))
    type_concept_nodes = list(map(lambda i: concept_types['edges'][i]['start'], random_indexes))
    return list(map(lambda node: find(node['term']), type_concept_nodes))

