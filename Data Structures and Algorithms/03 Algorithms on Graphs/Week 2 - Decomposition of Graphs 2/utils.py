def explore(adj, src, visited=None, previsit=None, postvisit=None, clock=0):
    if visited is None:
        visited = [False for _ in range(len(adj))]
    if previsit is None:
        previsit = [0 for _ in range(len(adj))]
    if postvisit is None:
        postvisit = [0 for _ in range(len(adj))]
    visited[src] = True
    # <previsit>
    previsit[src] = clock
    clock += 1
    # </previsit>
    for dest in adj[src]:
        if not visited[dest]:
            _, visited, previsit, postvisit, clock = explore(adj, dest, visited, previsit, postvisit, clock)
    # <postvisit>
    postvisit[src] = clock
    clock += 1
    # </postvisit>

    # TODO that may be wrong, because we include vertices found in previous calls to explore. Do we intend that?
    found_vertices = [i for i in range(len(adj)) if visited[i]]

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
    clock = 0
    for v in range(len(adj)):
        if not visited[v]:
            found_vertices, visited, previsit, postvisit, clock = explore(adj, v, visited, previsit, postvisit, clock)
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
