# app/blueprints/ml/routes.py

from flask import Blueprint

ml_bp = Blueprint('ml', __name__)

@ml_bp.route('/')
def ml_home():
    return "ML route is working!"
