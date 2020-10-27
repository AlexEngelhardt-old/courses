"""Find the least common multiple of two integers"""

# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def lcm_faster(a, b):
    """This one is faster, but doesn't seem perfect just yet."""
    if a <= b:
        smaller, larger = a, b
    else:
        smaller, larger = b, a
    lcm_candidate = larger
    while lcm_candidate % smaller:
        lcm_candidate += larger
    return lcm_candidate


if __name__ == '__main__':
    #inp = sys.stdin.read()
    inp = input()
    a, b = map(int, inp.split())
    # print(lcm_naive(a, b))
    print(lcm_faster(a, b))

