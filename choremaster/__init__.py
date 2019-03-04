#!/usr/bin/env python3
"""Flask factory."""
import os

from flask import Flask

from .ChoreLogger import LoggerAPI
from .StatsAPI import StatsAPI

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
    stat_view = StatsAPI.as_view('stats')
    app.add_url_rule('/chores/', view_func=log_view, methods=['GET'])
    app.add_url_rule('/chores/<int:_id>', view_func=log_view, methods=['POST'])

    app.add_url_rule(
        "/chores/<int:_id>/stats/<int:year>/", view_func=stat_view, methods=['GET']
    )

    return app
