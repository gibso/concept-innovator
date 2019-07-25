from flask import Blueprint
from concept_innovator import conceptnet_adapter, parser, blender, writer
from flask_api import status

bp = Blueprint('innovator', __name__, url_prefix='/innovator')


@bp.route('/<domain>', methods=['GET'])
def innovate_in(domain):
    input_space_nodes = conceptnet_adapter.find_two_random_types_of(domain)
    print(f'found concepts in {domain}-domain: "{input_space_nodes[0]["label"]}" and "{input_space_nodes[1]["label"]}"')
    casl_spec = parser.create_casl_for_input_spaces(input_space_nodes, domain)
    innovation_spec = blender.create_blending_for(casl_spec)
    innovation = writer.describe_spec(innovation_spec)
    return '', status.HTTP_204_NO_CONTENT
