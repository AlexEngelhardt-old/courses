from x1_acyclicity import acyclic
import utils

adj = [
    [1],  # connection from v1 to v2, i.e. index 0 to 1
    [2],
    [0],
    [0]
]

print(utils.DFS(adj))
print(utils.SCCs(adj))
print("Should be 1:", acyclic(adj))

adj = [
    [1, 2, 3],
    [2, 4],
    [3, 4],
    [],
    []
]

print(utils.DFS(adj))
print(utils.SCCs(adj))
print("Should be 0:", acyclic(adj))
