"""wsgi.py
Just a wrapper for the wsgi handler
"""

from choremaster import create_app

app = create_app()
