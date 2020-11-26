import sys


def explore(v, adj, visited):
    res = [v]
    visited[v] = 1
    for v2 in adj[v]:
        if not visited[v2]:
            explore(v2, adj, visited)


def number_of_components(adj):
    n_vertices = len(adj)
    result = 0
    visited = [0 for _ in range(n_vertices)]

    while sum(visited) < n_vertices:
        result += 1
        next_vertex = [v for v in range(n_vertices) if not visited[v]][0]
        explore(next_vertex, adj, visited)

    return result


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
    print(number_of_components(adj))
