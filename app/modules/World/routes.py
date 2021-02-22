from flask import Flask, Blueprint
from flask_restplus import Api, Namespace, Resource
from app import api
from .services import get_all_data_panda, get_all_data_by_category_panda, get_information_country


world_routes = Blueprint('world', __name__, url_prefix='/world')
world_routes_api = api.namespace('World', description = "JHU resource")


@world_routes_api.route("/")
class List(Resource):
    def get(self):
        """
        returns all data of the countries
        """
        return get_all_data_panda()

@world_routes_api.route("/recovered/<country_code>")
class RecoveredList(Resource):
    def get(self, country_code):
        """
        returns the recovered history of a country
        """
        return get_all_data_by_category_panda('recovered', country_code)


@world_routes_api.route("/death/<country_code>")
class DeathList(Resource):
    def get(self, country_code):
        """
        returns the death history of a country
        """
        return get_all_data_by_category_panda('deaths', country_code)


@world_routes_api.route("/confirmed/<country_code>")
class ConfirmedList(Resource):
    def get(self, country_code):
        """
        returns the confirmed history of a country
        """
        return get_all_data_by_category_panda('confirmed', country_code)


@world_routes_api.route("/informations/")
class InformationList(Resource):
    def get(self):
        """
        returns a list of books
        """
        return get_information_country()
