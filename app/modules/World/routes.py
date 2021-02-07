from flask import Flask, Blueprint
from flask_restplus import Api, Namespace, Resource
from app import api


world_routes = Blueprint('world', __name__, url_prefix='/world')
ns_books = api.namespace('World', description = "Books operations")


@ns_books.route("/recovered/")
class RecoveredList(Resource):
    def get(self):
        """
        returns a list of books
        """
        return {"response": 'test data'}

@ns_books.route("/death/")
class DeathList(Resource):
    def get(self):
        """
        returns a list of books
        """
        return {"response": 'test data'}
    

@world_routes.route('/recovered')
def world_recovered():
    """
    Get the recovered case in the world
    """
    return 'hello world'


@world_routes.route('/death')
def world_death():
    """
    Get the recovered case in the world
    """
    return 'hello world'


@world_routes.route('/confirmed')
def world_confirmed():
    """
    Get the recovered case in the world
    """
    return 'hello world'

@world_routes.route('/active')
def word_active():
    """
    Get the recovered case in the world
    """
    return 'hello world'