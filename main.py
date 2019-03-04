#!/usr/bin/env python3
from choremaster import create_app
from choremaster.config import config

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port="8888", debug=True)
