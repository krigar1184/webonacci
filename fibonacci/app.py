import json
from flask import Flask
from .service import generate_fibonacci_sequence


app = Flask(__name__)


@app.route('/health')
def health_check():
    return json.dumps({'status': 'OK'})


@app.route('/fib/<int:start_idx>/<int:end_idx>')
def fib(start_idx, end_idx):
    return json.dumps({'result': generate_fibonacci_sequence(start_idx, end_idx)})
