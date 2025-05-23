from flask import Blueprint, render_template
from .models import get_all_devices

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    devices = get_all_devices()
    return render_template("index.html", devices=devices)
