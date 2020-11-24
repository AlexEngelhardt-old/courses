from collections import namedtuple
from x3_is_bst_hard import IsBinarySearchTree, Node

tree = [
    Node(2, 1, 2),
    Node(1, -1, -1),
    Node(2, -1, -1)
]
print(f"Should be True: {IsBinarySearchTree(tree)}")


tree = [
    Node(2, 1, 2),
    Node(1, -1, 3),
    Node(3, -1, -1),
    Node(2, -1, -1)
]
print(f"Should be False: {IsBinarySearchTree(tree)}")


tree = [
    Node(4, 1, 2),
    Node(2, 3, 4),
    Node(6, 5, 6),
    Node(1, -1, -1),
    Node(3, -1, -1),
    Node(5, -1, -1),
    Node(7, -1, -1)
]
print(f"Should be True: {IsBinarySearchTree(tree)}")
