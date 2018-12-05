from flask import json
from flask import Flask

from .service import generate_fibonacci_sequence, check_redis_health
from .utils import caches


app = Flask(__name__)


@app.route('/health')
def health_check():
    try:
        redis_state = check_redis_health(caches['redis'])
    except Exception as e:
        status_code = 500
        redis_state = {
            'is_healthy': False,
            'error_info': str(e),
        }
    else:
        status_code = 200

    return json.dumps({'redis': redis_state}), status_code


@app.route('/fib/<int:start_idx>/<int:end_idx>')
def fib(start_idx, end_idx):
    return json.dumps({'result': generate_fibonacci_sequence(start_idx, end_idx)})
