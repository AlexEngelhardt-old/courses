import sys

sys.setrecursionlimit(200000)

def explore(adj, src, visited=None, previsit=None, postvisit=None, found_vertices=None, clock=0):
    if visited is None:
        visited = [False for _ in range(len(adj))]
    if previsit is None:
        previsit = [0 for _ in range(len(adj))]
    if postvisit is None:
        postvisit = [0 for _ in range(len(adj))]
    if found_vertices is None:
        found_vertices = []
    visited[src] = True
    found_vertices.append(src)
    # <previsit>
    previsit[src] = clock
    clock += 1
    # </previsit>
    for dest in adj[src]:
        if not visited[dest]:
            found_vertices, visited, previsit, postvisit, clock = explore(adj, dest, visited, previsit, postvisit, found_vertices, clock)
    # <postvisit>
    postvisit[src] = clock
    clock += 1
    # </postvisit>

    return found_vertices, visited, previsit, postvisit, clock


def find_sink(adj, v=0):
    # Graph must be acyclic, else we'll run into an infinite loop
    while adj[v]:
        v = adj[v][0]
    return v


def reverse_graph(adj):
    adj_rev = [[] for _ in range(len(adj))]
    for src in range(len(adj)):
        for dest in adj[src]:
            adj_rev[dest].append(src)

    return adj_rev


def DFS(adj):
    # Make sure to return the pre- and especially post-order numbers.
    # We need them for topological sort
    previsit = [0 for _ in range(len(adj))]
    postvisit = [0 for _ in range(len(adj))]
    visited = [False for _ in range(len(adj))]
    found_vertices = []
    clock = 0
    for v in range(len(adj)):
        if not visited[v]:
            found_vertices, visited, previsit, postvisit, clock = explore(adj, v, visited, previsit, postvisit, found_vertices, clock)
    assert sum(visited) == len(visited)
    return previsit, postvisit


def SCCs(adj):
    CC = [0 for _ in range(len(adj))]  # strongly connected components

    _, postvisit = DFS(reverse_graph(adj))
    cc_ctr = 1
    while max(postvisit) > 0:
        v = postvisit.index(max(postvisit))
        found_vertices, _, _, _, _ = explore(adj, v)
        for fv in found_vertices:
            if CC[fv] == 0:  # if it's untouched, that is
                CC[fv] = cc_ctr
            postvisit[fv] = 0  # just remove them
        cc_ctr += 1

    return CC


def number_of_strongly_connected_components(adj):
    return max(SCCs(adj))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
