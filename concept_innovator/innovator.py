from flask import Blueprint, request
import json
from concept_innovator import conceptnet_adapter, parser, blender, writer

bp = Blueprint('innovator', __name__, url_prefix='/innovator')


@bp.route('/<domain>', methods=['GET'])
def innovate_in(domain):
    domain_type_concepts = conceptnet_adapter.find_two_random_types_of(domain)
    casl_spec = parser.create_casl_for_concepts(domain_type_concepts, domain)
    innovation_spec = blender.create_blending_for(casl_spec)
    innovation = writer.describe_spec(innovation_spec)
    return bp.response_class(
        response=json.dumps(innovation),
        status=200,
        mimetype='application/json'
    )