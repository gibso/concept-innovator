import requests
import random

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


def find_related_nodes_for(node, relation):
    print(f'get "{relation}"-relations for "{node["term"]}"-node')
    relations_to_node = requests.get(f'http://api.conceptnet.io/query?start={node["term"]}&rel={relation}').json()
    return list(map(lambda edge: edge['end'], relations_to_node['edges']))

