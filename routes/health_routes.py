from flask import Blueprint

import controllers

health = Blueprint('health', __name__)


@health.route('/health', methods=['GET'])
def get_health():
    return controllers.get_health()