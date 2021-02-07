from app import app
from .routes import world_routes


app.register_blueprint(world_routes)