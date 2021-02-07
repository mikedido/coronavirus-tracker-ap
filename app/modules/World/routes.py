from flask import Flask, Blueprint


world_routes = Blueprint('world', __name__, url_prefix='/world')

@world_routes.route('/recovered')
def word_recovered():
    """
    Get the recovered by country
    """
    return 'hello world'