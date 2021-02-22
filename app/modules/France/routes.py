from flask import Flask, Blueprint
from flask_restplus import Api, Namespace, Resource
from app import api
from .test import Request_data_vaccination
import json
from .services import get_data


france_routes = Blueprint('france', __name__, url_prefix='/france')
france_routes_api = api.namespace('France', description = "France operations")


@france_routes_api.route("/recovered/")
class RecoveredList(Resource):
    def get(self):
        """
        returns a list of books
        """
        return get_data()


@france_routes_api.route("/death/")
class DeathList(Resource):
    def get(self):
        """
        returns a list of books
        """
        return {"response": 'test data'}


@france_routes_api.route("/confirmed/")
class ConfirmedList(Resource):
    def get(self):
        """
        returns a list of books+
         
        """
        return {"response": 'test data'}


@france_routes_api.route("/vaccination")
class vaccinationList(Resource):
    def get(self):
        """
        """
        return {"response": 'test data'}


@france_routes_api.route("/depistage")
class DepistageList(Resource):
    def get(self):
        """
        """
        return {"response": 'test data'}