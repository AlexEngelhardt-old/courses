# Uses python3
import sys


def get_fibonacci_last_digit(n):
    if n <= 2:
        return 1

    previous = 1
    current = 1

    for _ in range(2, n):
        previous, current = current, (previous + current) % 10

    return current


if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_fibonacci_last_digit(n))
