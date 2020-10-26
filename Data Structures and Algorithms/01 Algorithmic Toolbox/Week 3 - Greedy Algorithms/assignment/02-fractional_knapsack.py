# Uses python3
import sys


def get_val_per_weight(weights, values):
    return [v / w for v, w in zip(values, weights)]


def sort_by_valperweight(weights, values, verbose=False):
    val_per_weight = get_val_per_weight(weights, values)
    sort_index_order = [i[0] for i in sorted(enumerate(val_per_weight), key=lambda x:x[1], reverse=True)]
    reordered_weights = [weights[i] for i in sort_index_order]
    reordered_values = [values[i] for i in sort_index_order]
    return reordered_weights, reordered_values


def get_optimal_value(capacity, weights, values, sort_it=True, verbose=False):
    value = 0.
    n_items = len(weights)
    if sort_it:
        weights, values = sort_by_valperweight(weights, values, verbose=verbose)
    val_per_weight = get_val_per_weight(weights, values)
    if verbose:
        print("*" * 30)
        print(f"capacity: {capacity}")
        print(f"weights: {weights}")
        print(f"values: {values}")
        print(f"val_per_weight: {val_per_weight}")

    if weights[0] > capacity:  # this includes the case capacity==0, which returns 0
        return val_per_weight[0] * capacity
    else:
        value += values[0]
        capacity -= weights[0]

        if n_items > 1:
            value += get_optimal_value(capacity, weights[1:], values[1:], sort_it=False, verbose=verbose)

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
