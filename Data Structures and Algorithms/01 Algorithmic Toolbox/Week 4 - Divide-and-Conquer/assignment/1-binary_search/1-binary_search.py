# Uses python3
import math
import sys


def binary_search(a, x, left=0, right=None):
    if right is None:
        right = len(a)-1
    if left > right:
        return -1

    mid_key = math.floor(left + (right-left)/2)
    if a[mid_key] == x:
        return mid_key
    elif a[mid_key] > x:
        return binary_search(a, x, left=left, right=mid_key-1)
    elif a[mid_key] < x:
        return binary_search(a, x, left=mid_key+1, right=right)

    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    values = data[n + 2:]
    for x in values:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')
