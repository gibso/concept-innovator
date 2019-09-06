from flask import Blueprint, send_file, request
from concept_specifier.input_specification import InputSpecification
from concept_specifier.mental_space import MentalSpace
import json

bp = Blueprint('specifier', __name__, url_prefix='/specify')


@bp.route('/concept', methods=['POST'])
def specify_concept():
    concept_name = json.loads(request.data)['concept-name']
    mental_space = MentalSpace(concept_name)
    spec_file_name = mental_space.casl_file.name
    return send_file(spec_file_name, as_attachment=True, mimetype='text/plain')


@bp.route('/input-spaces', methods=['POST'])
def specify_input_spaces():
    input_space_names = json.loads(request.data)['input-space-names']
    spec = InputSpecification(input_space_names)
    spec_file_name = spec.casl_file.name
    return send_file(spec_file_name, as_attachment=True, mimetype='text/plain')