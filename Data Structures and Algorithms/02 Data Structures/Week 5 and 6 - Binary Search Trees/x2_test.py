from collections import namedtuple
from x2_is_bst import IsBinarySearchTree

Node = namedtuple('Node', ['value', 'left', 'right'])

tree = [
    Node(2, 1, 2),
    Node(1, -1, -1),
    Node(2, -1, -1)
]

print(IsBinarySearchTree(tree))

tree = [
    Node(4, 1, 2),
    Node(2, 3, 4),
    Node(6, 5, 6),
    Node(1, -1, -1),
    Node(3, -1, -1),
    Node(5, -1, -1),
    Node(7, -1, -1)
]

print(IsBinarySearchTree(tree))
