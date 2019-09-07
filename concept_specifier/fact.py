import re
from flask import current_app as app


class InvalidFact(Exception):
    pass


class Fact(object):

    def __init__(self, edge):
        self.edge = edge
        if self.is_invalid:
            raise InvalidFact('Fact contains invalid languages', self.invalid_languages)

    @property
    def start(self):
        return self.__remove_id_prefix(self.edge['start']['term'])

    @property
    def relation(self):
        return self.edge['rel']['label']

    @property
    def end(self):
        return self.__remove_id_prefix(self.edge['end']['term'])

    @property
    def languages(self):
        languages = [self.edge['start']['language'], self.edge['end']['language']]
        # convert to set and back to list, to get unique values
        return list(set(languages))

    @property
    def invalid_languages(self):
        return [lang for lang in self.languages if lang not in self.valid_langauges()]

    @property
    def is_valid(self):
        return not self.invalid_languages

    @property
    def is_invalid(self):
        return not self.is_valid

    @classmethod
    def __remove_id_prefix(cls, term):
        id_prefix_regex = r'\/c\/.*?\/'
        return re.sub(id_prefix_regex, '', term)

    @classmethod
    def valid_langauges(cls):
        return app.config['VALID_FACT_LANGUAGES']
