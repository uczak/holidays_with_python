import os
from os import environ

from flask import Flask, redirect
from flask_cors import CORS, cross_origin
from flask_restx import Api

from services.holidays.controller import request_holiday_namespace

#from services.repository.connection import Connection_api

# Application basic settings.
__app_title__ = "Services"
__app_description__ = 'Services API.'
__app_secret_key__ = b'\x9b\x89\xe61x|\x9e\xf4\x0b[\x0e\xa8\xd0\xa2o6F\xd4@\x15\x11\xfe\x9f\xd7'
__version_tag__ = environ.get('API_VERSION', '1.0')


# Creates the flask application and the flask_restplus api
app = Flask(__name__)
app.config['ERROR_404_HELP'] = False
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = __app_secret_key__


api = Api(app, version=__version_tag__, title=__app_title__,
          description=__app_description__)
CORS(app)

# Register apis.
api.add_namespace(request_holiday_namespace)


@app.route('/swagger')
def redirect_home():
    return redirect('/')


@app.route('/healthcheck')
@cross_origin()
def testando():
    return 'On-line', 200  # Active().get_active()
