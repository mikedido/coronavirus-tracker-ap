from flask import Flask, Blueprint


france_routes = Blueprint('france', __name__, url_prefix='/france')

@france_routes.route('/recovered')
def france_recovered():
    """
    Get the recovered by country
    """
    return 'hello world'