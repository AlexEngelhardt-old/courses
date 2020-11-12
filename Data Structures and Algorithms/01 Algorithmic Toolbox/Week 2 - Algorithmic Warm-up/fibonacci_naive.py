"""Surprisingly, the recursive naive version breaks for n ~= 40

The running time T(n) is T(n-1) + T(n-2) + 3.
This is exponential running time.
Because you evaluate F(n-4) multiple times! The lower the number,
the more often you compute them.

Fib(100) takes 56000 years to compute!
"""


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    n = int(input())

    print(fib(n))
