# Uses python3
import sys
import random


def partition2(a, l, r):
    x = a[l]
    j = l  # j is the position of the pivot
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def partition3(a, l, r):
    """Returns m1, m2, so that
    a[i] < a[0] for all l <= i <= m1-1,
    a[i] > a[0] for all m1+1 <= i <= r,
    a[i] == a[0] for all m1 <= i <= m2
    """
    x = a[l]
    m1 = m2 = l  # m2 is the position of the pivot x, m1 is the min_pos of the first element == x
    for i in range(l+1, r+1):
        if a[i] < x:
            m1 += 1
            m2 += 1
            a[i], a[m2] = a[m2], a[i]
            a[m2], a[m1] = a[m1], a[m2]
        elif a[i] == x:
            m2 += 1
            a[i], a[m2] = a[m2], a[i]
        elif a[i] > x:
            pass

    a[l], a[m1] = a[m1], a[l]
    return m1, m2


def randomized_quick_sort(a, l, r, partition=3):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    if partition == 2:
        m = partition2(a, l, r)
        randomized_quick_sort(a, l, m - 1)
        randomized_quick_sort(a, m + 1, r)
    elif partition == 3:
        m1, m2 = partition3(a, l, r)
        randomized_quick_sort(a, l, m1 - 1)
        randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
