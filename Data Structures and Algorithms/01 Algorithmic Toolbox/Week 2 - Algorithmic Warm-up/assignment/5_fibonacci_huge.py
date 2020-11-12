"""Find the n-th Fibonacci number modulo m.

The Pisano period helps you there.

"Therefore, to compute,
say, F_2015 mod 3 we just need to find the remainder of 2015 when divided by 8. Since 2015 = 251 · 8 + 7, we
conclude that F_2015 mod 3 = F 7 mod 3 = 1."
"""

# Uses python3
import sys


def get_fibonacci_huge_fast(n, m):
    if m == 1:
        return 0

    cycle = [0, 1, 1]
    while True:
        next = (cycle[-1] + cycle[-2]) % m
        if cycle[-1] == 0 and next == 1:
            cycle = cycle[:-1]  # delete the last zero, because it starts a new cycle
            break
        else:
            cycle.append(next)

    n = n % len(cycle)
    return cycle[n]


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
