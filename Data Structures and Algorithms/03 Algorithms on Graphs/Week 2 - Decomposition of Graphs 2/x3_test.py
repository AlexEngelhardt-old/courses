import cProfile
from utils import SCCs

adj = [
    [1, 2, 3],
    [2, 4],
    [3, 4],
    [],
    []
]

print(SCCs(adj))

cProfile.run('SCCs(adj*1000)')
