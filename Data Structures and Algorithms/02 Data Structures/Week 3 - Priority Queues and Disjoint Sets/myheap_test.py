from myheap import Heap

h = Heap(max_size=16, elements=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])
h.print_contents()

h.sift_up(15)
print("\n\n")
h.print_contents()

h.sift_down(2)
print("\n\n")
h.print_contents()