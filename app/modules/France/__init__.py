from app import app
from .routes import france_routes


app.register_blueprint(france_routes)