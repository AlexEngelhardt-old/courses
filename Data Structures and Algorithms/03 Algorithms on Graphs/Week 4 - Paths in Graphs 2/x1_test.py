from x1_dijkstra import distance

input = """4 4
1 2 1
4 1 2
2 3 2
1 3 5
1 3
"""

data = list(map(int, input.split()))
n, m = data[0:2]
data = data[2:]
edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
data = data[3 * m:]
adj = [[] for _ in range(n)]
cost = [[] for _ in range(n)]
for ((a, b), w) in edges:
    adj[a - 1].append(b - 1)
    cost[a - 1].append(w)
s, t = data[0] - 1, data[1] - 1
print(distance(adj, cost, s, t))
