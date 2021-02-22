from app import app
from .routes import us_routes


app.register_blueprint(us_routes)