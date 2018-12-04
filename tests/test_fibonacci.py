import os
import json
import requests
from unittest import mock
import pytest
from fibonacci.service import generate_fibonacci_sequence, check_redis_health


@pytest.mark.parametrize(('start', 'end', 'expected'), [
    (0, 1, [0, 1]),
    (3, 5, [2, 3, 5]),
    (0, 7, [0, 1, 1, 2, 3, 5, 8, 13])
])
def test_sequence_generation_success(start, end, expected):
    assert generate_fibonacci_sequence(start, end) == expected

@pytest.mark.parametrize(('start', 'end'), [
    (1, 0),
    (5, 5),
    ('a', 'b'),
])
def test_sequence_generation_fail(start, end):
    with pytest.raises(AssertionError):
        generate_fibonacci_sequence(start, end)


def test_check_health_success():
    app_host = os.environ.get('FLASK_HOST')
    app_port = os.environ.get('FLASK_PORT')

    response = requests.get(f'http://{app_host}:{app_port}/health')
    assert response.status_code == 200

    data = json.loads(response.content)
    assert data['redis']['is_healthy'] is True

#
#def test_check_health_fail():
#    app_host = 'nonexisting.local'
#    app_port = os.environ.get('FLASK_PORT')
#    response = requests.get(f'http://{app_host}:{app_port}/health')
#    assert response.status_code == 200
