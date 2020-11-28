import cProfile
from x2_toposort import toposort

adj = [
    [1],  # connection from v1 to v2, i.e. index 0 to 1
    [2],
    [0],
    [0]
]

print(toposort(adj))

adj = [
    [1, 2, 3],
    [2, 4],
    [3, 4],
    [],
    []
]

print(toposort(adj))

# cProfile.run('toposort(adj)')
