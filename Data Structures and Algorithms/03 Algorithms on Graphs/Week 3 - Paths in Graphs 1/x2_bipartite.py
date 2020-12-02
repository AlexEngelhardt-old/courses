import sys
from collections import deque


def bfs_colors(adj, colors, start):
    """Returns "coloring" of a graph to check if its bipartite: We start BFS on a "white" node,
    then all edge targets will be colored black, and so on.
    The color is basically the BFS distance modulo 2."""

    if colors[start] != -1:
        # Then we already know this node
        return colors

    colors[start] = True

    node_queue = deque()
    node_queue.append(start)

    while node_queue:
        v = node_queue.popleft()

        for destination in adj[v]:
            if colors[destination] == -1:  # i.e. if undiscovered
                node_queue.append(destination)
                colors[destination] = not colors[v]

    return colors


def bipartite(adj):
    colors = [-1 for _ in range(len(adj))]

    for start in range(len(adj)):
        # start BFS from *every* node once, to surely discover all vertex colors.
        # Between different SCCs, the colors don't matter, since no edge goes between them anyway.
        colors = bfs_colors(adj, colors, start)

    for source in range(len(adj)):
        for dest in adj[source]:
            if colors[source] == -1 or colors[dest] == -1:  # these nodes are unconnected, their color doesn't matter
                continue
            if colors[source] == colors[dest]:
                return 0  # Graph is not bipartite

    return 1  # Graph *is* bipartite


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
