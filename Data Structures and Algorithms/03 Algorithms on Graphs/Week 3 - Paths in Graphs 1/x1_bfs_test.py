from x1_bfs import distance, bfs

adj = [
    [1, 2, 3],
    [0, 2],
    [0, 1],
    [0]
]

s = 2
t = 4
print(bfs(adj, s-1))
print(distance(adj, s-1, t-1))
