import sys


def explore(v, adj, visited):
    res = [v]
    visited[v] = 1
    for v2 in adj[v]:
        if not visited[v2]:
            explore(v2, adj, visited)


def reach(adj, x, y):
    n_nodes = len(adj)
    visited = [0 for _ in range(n_nodes)]
    explore(x, adj, visited)  # visited is passed by reference, so it'll stay the same list during recurisve calls!
    return visited[y]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
