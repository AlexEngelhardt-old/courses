def lfill(arr, length):
    """Prepends [0] elements to arr so that its total length is at least length."""
    return [0] * (length - len(arr)) + arr


def poly_mult_naive(A, B):
    """Naive  O(n^2) implementation of polynomial multiplication.
    A and B are coefficient arrays:

    Example
    -------

    A = 3x^2 + 2x + 5
    B = 5x^2 + x + 2
    A * B = 15x^4 + 13x^3 + 33x^2 + 9x + 10

    >>> poly_mult([3, 2, 5], [5, 1, 2])

    [15, 13, 33, 9, 10]

    >>> poly_mult([3, 2, 5], [4])

    [12, 8, 20]

    """

    n = max(len(A), len(B))
    A = lfill(A, n)
    B = lfill(B, n)

    res = [0] * (2*n - 1)

    for i in range(n):
        for j in range(n):
            res[i+j] += A[i] * B[j]

    # If there are leading zeroes, remove them again:
    while(res[0] == 0):
        del res[0]

    return res


def poly_mult_better(A, B):
    """Divide-and-conquer implementation for polynomial multiplication.
    Still a bit naive though.

    Idea: Split up A into D1 and D0, each of degree n/2.
    e.g. A = [4, 3, 2, 1], then D1 = [4, 3] and D2 = [2, 1]
    Just split them up, no computation necessary.
    Split B into E1 and E0 in the same way.

    Then AB = D1*E1 * x^n + (D1*E0 + D0*E1) * x^(n/2) + D0*E0

    Runtime: T(n) = 4 * T(n/2) + kn
    Total runtime: O(n^2)
    """

    # Meh, I'll skip this
    pass


def poly_mult_fast(A, B):
    """By Karatsuba"""

    # meh.

    return [1, 2, 3]


if __name__ == "__main__":
    print(poly_mult_naive([3, 2, 5], [5, 1, 2]))
    print(poly_mult_fast([3, 2, 5], [5, 1, 2]))
    print('---')
    print(poly_mult_naive([3, 2, 5], [4]))
    print(poly_mult_fast([3, 2, 5], [4]))