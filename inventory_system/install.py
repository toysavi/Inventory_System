from flask import Flask
from config import *
from app.routes import routes
from app.api import api
from app.models import mysql

app = Flask(__name__)
app.config.from_object('config')
mysql.init_app(app)

app.register_blueprint(routes)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)
