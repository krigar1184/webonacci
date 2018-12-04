from flask import Flask


app = Flask(__name__)


def nth_fibonacci_number(n):  # TODO more efficient algorithm needed
    if n == 0:
        return 0

    if n == 1:
        return 1

    return nth_fibonacci_number(n - 1) + nth_fibonacci_number(n - 2)


def f(start: int, end: int) -> list:
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


@app.route('/health')
def health_check():
    return 'OK'


@app.route('/fib/<int:start_idx>/<int:end_idx>')
def fib(start_idx, end_idx):
    return f'Result: {fibonacci(start_idx, end_idx)}'
