from flask import Flask
from flask_restplus import Api, Resource
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property


# Create the flask application.
app = Flask(__name__)
api = Api(app, version='1.0',
          title='Coronavirus tracker API',
          description='Get the last information about the COVID-19 in the worlds',
          license='MIT',
          contact='Mahdi Gueffaz')

# Import assets, models, routes, etc.
from .modules import France, World, US

# Run the application (server).
if __name__ == 'main':
    app.run()
    # app.run(port=PORT, threaded=True