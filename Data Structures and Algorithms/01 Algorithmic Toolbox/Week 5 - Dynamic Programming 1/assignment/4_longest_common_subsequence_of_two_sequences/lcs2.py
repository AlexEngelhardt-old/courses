import sys


def lcs2(a, b):
    mx = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]

    for i in range(len(b)):
        for j in range(len(a)):
            if a[j] == b[i]:
                mx[i+1][j+1] = mx[i][j] + 1
            else:
                mx[i+1][j+1] = max(mx[i][j+1], mx[i+1][j])

    # for row in range(len(mx)):
    #     print(mx[row])

    lcs = mx[-1][-1]
    return lcs


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
