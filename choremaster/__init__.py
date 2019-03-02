#!/usr/bin/env python3
"""Flask factory."""
import os

from flask import Flask

from .ChoreLogger import LoggerAPI

def create_app():
    """Flask app factory."""
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'chores.sqlite'),
    )
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # DB access
    from . import db
    db.init_app(app)

    # hookup endpoints
    log_view = LoggerAPI.as_view('chores')

    app.add_url_rule('/chores/', view_func=log_view, methods=['GET'])
    app.add_url_rule('/chores/<int:id>', view_func=log_view,methods=['POST'])

    return app