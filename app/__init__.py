import os
from flask import Flask
from .db import get_db_connection

def create_app():
    app = Flask(__name__)
    
    # Set the upload folder
    app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path, 'uploaded_pdfs')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    with app.app_context():
        get_db_connection()  # Initialize the database

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
