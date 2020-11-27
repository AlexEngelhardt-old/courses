def explore(adj, src, visited=None):
    if visited is None:
        visited = [False for _ in range(len(adj))]
    visited[src] = True
    for dest in adj[src]:
        if not visited[dest]:
            explore(adj, dest, visited)

    found_vertices = [i for i in range(len(adj)) if visited[i]]
    return found_vertices, visited


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
    CC = [0 for _ in range(len(adj))]
    previsit = [0 for _ in range(len(adj))]
    postvisit = [0 for _ in range(len(adj))]
    visited = [False for _ in range(len(adj))]

    cc_ctr = 1
    for v in range(len(adj)):
        if not visited[v]:
            found_vertices, visited = explore(adj, v, visited)
            for v in found_vertices:
                CC[v] = cc_ctr
            cc_ctr += 1
