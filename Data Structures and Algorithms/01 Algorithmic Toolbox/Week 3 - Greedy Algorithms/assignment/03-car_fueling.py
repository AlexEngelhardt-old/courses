# python3
import sys


def compute_min_refills(distance, tank, stops):
    n_gas_stations = len(stops)
    stops = [0] + stops + [distance]
    n_refills = 0
    pos_i = 0

    while pos_i <= n_gas_stations:
        last_refill = pos_i

        while pos_i <= n_gas_stations and stops[pos_i + 1] - stops[last_refill] <= tank:
            pos_i += 1

        if pos_i == last_refill:
            # no next step is possible
            return -1

        if pos_i <= n_gas_stations:
            n_refills += 1

    return n_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
