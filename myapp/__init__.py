from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api, reqparse

app = Flask(__name__)
api = Api(app)

app.config.from_object('config')

db = SQLAlchemy(app)

from myapp.views import aview

from myapp.resources.user import UserAPI, UserListAPI

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, location='json')

api.add_resource(UserAPI, '/users/<int:id>')
api.add_resource(UserListAPI, '/users')

