from flask import Flask


# Create the flask application.
app = Flask(__name__)

# Import assets, models, routes, etc.
from .modules import France, World

# Run the application (server).
if __name__ == 'main':
    app.run()
    # app.run(port=PORT, threaded=True)