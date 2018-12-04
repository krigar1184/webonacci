from .utils import local_cache


@local_cache
def nth_fibonacci_number(n):  # TODO more efficient algorithm needed
    if n == 0:
        return 0

    if n == 1:
        return 1

    return nth_fibonacci_number(n - 1) + nth_fibonacci_number(n - 2)


def generate_fibonacci_sequence(start: int, end: int) -> list:
    assert isinstance(start, int), 'start should be integer'
    assert isinstance(end, int), 'end should be integer'
    assert start >= 0, 'start should be less than or equal to zero'
    assert start < end, 'start index should be less than end index'

    start_value = nth_fibonacci_number(start)
    next_value = nth_fibonacci_number(start + 1)
    counter = end - start
    result = [start_value, next_value]

    while counter > 1:
        tmp = start_value
        start_value = next_value
        next_value = tmp + next_value

        result.append(next_value)
        counter -= 1

    return result
