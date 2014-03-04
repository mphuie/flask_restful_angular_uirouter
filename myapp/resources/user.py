from myapp import db
from myapp.models import *
from flask.ext.restful import Api, Resource, reqparse
from flask import request

class UserAPI(Resource):
    def get(self, id):
        u = User.query.get(id)
        if u:
            return { 'name': u.name }
        else:
            return { 'description': 'ID does not exist' }, 404

    def put(self, id):
        pass

    def delete(self, id):
        pass

class UserListAPI(Resource):


    def get(self):
        all_users = []
        users = User.query.all()
        for u in users:
            all_users.append({'name': u.name})
        return all_users

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        args = parser.parse_args()
        u = User()
        u.name = args['name']
        db.session.add(u)
        db.session.commit()


        return { 'name': u.name }