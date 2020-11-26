import sys
from collections import deque
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrderRecursive(self, start=0):
        result = []

        if self.left[start] != -1:
            result.extend(self.inOrderRecursive(self.left[start]))
        result.extend([self.key[start]])
        if self.right[start] != -1:
            result.extend(self.inOrderRecursive(self.right[start]))

        return result

    def preOrderRecursive(self, start=0):
        result = []

        result.extend([self.key[start]])
        if self.left[start] != -1:
            result.extend(self.preOrderRecursive(self.left[start]))
        if self.right[start] != -1:
            result.extend(self.preOrderRecursive(self.right[start]))

        return result

    def postOrderRecursive(self, start=0):
        result = []

        if self.left[start] != -1:
            result.extend(self.postOrderRecursive(self.left[start]))
        if self.right[start] != -1:
            result.extend(self.postOrderRecursive(self.right[start]))
        result.extend([self.key[start]])

        return result

    def inOrderNonrecUgly(self):
        my_left = self.left.copy()
        my_right = self.right.copy()
        stack = deque()
        results = []
        stack.append(0)
        while stack:
            node = stack.pop()
            if my_right[node] == -1 and my_left[node] == -1:
                results.append(self.key[node])
                continue
            if my_right[node] != -1:
                stack.append(my_right[node])
                my_right[node] = -1  # we now already processed the right arm
            stack.append(node)
            if my_left[node] != -1:
                stack.append(my_left[node])
                my_left[node] = -1
        return results

    def inOrder(self):
        """From https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
        """

        stack = deque()
        results = []
        current_node = 0

        while True:
            while current_node != -1:
                stack.append(current_node)
                current_node = self.left[current_node]

            item = stack.pop()
            results.append(self.key[item])
            current_node = self.right[item]

            if not stack and current_node == -1:
                break

        return results

    def preOrder(self):
        stack = deque()
        stack.append(0)
        while stack:
            node = stack.pop()
            yield self.key[node]
            if self.right[node] != -1:
                stack.append(self.right[node])
            if self.left[node] != -1:
                stack.append(self.left[node])

    def postOrderMine(self):
        """My implementation, but not the prettiest"""
        my_left = self.left.copy()
        my_right = self.right.copy()
        stack = deque()
        results = []
        stack.append(0)
        while stack:
            node = stack.pop()
            if my_right[node] == -1 and my_left[node] == -1:
                results.append(self.key[node])
                continue
            stack.append(node)
            if my_right[node] != -1:
                stack.append(my_right[node])
                my_right[node] = -1  # we now already processed the right arm
            if my_left[node] != -1:
                stack.append(my_left[node])
                my_left[node] = -1
        return results

    def postOrder(self):
        """From https://www.geeksforgeeks.org/iterative-postorder-traversal/"""
        pass


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


if __name__=='__main__':
    threading.Thread(target=main).start()
