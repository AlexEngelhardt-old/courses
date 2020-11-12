import sys

# In this knapsack version, w_i == v_i, since we are dealing with gold bars


def optimal_weight(W, w):

    values = [[0 for _ in range(W+1)] for _ in range(len(w)+1)]

    for sack_weight in range(1, W+1):
        for n_bars in range(1, len(w)+1):
            dont_use_bar_i = values[n_bars-1][sack_weight]
            use_bar_i = 0 if w[n_bars-1] > sack_weight else values[n_bars-1][sack_weight-w[n_bars-1]] + w[n_bars-1]
            values[n_bars][sack_weight] = max(
                use_bar_i, dont_use_bar_i
            )

    return values[len(w)][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
