from flask import Flask, Blueprint
from flask_restful import Api

from app.api.v1.views import Products


def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)

    
    app.config.from_mapping(
        SECRET_KEY='Mesh'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    from .api.v1 import v1
    app.register_blueprint(v1)
            
    return app