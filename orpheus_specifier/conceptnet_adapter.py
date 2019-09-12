from flask import current_app as app
import http.client
import json
from urllib.parse import urlencode


class ConceptnetAdapter:

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

    @property
    def connection(self):
        return http.client.HTTPConnection(app.config['CONCEPTNET_HOST'])

    @classmethod
    def find_all_related_edges_for(cls, concept):
        all_edges = []
        max_edges_per_relation = app.config['MAX_FACTS_PER_RELATION']
        for relation in cls.RELATIONS:
            edges = cls.find_edges_for(concept, relation)
            edges = edges[0:max_edges_per_relation] if max_edges_per_relation else edges
            all_edges.extend(edges)
        return all_edges

    @classmethod
    def find_edges_for(cls, concept, relation):
        concept = concept.lower()
        print(f'get "{relation}"-relations for "{concept}"-node')
        response = cls.__query({
            'start': f'/c/en/{concept}',
            'rel': f'/r/{relation}'
        })
        return response['edges']

    @classmethod
    def __query(cls, query_params):
        url = '/query?' + urlencode(query_params)
        return cls.__perform_request(url)

    @classmethod
    def __perform_request(cls, url):
        conn = cls().connection
        conn.request('GET', url)
        response = conn.getresponse()
        if response.status != 200:
            raise Exception(response.reason, response.status)
        json_str = response.read().decode('utf-8')
        return json.loads(json_str)
