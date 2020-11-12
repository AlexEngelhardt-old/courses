"""The goal in this problem is to find the last digit of a sum of the first n Fibonacci numbers.

Instead of computing this sum in a loop, try to come up with a formula for F 0 + F 1 + F 2 + · · · + F n . For
this, play with small values of n. Then, use a solution for the previous problem.
"""
# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

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


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))

