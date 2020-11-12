"""Greatest common divisor: Find the greatest d that divides
both inputs a and b.

GCD(10, 4) = 2

GCD(3918848, 1653264) = ?
"""


def gcd(a, b):
    """Runtime approx. a+b. Apparently this is too slow.
    """
    best = 0
    for d in range(1, a+b+1):
        # why does it need to run until a+b? I thought min(a, b)?

        if a % d == 0 and b % d == 0:
            best = d

    return best


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(gcd(a, b))
