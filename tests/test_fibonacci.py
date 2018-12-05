import os
import requests
import pytest
from mockredis import mock_redis_client
from fibonacci.service import generate_fibonacci_sequence, check_redis_health


@pytest.fixture
def is_healthy(request):
    return request.param


@pytest.fixture
def redis_store_mock(request, is_healthy):
    client = mock_redis_client()
    client.ping = lambda: is_healthy

    return client


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


@pytest.mark.parametrize('is_healthy', [True, False], indirect=['is_healthy'])
def test_check_health_success(redis_store_mock, is_healthy):
    assert check_redis_health(redis_store_mock)['is_healthy'] is is_healthy
