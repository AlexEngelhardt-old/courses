#!/usr/bin/python3

from collections import namedtuple, deque
import sys
import threading

Node = namedtuple('Node', ['value', 'left', 'right'])

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    """I think a tree is a BST iff the in-order traversal is sorted"""
    if not tree:  # an empty list is a BST
        return True

    stack = deque()
    results = []
    current_node = 0
    current_value = float('-inf')

    while True:
        while current_node != -1:
            stack.append(current_node)
            current_node = tree[current_node].left

        item = stack.pop()

        if tree[item].value <= current_value:
            return False
        else:
            current_value = tree[item].value

        current_node = tree[item].right

        if not stack and current_node == -1:
            break

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


if __name__ == '__main__':
    threading.Thread(target=main).start()
