from flask import Blueprint, send_file, request
from concept_specifier.input_specification import InputSpecification
from concept_specifier.mental_space import MentalSpace
import json

bp = Blueprint('specifier', __name__, url_prefix='/specify')


@bp.route('/<concept>', methods=['GET'])
def specify_concept(concept):
    casl_file = MentalSpace(concept).casl_file
    return send_file(casl_file.name, as_attachment=True, mimetype='text/plain')


@bp.route('/input-spaces', methods=['POST'])
def specify_input_spaces():
    input_space_names = json.loads(request.data)['input-space-names']
    casl_file = InputSpecification(input_space_names).casl_file
    return send_file(casl_file.name, as_attachment=True, mimetype='text/plain')


# bp = Blueprint('specifier', __name__, url_prefix='/specifier')
#
# @bp.route('/<domain>', methods=['GET'])
# def innovate_in(domain):
#
#     random_concepts = conceptnet_adapter.find_two_random_types_of(domain)
#     print(f'found concepts in {domain}-domain: "{random_concepts[0]["label"]}" and "{random_concepts[1]["label"]}"')
#
#     blend = innovate_from(random_concepts[0], random_concepts[1])
#     return blend, status.HTTP_204_NO_CONTENT
#
#
# @bp.route('/boathouse', methods=['GET'])
# def innovate_boathause():
#     return innovate_from('boat', 'house')
#
#
#
#
# def innovate_from(concept1, concept2):
#     spec1 = get_specified_mental_space_for(concept1)
#     spec2 = get_specified_mental_space_for(concept2)
#     blend = amalgamation_adapter.blend_specs(spec1, spec2)
#     return blend
#
#
# def get_specified_mental_space_for(concept):
#     if not conceptnet_adapter.concept_exists(concept):
#         raise Exception(f'{concept} does not exist in ConceptNet')
#     spec = Specification.from_central_concept(concept)
#     return spec