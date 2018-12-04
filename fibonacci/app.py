import json
from flask import Flask
from .service import generate_fibonacci_sequence, check_redis_health


app = Flask(__name__)


@app.route('/health')
def health_check():
    try:
        redis_state = check_redis_health()
    except Exception as e:
        redis_state = {
            'redis': {
                'is_healthy': False,
                'error_info': str(e),
            }
        }

    return json.dumps(redis_state)


@app.route('/fib/<int:start_idx>/<int:end_idx>')
def fib(start_idx, end_idx):
    return json.dumps({'result': generate_fibonacci_sequence(start_idx, end_idx)})
