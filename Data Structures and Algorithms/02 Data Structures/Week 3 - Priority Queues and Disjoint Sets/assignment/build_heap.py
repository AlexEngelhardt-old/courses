def build_min_heap_naive(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def sift_down(data, i):
    left_child_i = i * 2 + 1
    right_child_i = i * 2 + 2
    new_i = i
    if left_child_i < len(data):
        if data[new_i] > data[left_child_i]:
            new_i = left_child_i
    if right_child_i < len(data):
        if data[new_i] > data[right_child_i]:
            new_i = right_child_i
    if new_i != i:
        data[i], data[new_i] = data[new_i], data[i]
        return [(i, new_i)] + sift_down(data, new_i)
    return []


def build_min_heap(data):
    # SiftDown for all n nodes (bzw. those that have at least one child)
    swaps = []
    first_parent = (len(data)-2) // 2
    for i in range(first_parent, -1, -1):
        swaps.extend(sift_down(data, i))
    return swaps


if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_min_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
