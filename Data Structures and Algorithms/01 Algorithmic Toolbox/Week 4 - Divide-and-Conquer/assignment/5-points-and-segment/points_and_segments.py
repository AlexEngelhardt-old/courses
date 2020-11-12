# Uses python3
import sys
import bisect


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    n_segments = len(starts)
    starts.sort()
    ends.sort()

    for i in range(len(points)):
        n_ending_before = bisect.bisect_left(ends, points[i])
        n_starting_after = n_segments - bisect.bisect_right(starts, points[i])
        cnt[i] = n_segments - n_ending_before - n_starting_after
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    #cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
