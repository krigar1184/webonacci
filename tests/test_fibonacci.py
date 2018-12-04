import pytest
from fibonacci.service import generate_fibonacci_sequence


@pytest.mark.parametrize(('start', 'end', 'expected'), [
    (0, 1, [0, 1]),
    (3, 5, [2, 3, 5]),
    (0, 7, [0, 1, 1, 2, 3, 5, 8, 13])
])
def test_success(start, end, expected):
    assert generate_fibonacci_sequence(start, end) == expected

@pytest.mark.parametrize(('start', 'end'), [
    (1, 0),
    (5, 5),
    ('a', 'b'),
])
def test_wrong_input(start, end):
    with pytest.raises(AssertionError):
        generate_fibonacci_sequence(start, end)
