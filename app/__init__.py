# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from importlib import import_module
from logging import basicConfig, DEBUG, getLogger, StreamHandler
from os import path

# Integrate custom commands
from .commands import commands

db = SQLAlchemy()
login_manager = LoginManager()

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)

def register_blueprints(app):
    for module_name in ('base', 'home'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def configure_database(app):

    @app.before_first_request
    @with_appcontext
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def configure_commands(app):
    app.register_blueprint(commands)

def create_app(config):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)

    # Define the custom commands
    configure_commands(app)

    # App is fully constructed
    return app
