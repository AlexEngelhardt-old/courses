import sys


def get_change_recursive(m):
    """Slow, naive solution.
    The available coins are 1, 3, and 4.
    Takes input m (amount to arrive at) and returns the minimum number of moves to arrive there.
    """
    if m < 0:
        raise ValueError("Invalid negative amount")
    if m == 0:
        raise ValueError("ok 0 moves, but this shouldn't happen either.")

    if m in [1, 3, 4]:
        return 1

    alt_paths = [get_change_recursive(m-1)]

    if m > 3:
        alt_paths.append(get_change_recursive(m-3))
    if m > 4:
        alt_paths.append(get_change_recursive(m-4))

    return min(alt_paths) + 1


def get_change(m):
    coins = [1, 3, 4]
    n_moves = [0 for _ in range(m+1)]  # contains [0] for money-amount = 0 (and 0 moves)
    for amount in range(1, m+1):
        legal_moves = []
        for c in coins:
            if amount >= c:  # only then can you use this coin
                legal_moves.append(n_moves[amount-c] + 1)
        n_moves[amount] = min(legal_moves)
    return n_moves[m]





if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
