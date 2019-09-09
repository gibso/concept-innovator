import requests
from flask import current_app as app

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
    'MadeOf'
    'ReceivesAction',
    # 'ExternalURL'
]


def find_edges_for(concept, relation):
    concept = concept.lower()
    print(f'get "{relation}"-relations for "{concept}"-node')
    response = requests.get(f'http://api.conceptnet.io/query?start=/c/en/{concept}&rel=/r/{relation}')
    return response.json()['edges']


def find_all_related_edges_for(concept):
    all_edges = []
    max_edges_per_relation = app.config['MAX_FACTS_PER_RELATION']
    for relation in RELATIONS:
        edges = find_edges_for(concept, relation)
        edges = edges[0:max_edges_per_relation] if max_edges_per_relation else edges
        all_edges.extend(edges)
    return all_edges
