# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fibonacci_sum_squares_fast(n):
    """The last digit of the sum of the first n squared Fib numbers equals
    (Fib_n%10 * Fib_(n+1)%10) % 10
    See the week2 PDF for why this works."""

    last_digits = [0, 1, 1]
    while True:
        next = (last_digits[-1] + last_digits[-2]) % 10
        if last_digits[-1] == 0 and next == 1:
            last_digits = last_digits[:-1]  # delete the last zero, because it starts a new cycle
            break
        else:
            last_digits.append(next)

    ssq_last_digit = (last_digits[n % 60] * last_digits[(n+1) % 60]) % 10
    return ssq_last_digit


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_fast(n))
