# Uses python3
import sys


def merge_slow(left, right):
    """Merge two sorted arrays into one sorted array."""
    res = [0] * (len(left) + len(right))
    idx_left = 0
    idx_right = 0
    i = 0
    n_inversions = 0
    while len(left) and len(right):
        if left[0] <= right[0]:
            res[i] = left[0]
            del left[0]
        else:
            n_inversions += sum([l > right[0] for l in left])
            res[i] = right[0]
            del right[0]
        i += 1
    res[i:] = left + right  # only one of left and right still has elements

    return n_inversions, res


def merge(left, right):
    """Merge two sorted arrays into one sorted array."""
    res = [0] * (len(left) + len(right))
    idx_left = 0
    idx_right = 0
    i = 0
    n_inversions = 0
    while len(left) and len(right):
        if left[0] <= right[0]:
            res[i] = left[0]
            del left[0]
        else:
            n_inversions += len(left)  # because *all* the remaining elements in left are inversions with right[0]
            res[i] = right[0]
            del right[0]
        i += 1
    res[i:] = left + right  # only one of left and right still has elements

    return n_inversions, res


def mergesort(arr):
    if len(arr) <= 1:
        return 0, arr

    mid = len(arr)//2
    n_inv_left, left = mergesort(arr[:mid])
    n_inv_right, right = mergesort(arr[mid:])
    n_inv, arr = merge(left, right)
    n_inv_total = n_inv + n_inv_left + n_inv_right
    return n_inv_total, arr


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    n_inv, a = mergesort(a)
    print(n_inv)
