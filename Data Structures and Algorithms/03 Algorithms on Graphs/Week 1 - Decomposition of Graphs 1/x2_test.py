from x2_connected_components import number_of_components

n = 4  # n vertices, named from 1 to n
m = 4  # m edges

adj = [  # Adjacency list
    [1],
    [0, 2],
    [1],
    []
]

print(number_of_components(adj))
