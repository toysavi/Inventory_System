from flask import Blueprint, jsonify
from .models import get_all_devices

api = Blueprint('api', __name__)

@api.route('/api/devices')
def api_devices():
    data = get_all_devices()
    return jsonify(data)
