import sys
from utils import *


def acyclic(adj):
    """A graph is acyclic iff every vertex is in its own Strongly Connected Component."""
    scc = SCCs(adj)
    is_acyclic = len(set(scc)) == len(scc)
    return int(not is_acyclic)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
