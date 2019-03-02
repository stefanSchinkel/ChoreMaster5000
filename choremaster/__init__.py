#!/usr/bin/env python3
"""Flask factory."""

from flask import Flask

from .ChoreLogger import LoggerAPI

def create_app(config):
    """Flask app factory."""
    app = Flask(__name__)
    app.config["DB"] = config["database"]

    log_view = LoggerAPI.as_view('chores')

    app.add_url_rule('/chores/', view_func=log_view, methods=['GET'])
    app.add_url_rule('/chores/<int:chore_id>', view_func=log_view,
        methods=['POST'])

    return app