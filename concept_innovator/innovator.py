from flask import Blueprint, request
import json

bp = Blueprint('innovator', __name__, url_prefix='/innovator')


@bp.route('/<domain>', methods=['GET'])
def innovate_in(domain):
    