from mydisjointset import DJS

d = DJS()

for i in range(1, 10+1):
    d.make_set(i)

d.union(1, 3)
d.union(1, 6)
d.union(2, 4)
d.union(2, 5)
d.union(7, 8)
d.union(8, 9)

d.find(1)
d.find(2)
d.find(3)
d.find(4)
d.find(5)
d.find(6)
