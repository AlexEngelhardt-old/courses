# Uses python3
import sys


def optimal_sequence_greedy(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return sequence[::-1]


def optimal_sequence_dp(n):
    # Create the arary of min_n_steps_to_here:
    min_n_moves = [0] + [-1] * (n-1)
    for i in range(2, n+1):  # i is the actual number we want to get to, i-1 will be its array index
        candidates = [min_n_moves[i-2]]
        if i % 3 == 0:
            candidates.append(min_n_moves[i//3 - 1])
        if i % 2 == 0:
            candidates.append(min_n_moves[i//2 - 1])
        min_n_moves[i-1] = min(candidates) + 1

    # Backtrace one possible best path
    path = [n]  # start with the last number
    current_num = n
    while current_num >= 2:
        # decrease current_index to next lower number: max. three candidates
        if current_num % 3 == 0 and min_n_moves[current_num // 3 - 1] == min_n_moves[current_num-1] - 1:
            current_num //= 3
        elif current_num % 2 == 0 and min_n_moves[current_num // 2 - 1] == min_n_moves[current_num-1] - 1:
            current_num //= 2
        elif min_n_moves[current_num-2] == min_n_moves[current_num-1] - 1:
            current_num -= 1
        else:
            raise RuntimeError("This shouldn't have happened!")

        # append the next element to the path
        path.append(current_num)  # current_index is the number, min_n_moves[current_index] the n_moves to get there

    path.reverse()
    return path


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence_dp(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
