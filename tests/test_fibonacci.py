import pytest
from fibonacci.app import f


@pytest.mark.parametrize(('start', 'end', 'expected'), [
    (0, 1, [0, 1]),
    (3, 5, [2, 3, 5]),
    (0, 7, [0, 1, 1, 2, 3, 5, 8, 13])
])
def test_f(start, end, expected):
    assert f(start, end) == expected
