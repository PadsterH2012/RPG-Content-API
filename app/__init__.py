from flask import Flask
from .db import get_db_connection

def create_app():
    app = Flask(__name__)

    with app.app_context():
        get_db_connection()  # Initialize the database

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
