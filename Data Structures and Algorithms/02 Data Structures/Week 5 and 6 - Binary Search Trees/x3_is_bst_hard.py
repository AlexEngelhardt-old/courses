#!/usr/bin/python3

import sys, threading
from collections import deque


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.meta = dict()


sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    """Here a BST can contain duplicate keys, but the have to be in the right child, not the left.
    The left child is strictly less than the parent, the right child is >=.

    Post-order traverse the tree (algo from here: https://www.geeksforgeeks.org/iterative-postorder-traversal/),
    and for each subtree check the largest left value and the smallest right value. It's a kind-of dynamic
    programming approach.
    """
    if not tree:  # an empty list is a BST
        return True

    stack1 = deque()
    stack2 = deque()

    stack1.append(0)  # don't push the actual tree nodes, but only their indices. We need them later.

    while stack1:
        item = stack1.pop()
        stack2.append(item)
        if tree[item].left != -1:
            stack1.append(tree[item].left)
        if tree[item].right != -1:
            stack1.append(tree[item].right)

    while stack2:
        # In here we actually traverse the tree's items in a post-order way.
        # Because it's post-order, we can be sure that each item's children have already been processed.
        item = stack2.pop()

        tree[item].meta['subtree_largest_value'] = tree[item].value
        tree[item].meta['subtree_smallest_value'] = tree[item].value
        if tree[item].left != -1:
            if tree[item].value <= tree[tree[item].left].meta['subtree_largest_value']:
                return False

            tree[item].meta['subtree_largest_value'] = max(
                tree[item].meta['subtree_largest_value'],
                tree[tree[item].left].value
            )
            tree[item].meta['subtree_smallest_value'] = min(
                tree[item].meta['subtree_smallest_value'],
                tree[tree[item].left].value
            )
        if tree[item].right != -1:
            if tree[item].value > tree[tree[item].right].meta['subtree_smallest_value']:
                return False

            tree[item].meta['subtree_largest_value'] = max(
                tree[item].meta['subtree_largest_value'],
                tree[tree[item].right].value
            )
            tree[item].meta['subtree_smallest_value'] = min(
                tree[item].meta['subtree_smallest_value'],
                tree[tree[item].right].value
            )

    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(Node(*map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
