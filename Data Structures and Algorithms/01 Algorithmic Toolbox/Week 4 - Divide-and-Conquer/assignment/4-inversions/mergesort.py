def merge_old(left, right):
    """Merge two sorted arrays into one sorted array."""
    res = [0] * (len(left) + len(right))
    idx_left = 0
    idx_right = 0
    for i in range(len(res)):
        if idx_right >= len(right):
            res[i] = left[idx_left]
            idx_left += 1
        elif idx_left >= len(left):
            res[i] = right[idx_right]
            idx_right += 1
        elif left[idx_left] < right[idx_right]:
            res[i] = left[idx_left]
            idx_left += 1
        else:
            res[i] = right[idx_right]
            idx_right += 1
    return res


def merge(left, right):
    """Merge two sorted arrays into one sorted array."""
    res = [0] * (len(left) + len(right))
    idx_left = 0
    idx_right = 0
    i = 0
    while len(left) and len(right):
        if left[0] < right[0]:
            res[i] = left[0]
            del left[0]
        else:
            res[i] = right[0]
            del right[0]
        i += 1
    res[i:] = left + right  # only one of left and right still has elements

    return res


def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)
