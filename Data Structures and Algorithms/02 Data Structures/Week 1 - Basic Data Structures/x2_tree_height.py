# python3

import sys
import threading
from collections import deque
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:
    def __init__(self, name=None, parent=None):
        self.name = name
        self.parent = parent
        self.children = list()
        self.level = None  # unknown now, but will be added later

    def add_child(self, i):
        self.children.append(i)


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.build_tree()

    def build_tree(self):
        # build the tree out of nodes, top down now (so you know the children of each node)
        self.nodes = [Node(name=i, parent=self.parent[i]) for i in range(self.n)]  # content: its parent
        for node_i, dad in enumerate(self.parent):
            if dad == -1:
                self.root_i = node_i
            else:
                self.nodes[dad].add_child(node_i)

    def compute_height(self):  # do it Breadth-First Search, with a queue
        self.nodes[self.root_i].level = 1
        max_level = 1
        queue = deque()
        queue.append(self.nodes[self.root_i])

        while queue:
            this_node = queue.popleft()
            if not this_node.level:  # cause root's level is already set
                this_node.level = 1 + self.nodes[this_node.parent].level  # it exists since we traverse by level
                # max_level = max(max_level, this_node.level)
                max_level = this_node.level  # should work because we traverse by level, deepest one last
            for child_i in this_node.children:
                queue.append(self.nodes[child_i])

        return max_level

    def compute_height_recursively(self, starting_at=None):  # seems to throw a recursion error
        if starting_at is None:
            starting_at = self.root_i
        if not self.nodes[starting_at].children:  # leaf node
            return 1
        else:
            return 1 + max([self.compute_height(starting_at=child_i) for child_i in self.nodes[starting_at].children])

    def compute_height_slow(self):
        # Replace this code with a faster implementation
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height)
        return maxHeight


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()
