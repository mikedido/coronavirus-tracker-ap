import json
from app import api
from flask import Flask, Blueprint
from flask_restplus import Api, Namespace, Resource
from .services import get_all_data, get_all_data_by_category


us_routes = Blueprint('US', __name__, url_prefix='/US')
us_routes_api = api.namespace('US', description = "United Statess operations")


@us_routes_api.route("/")
class List(Resource):
    def get(self):
        """
        returns a list of books
        """
        return json.loads(get_all_data())


@us_routes_api.route("/confirmed/<province_name>")
class RecoveredList(Resource):
    def get(self, province_name):
        """
        returns a list of books
        """
        return json.loads(get_all_data_by_category('confirmed', province_name))


@us_routes_api.route("/death/<province_name>")
class DeathList(Resource):
    def get(self, province_name):
        """
        returns a list of books
        """
        return json.loads(get_all_data_by_category('deaths', province_name))