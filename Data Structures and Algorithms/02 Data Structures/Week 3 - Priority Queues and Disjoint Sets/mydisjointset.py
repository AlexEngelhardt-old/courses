class DJS:
    def __init__(self):
        self.parent = []
        self.contents = []
        self.rank = []
        self.length = 0

    def make_set(self, value):
        # TODO we have to check make_set's `i` is not already in the set, right? That's currently
        # TODO an O(n) operation (without hash maps / dicts)
        self.parent.append(self.length)  # parent[i] = i
        self.rank.append(0)
        self.contents.append(value)
        self.length += 1
        return self.length - 1  # the new index i

    def union(self, i, j):
        i_root = self.find(i)
        j_root = self.find(j)
        if i == j:  # they already are unioned
            return
        if self.rank[i_root] > self.rank[j_root]:
            self.parent[j_root] = i_root
        else:
            self.parent[i_root] = j_root
            if self.rank[i_root] == self.rank[j_root]:
                self.rank[j_root] += 1

    def find(self, i):
        # TODO "path compression" is not yet implemented here.
        while i != self.parent[i]:
            i = self.parent[i]
        return i
