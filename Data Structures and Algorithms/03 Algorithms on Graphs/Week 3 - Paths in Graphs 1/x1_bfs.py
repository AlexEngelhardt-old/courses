import sys
from collections import deque


def bfs(adj, start):
    distances = [-1 for _ in range(len(adj))]
    distances[start] = 0

    node_queue = deque()
    node_queue.append(start)

    while node_queue:
        v = node_queue.popleft()

        for destination in adj[v]:
            if distances[destination] == -1:  # i.e. if undiscovered
                node_queue.append(destination)
                distances[destination] = distances[v] + 1

    return distances


def distance(adj, s, t):
    distances = bfs(adj, start=s)
    return distances[t]


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
