from collections import deque
import sys


class StackWithMaxNaive():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return max(self.__stack)


class StackWithMax():
    def __init__(self):
        self.stack = deque()
        self.max_stack = deque()

    def Push(self, a):
        self.stack.append(a)
        if not self.max_stack or a >= self.max_stack[-1]:  # must be __geq__, because we can have duplicate maxima, then keep previous ones!
            self.max_stack.append(a)

    def Pop(self):
        last = self.stack.pop()
        if self.max_stack and last == self.max_stack[-1]:
            self.max_stack.pop()

    def Max(self):
        return self.max_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert 0
