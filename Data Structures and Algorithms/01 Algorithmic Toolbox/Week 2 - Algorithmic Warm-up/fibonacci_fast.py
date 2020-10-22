"""This version runs in linear time instead.

T(n) = 2n + 2
T(100) = 202 "lines of code"
"""


def fib(n):
    if n <= 2:
        return 1
    fibs = [1 for i in range(n)]

    for i in range(2, n):
        fibs[i] = fibs[i-1] + fibs[i-2]

    return fibs[n-1]


if __name__ == '__main__':
    n = int(input())

    print(fib(n))
