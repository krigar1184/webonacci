#!/usr/local/bin/python

import os
from fibonacci.app import app


host = os.environ.get('FLASK_HOST')
port = os.environ.get('FLASK_PORT')

if __name__ == '__main__':
    app.run(host=host, port=port, load_dotenv=True)
