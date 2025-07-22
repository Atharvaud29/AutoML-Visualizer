# app/__init__.py

from flask import Flask
from app.blueprints.preprocessing.routes import preprocessing_bp
from app.blueprints.ml.routes import ml_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = "your-secret-key"  # You can load from config later

    # Register blueprints
    app.register_blueprint(preprocessing_bp, url_prefix="/preprocessing")
    app.register_blueprint(ml_bp, url_prefix="/ml")

    return app
