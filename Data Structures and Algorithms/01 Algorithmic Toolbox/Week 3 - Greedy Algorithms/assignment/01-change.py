# Uses python3
import sys


def get_change(amount, coins=[10, 5, 1]):
    # The 'coins' array must be sorted descending
    n_coins = amount // coins[0]
    new_amount = amount - n_coins * coins[0]
    if len(coins) > 1:
        n_coins += get_change(new_amount, coins[1:])
    return n_coins


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
