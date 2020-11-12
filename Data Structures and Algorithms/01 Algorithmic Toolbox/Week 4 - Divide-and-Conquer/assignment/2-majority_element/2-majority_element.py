# Uses python3
import sys

"""You have to write an O(n log(n)) algorithm here.
As per the video on the Master Theorem, you end up with O(n logn) iff you break your problems
into *two* subproblems, each with runtime T(n/2) + O(n):

T(n) = 2 * T(n/2) + O(n)
"""


def is_majority(candidate, array, left, right):
    return array[left:right].count(candidate) > (right-left)/2


def get_majority_element(a, left, right):
    if left == right:
        raise ValueError("shouldn't even happen")
        # return -1
    if left + 1 == right:  # Python style indexing here, i.e. a[0:1] is only one element
        return a[left]

    # Now, the array is at least size 2
    mid = left + (right-left) // 2  # add +1 because Python-style indexing
    majority_left = get_majority_element(a, left, mid)
    majority_right = get_majority_element(a, mid, right)

    if majority_left != -1:
        # we have a *candidate*. Verify it is one:
        if is_majority(majority_left, a, left, right):
            return majority_left
    if majority_right != -1:
        if is_majority(majority_right, a, left, right):
            return majority_right

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
