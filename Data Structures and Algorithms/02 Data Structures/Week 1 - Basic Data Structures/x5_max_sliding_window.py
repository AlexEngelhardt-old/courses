from collections import deque


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


class QueueWithMax:
    """To be able to use the linear-time max() operation from exercise 4, we need to use stacks.
    Fortunately we can implement a queue using two stacks:
    https://www.geeksforgeeks.org/queue-using-stacks/

    Bad tho: I think this makes the complexity O(n*m) again, worst case at least(?)
    """
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()
        self.max_stack1 = deque()
        self.max_stack2 = deque()

    def enqueue(self, a):
        self.stack1.append(a)
        if not self.max_stack1 or a >= self.max_stack1[-1]:  # must be __geq__, because we can have duplicate maxima, then keep previous ones!
            self.max_stack1.append(a)

    def dequeue(self):
        if not self.stack1 and not self.stack2:
            raise IndexError("Queue is empty")
        if not self.stack2:
            while self.stack1:
                a = self.stack1.pop()
                self.stack2.append(a)
                if not self.max_stack2 or a >= self.max_stack2[-1]:
                    self.max_stack2.append(a)
            self.max_stack1.clear()
        last = self.stack2.pop()
        if self.max_stack2 and last == self.max_stack2[-1]:
            self.max_stack2.pop()

    def max(self):
        if not self.max_stack1:
            return self.max_stack2[-1]
        elif not self.max_stack2:
            return self.max_stack1[-1]
        else:
            return max(self.max_stack1[-1], self.max_stack2[-1])


def max_sliding_window(sequence, m):
    q = QueueWithMax()
    for i, x_i in enumerate(sequence):
        q.enqueue(x_i)
        if (i+1) > m:
            q.dequeue()
        if (i+1) >= m:  # if first 4 elements are processed
            yield q.max()


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))

