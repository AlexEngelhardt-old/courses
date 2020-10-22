"""Let's implement the Euclidean Algorithm.
Runtime ca. log(ab)

Lemma:

Let a' be the remainder when a is divided by b, then

gcd(a, b) = gcd(a', b)

gcd(3918848, 1653264)
= gcd(1653264, 612320)
= gcd(612320, 428624)
= ... etc
"""


def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    else:
        a_prime = a % b
        return gcd(b, a_prime)


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(gcd(a, b))
