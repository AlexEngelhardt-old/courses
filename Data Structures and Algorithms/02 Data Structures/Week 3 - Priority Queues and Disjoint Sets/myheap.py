class Heap:
    """Priority Queue implemented as a Binary Max Heap.

    It's cool because
      - fast: all operations in O(log n)
      - space efficient: tree is stored implicitly as an array. We compute (not store) the child and parent indices
      - easy to implement: each operation is just a few lines of code
    """

    def __init__(self, max_size, elements=None):
        self.max_size = max_size
        self.elements = [0] * max_size  # TODO even better would be an automatically-resizing dynamic array
        if elements:
            if len(elements) > max_size:
                raise ValueError('Number of elements is larger than max_size')
            self.elements[:len(elements)] = elements
        self.size = len(elements)

    def print_contents(self):
        for i in range(self.size):
            if not ((i+1) & i):  # if i+1 is a power of two, print a newline
                print()
            print(self.elements[i], end=" ")

    def has_left_child(self, i):
        return 2 * i + 1 <= self.size

    def has_right_child(self, i):
        return 2 * i + 2 <= self.size

    def get_left_child(self, i):
        if self.has_left_child(i):
            return 2*i + 1
        else:
            raise IndexError('Node has no left child')

    def get_right_child(self, i):
        if self.has_right_child(i):
            return 2*i + 2
        else:
            raise IndexError('Node has no right child')

    def get_parent(self, i):
        if i == 0:
            raise IndexError('Root node has no parent')
        return (i-1) // 2

    def sift_up(self, i):
        while i > 0 and self.elements[i] > self.elements[self.get_parent(i)]:
            self.elements[i], self.elements[self.get_parent(i)] = self.elements[self.get_parent(i)], self.elements[i]
            i = self.get_parent(i)

    def sift_down(self, i):
        max_index = i
        if self.has_left_child(i):
            if self.elements[self.get_left_child(i)] > self.elements[max_index]:
                max_index = self.get_left_child(i)
        if self.has_right_child(i):
            if self.elements[self.get_right_child(i)] > self.elements[max_index]:
                max_index = self.get_right_child(i)
        if i != max_index:
            self.elements[i], self.elements[max_index] = self.elements[max_index], self.elements[i]
            self.sift_down(max_index)

    def insert(self, value):
        if self.size == self.max_size:
            raise Exception('Heap is full. TODO: Implement a dynamic array and a resize operation.')
        self.elements[self.size] = value
        self.sift_up(self.size)
        self.size += 1

    def extract_max(self):
        res = self.elements[0]
        self.elements[0], self.elements[self.size - 1] = self.elements[self.size-1], self.elements[0]
        self.sift_down(0)
        # elements[size] still contains a value, but we'll ignore it because we shrink size:
        self.size -= 1
        return res

    def remove(self, i):
        self.elements[i] = float('inf')
        self.sift_up(i)
        self.extract_max()

    def change_priority(self, i, new_value):
        old_value = self.elements[i]
        self.elements[i] = new_value
        if new_value < old_value:
            self.sift_down(i)
        else:
            self.sift_up(i)
