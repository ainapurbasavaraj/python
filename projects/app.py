from flask import flask
from flask_restful import Resource, Api

app = flask(__name__)

api = Api(app)

class Student(Resource):
    def get(self,name):
        return {'student' : name}