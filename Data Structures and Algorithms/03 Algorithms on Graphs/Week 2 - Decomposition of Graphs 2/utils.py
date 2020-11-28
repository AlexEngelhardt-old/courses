def explore(adj, src, visited=None, previsit=None, postvisit=None, found_vertices=None, clock=0):
    if found_vertices is None:
        found_vertices = set()
    visited[src] = True
    found_vertices.add(src)
    # <previsit>
    if previsit is not None:
        previsit[src] = clock
        clock += 1
    # </previsit>
    for dest in adj[src]:
        if not visited[dest]:
            found_vertices, visited, previsit, postvisit, clock = explore(adj, dest, visited, previsit, postvisit, found_vertices, clock)
    # <postvisit>
    if postvisit is not None:
        postvisit[src] = clock
        clock += 1
    # </postvisit>

    return found_vertices, visited, previsit, postvisit, clock


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
    found_vertices = set()
    clock = 0
    for v in range(len(adj)):
        if not visited[v]:
            found_vertices, visited, previsit, postvisit, clock = explore(adj, v, visited, previsit, postvisit, found_vertices, clock)
    assert sum(visited) == len(visited)
    return previsit, postvisit


def SCCs(adj):
    CC = [0 for _ in range(len(adj))]  # strongly connected components
    visited = [False for _ in range(len(adj))]
    found_vertices = set()

    _, postvisit = DFS(reverse_graph(adj))
    cc_ctr = 1

    # emulate np.argsort or R's order() here:
    arg_order = sorted(range(len(postvisit)), key=lambda k: postvisit[k], reverse=True)

    for v in arg_order:
        if v in found_vertices:
            continue
        found_vertices, visited, _, _, _ = explore(adj, v, visited, found_vertices=found_vertices)

        for fv in found_vertices:
            if CC[fv] == 0:  # if it's untouched, that is
                CC[fv] = cc_ctr
        cc_ctr += 1

    return CC
