# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0
    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next
    return sum % 10


def pisano10():
    fibs = [0, 1] + [-1 for i in range(2, 61)]
    for i in range(2, 61):
        fibs[i] = fibs[i-1] + fibs[i-2]
    sum_fibs = [sum(fibs[:i]) % 10 for i in range(1, len(fibs))]
    return sum_fibs


def fibonacci_sum_fast(n):
    """The cumsum is also a period of length 60, like the Fib-mod-10 Pisano series."""
    fib_sum_mod10 = pisano10()
    return fib_sum_mod10[n % 60]


def fibonacci_partial_sum_fast(a, b):
    return (fibonacci_sum_fast(b) + 10 - fibonacci_sum_fast(a-1)) % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))