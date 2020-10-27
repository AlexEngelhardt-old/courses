# Uses python3
import sys


def optimal_summands_slow(n):
    summands = []
    current_prize = 1
    total_prizes = 0
    while total_prizes < n:
        # first check if a next prize is possible, if no, give everything to the now first place:
        if total_prizes + current_prize + current_prize+1 > n:
            current_prize = n - total_prizes
            summands += [current_prize]
            break

        total_prizes += current_prize
        summands += [current_prize]
        current_prize += 1

    return summands


def optimal_summands_fast(n):
    # Something with Gauss' sum_i=1^n i Algorithm, probably.
    n_prizes = 1
    while (n_prizes+1) * (n_prizes+2) / 2 <= n:
        n_prizes += 1

    last_prize = int(n - ((n_prizes-1) * n_prizes / 2))

    summands = list(range(1, n_prizes)) + [last_prize]
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands_fast(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
