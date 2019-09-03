from flask import Blueprint
from concept_innovator import conceptnet_adapter, amalgamation_adapter, extractor, specifier
from flask_api import status

bp = Blueprint('innovator', __name__, url_prefix='/innovator')

@bp.route('/<domain>', methods=['GET'])
def innovate_in(domain):

    random_concepts = conceptnet_adapter.find_two_random_types_of(domain)
    print(f'found concepts in {domain}-domain: "{random_concepts[0]["label"]}" and "{random_concepts[1]["label"]}"')

    blend = innovate_from(random_concepts[0], random_concepts[1])
    return blend, status.HTTP_204_NO_CONTENT


@bp.route('/boathouse', methods=['GET'])
def innovate_boathause():
    return innovate_from('boat', 'house')


def innovate_from(concept1, concept2):
    spec1 = get_specified_mental_space_for(concept1)
    spec2 = get_specified_mental_space_for(concept2)
    blend = amalgamation_adapter.blend_specs(spec1, spec2)
    return blend


def get_specified_mental_space_for(concept):
    if not conceptnet_adapter.concept_exists(concept):
        raise Exception(f'{concept} does not exist in ConceptNet')
    mental_space = extractor.extract_mental_space_for(concept)
    spec = specifier.specify_mental_space(mental_space)
    return spec