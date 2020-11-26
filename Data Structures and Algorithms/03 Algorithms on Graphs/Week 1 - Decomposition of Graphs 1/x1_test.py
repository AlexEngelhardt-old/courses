from x1_reachability import reach

n = 4  # n vertices, named from 1 to n
m = 4  # m edges

adj = [  # Adjacency list
    [1, 3],  # Vertex 1 reaches 2 and 4
    [0, 2],  # Vertex 2 reaches 1 and 3
    [3, 1],
    [0, 2]
]

adj = [  # Adjacency list
    [1],
    [0, 2],
    [1],
    []
]

u = 1
v = 4  # can we reach v 4 from v 1?

print(reach(adj, u-1, v-1))
