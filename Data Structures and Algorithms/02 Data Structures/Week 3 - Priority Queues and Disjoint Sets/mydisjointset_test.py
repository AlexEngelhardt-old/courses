from mydisjointset import DJS

d = DJS()

for val in range(1, 10+1):
    d.make_set(val)

print(d.parent)
print(d.contents)
print(d.length)

d.union(1, 3)
d.union(1, 6)
d.union(2, 4)
d.union(2, 5)
d.union(7, 8)
d.union(8, 9)

print(d.find(1))
print(d.find(2))
print(d.find(3))
print(d.find(4))
print(d.find(5))
print(d.find(6))
