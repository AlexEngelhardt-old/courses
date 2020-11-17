# Course 2 - Data Structures

A few examples of questions that we are going to cover in this class are the following:

1. What is a good strategy of resizing a dynamic array?
2. How priority queues are implemented in C++, Java, and Python?
3. How to implement a hash table so that the amortized running time of all
   operations is O(1) on average?
4. What are good strategies to keep a binary tree balanced?

### Week 1 - Basic Data Structures

##### Arrays and Linked Lists

- Array: 3 things are important:
  - Contiguous area of memory, either on the stack or the heap
  - Equal-size elements
  - indexed by contiguous integers
- **Advantage** We have *constant-time access* to read and write each element
  - So we can do arithmetic to find the address of a particular element:
    `elem_addr = array_addr + elem_size * i` (for 0-based indexing)
- Multi-dimensional arrays work similarly. There's row-major and column-major
  indexing, though
- **Disadvantage (over linked lists)**: Adding or removing items at the
  beginning or in the middle is O(n), because you have to move many other items
  up or down by one.
  - Adding/removing at the end is constant-time though.


- (Singly) Linked Lists: Nodes with properties `key` (the content) and `next` (pointer to
  next element)
  - A list also contains a `head` pointer that points to the first element.
- Operations that are provided:
  - O(1):
    - prepend key to front of list
    - return first item
    - pop (remove and return) first item
    - add a key **after** a given node (i.e. you have its address)
  - O(n):
    - Append to end of list (if you have no `tail` pointer; else, it's O(1))
    - return last item
    - pop last item (even *with* `tail` pointer, because you need to update it)
    - find item
    - erase item
    - add a key **before** a given node


- Doubly Linked Lists
  - A node now has a "previous" pointer
  - makes "pop from back" and "add before node" O(1)
  - Updating nodes is a bit messier, but still relatively easy.


- Advantage of Linked Lists over Arrays:
  - Inserting at the front is O(1), not O(n), because you don't have to move the
    other elemnts
  - List elements don't have to be contiguous in memory

##### Stacks and Queues

- **Stack**: You can only operate on its top
- Stack API
  - Push(key): Add key to collection
  - Top(): Return newest key
  - Pop(): Remove (and return?) newest key
- Nice: *every* operation is O(1)
- Use cases:
  - Find if a string's parentheses and brackets are balanced: ([bad((abc)d)f()f]aa)
  - A **call stack**, e.g. in recursive functions, works similarly
- Implement a stack
  - with an array
    - then you need a *maximum* stack size
	- You can get errors when pushing into a full array
	- you might also waste space with a large allocation
  - with a singly linked list
    - push, top and pop should update the *first* element, not the last
	- you have some overhead because storing the pointers to next elements


- **Queue**: Like a shopping queue, FIFO (first come, first serve)
  - A stack is a LIFO queue
- Queue API:
  - enqueue(key): Add key to collection
  - dequeue(): Remove and return the oldest key
- Good for servers etc., you want to service the longest waiting dude
- Implement a queue
  - with a linked list (needs a tail pointer though)
    - enqueue(a): push to the back, List.PushBack()
    - dequeue(): pop *from the front*
  - with an array
    - you can make dequeuing from O(n) (because of rearranging remaining items)
      to O(1) by using a *circular* array. Keep `start` and `end` pointers. If
      they're equal, the queue is empty.

##### Trees

- e.g. a Syntax Tree for a sentence, or for an expression 2*sin(3z - 7)
  - *hmmm, parsing this expression creates the tree top-down, and computing a
    result would resolve the tree bottom up, right?!*
- hierarchies like geographical, or animal kingdom
- **Code is interpreted as an abstract syntax tree**
    while x < 0:
	    x = x + 2
        foo(x)

The corresponding tree:

- while
  - compare_op: <
    - var: x
    - const: 0
  - block
    - assign
	  - var: x
      - binop: +
        - var: x
        - const: 2
    - procedure_call
	  - var: foo
      - var: x

- **Binary Search Tree**
  - A *binary* tree has at most 2 children per node
  - In a BST, the root node's value is >= all nodes to its left, and <= all
    nodes to its right
	- That makes searching very quick
    - (?) So you can insert items in O(log n), right? And the result stays "sorted"!
- A tree is defined as a node with
  - A content (key)
  - A list of child trees
  - (optional) a pointer to its parent node
- A binary tree has the left and right children in there explicitly:
  - key
  - left
  - right
  - (optional) parent
- A node's *level* is 1 for root node, and +1 for each generation down
  - A node's *height* is the inverse: leaf nodes have height 1, the root node is highest.
- Tree procedures are often implemented recursively
  - height(tree) = 1 + max(height(tree.left), height(tree.right))


- **Tree Traversal**
  - visit all nodes in a specific order
    - *Depth-first (search)*: Walk down one subtree before exploring a sibling subtree
	  - Simple recursive algo: dfs(tree) = 1. dfs(left), 2. print(tree.key), 3. dfs(right)
      - Nice: This **In-order traversal** prints a BFS in alphabetical order!
        (left-deepest element comes first) (it must be a _binary_ tree though,
        because otherwise it's not clear where to put print(tree.key))
      - A **Pre-order traversal** prints the tree.key first, and only then walks
        through the children. This also works for non-binary trees.
      - A **Post-order traversal** puts the tree.key after all children
		- Post-order traversal works for parsing math expressions: (1+2) * (3-6)
    - *Breadth-first (search)*: Traverse all nodes at one level before going to the next
	  - aka. **Level traversal**
	  - Here we use a queue instead of a stack (as done for DFS). Also, this
        walk is not done recursively but iteratively (while queue not empty).
      - That way you can print level 1 (the root node), then all level 2, then
        all level 3, etc


### Week 2 - Dynamic Arrays and Amortized Analysis

- static array bad b/c size predetermined: `int arr[100];`
  - (Python has no static arrays, the `list` is dynamic)
- semi-solution: a dynamically allocated array:
  - `int *arr = new int[size]`
  - Allocate size at runtime, not compile-time
  - Bad: Size requirements can still grow at runtime

- **Fundamental Theorem of SW Engineering**: "We can solve any problem by
  introducing an extra level of indirection."
  - Here that "extra level of indirection" means another pointer, i.e. another
    layer of abstraction
- Dynamic arrays use this by storing a pointer to a dynamically allocated array,
  replacing it with a newly-allocated array as needed (you have to copy the old
  contents over in that case)
  - If you double the size at each resize, there can be at most 1/2 of the space
    wasted
- A DAA has at least the operations:
  - `get(i)`, i.e. random access, and at constant time O(1)
  - `set(i, val)` at constant time
  - `append(val)` is O(n) worst case (if you have to move and extend)
  - `remove(i)` is O(n)
  - `length()` is O(1)
- To implement, we must store
  - `arr`, the elements themselves
  - `capacity`, the max length of the array
  - `size`, the current length


- **Amortized Analysis - Aggregate Method (a brute-force sum)**
  - The worst-case operation times the number of operations overstates the
    cost. E.g. appending to a dynamic array, you don't *always* resize
    it. Mostly O(1), sometimes O(n).
  - The *amortized* cost: `cost(n operations) / n`
  - The *amortized* cost of inserting in a dyn. arr is O(n)/n = O(1)
- **Amortized Analysis - Banker's Method**
  - Charge extra for each cheap operation
  - Save the extra charge as tokens in your data structure (only conceptually,
    not really)
  - e.g. insert into dyn. arr.: Charge 3 for each insertion: save 2 of them
    - at resize time: place one token on each element that needs moving
    - place also one token on the item capacity/n elements prior to it
- **Amortized Analysis - Physicist's Method**
  - Define a potential function, taking a state of the data structur and mapping
    it to an integer.
  - Store in it the potential to do future work.
  - etc. etc., it's too complex and the previous methods are enough I think :)


- You have to resize by a factor, not by a constant length. Otherwise the
  amortized cost is not O(1) anymore, but O(n).


### Week 3 - Priority Queues and Disjoint Sets

##### Priority Queues

- Python: `heapq` (C++: `priority_queue`, Java: `PriorityQueue`)
- Store it as a binary tree (store *that* as an array)
- PQ: A generalization of a queue (with `PushBack` and `PopFront` operations)
  - A PQ has no beginning or end. You just have a *bag* of elements, but each
    element has a priority
  - Operations: `Insert(p)` and `ExtractMax` (get the elem with current max
    priority)
	- and maybe: `Remove(it)`, `GetMax()` (return without removing),
      `ChangePriority(it, p)`


- **Algorithms that use Priority Queues**
  - Dijkstra's algorithm: finding a shortest path in a graph
  - Prim's algorithm: Constructing a minimum spanning tree of a graph
  - Huffman's algorithm: constructing an optimum prefix-free encoding of a
    string (e.g. used in MP3 encoding)
  - Heap sort: sorting a given sequence
    - **This is good for *external* sorting, when the array doesn't fit into
      memory (then quicksort doesn't work)**
    - Also, quicksort has average O(n logn), and heapsort has *worst case* O(n
      logn). But usually, quicksort is faster.

- Naive implementation with an array: `Insert` takes O(1), `ExtractMax` is O(n)
  - You can use a sorted array, then `Insert` is O(n), and `ExtractMax` is O(1)

##### Priority Queues: Heaps

- With a **Binary Heap**, both `Insert` and `ExtractMax` can be done in O(log n)
- A **Binary max-heap** is a binary tree (i.e. each node has 0, 1, or 2
  children), where the value of each node is at least the values of its
  children.
- Operations on a BMH:
  - `GetMax` (without extracting it): Just return the root node, O(1)
  - `Insert`: Attach a new node to any *leaf*. Then sift that element up, swap
    it with its parents `while` the heap property is violated.
  - `ExtractMax`: Replace the root with any leaf (and remove that leaf). Then
    `SiftDown`: Swap the problematic node with its larger child until the heap
    property is satisfied again.
	- Running Time: O(tree height)
  - `ChangePriority`: Change the value of a node, then `SiftUp` or `SiftDown`
    that element until it's good.
  - `Remove`: change its priority to Infinity, then sift up, then `ExtractMax`
- Important in the Sift procedures: The heap property is always violated at at
  most 1 edge


- Because most operations are O(tree hight), we want trees to be *shallow*.
  - A **complete** binary tree has all levels fully packed (except maybe the
    last one, which you fill from left to right)
  - The height of a CBT with n nodes is minimal, and O(log n)
  - Second advantage: You can store a CBT as an array, because the indices can
    be clearly enumerated, and the relationships are clear:
	- parent(i) = floor(i/2)
    - leftchild(i) = 2i
    - rightchild(i) = 2i + 1
  - The only shape-shifting operations are `Insert`, `ExtractMax` (and `Remove`,
    but it's implemented using `ExtractMax`)
	- To `Insert`, put it in the shape-wise correct position, then let it
      `SiftUp` to a correct position.
    - To `ExtractMax`, replace the root with the *last leaf*, then let it
      `SiftDown`

##### Priority Queues: Heap Sort

- HeapSort:
  - Insert each element one after the other
  - Then `ExtractMax` until the heap is empty again
- It's a smart generalization of the O(n^2) selection sort:
  - Don't scan the array for the max value, but use a smart data structure
- Only disadvantage: It doesn't sort in-place, i.e. the heap uses additional
  space
  - Remedy in this lesson: In-place heap sort. Transform the array into a heap
    structure by permuting its elements.
- **Turn an array into a heap**
  - for i from floor(n/2) down to 1:
    - SiftDown(i)
- Then repeat n-1 times:
  - Swap A[1] and A[size]
  - size -= 1
  - SiftDown(1)

- Quicksort is usually faster, but quicksort has average O(n logn), and heapsort
  has worst case O(n logn)
- Also note: *Most* nodes are at the tree's bottom, i.e. SiftDown runtime is
  much less than log n.
  - So *building* the heap is actually O(2n) = O(n)
  - But the n-times `ExtractMax` leads to O(n logn) in total again
- But **partial sorting** (if k = O(n/logn)) can now be done in linear time,
  O(n + k log n):
  - BuildHeap() (in linear time)
  - ExtractMax() k times


- **Final remarks**
  - You can build a min-heap as well
  - In a d-ary heap, each node has exactly d children. Its height is log_d n,
    and sifting up runs in `O(log_d n)` then. But SiftDown is O(d * log_d n)
    then, because you need to compare d times.


##### Disjoint Sets: Naive Implementations

- Example: A maze. Is point B reachable from point A?


- A **disjoint set** data structure supports 3 operations:
  - `MakeSet(x)` creates a singleton set {x}
  - `Find(x)` returns the ID of the set containing x.
    - If x and y lie in the same set, Find(x) == Find(y)
  - `Union(x, y)` merges two sets containing x and y. They will have the same
    set ID then

- Solve your maze by assigning a set ID to each all-reachable region:
  - For each cell c in maze:
        MakeSet(c)
    For each cell c in maze:
        for each neighbor n of c not separated by a wall:
	        Union(c, n)

- Example: A computer network. Which computers are reachable from others?
  - Installing a new computer i: MakeSet(i)
  - Installing a cable between i and j: Union(i, j)
  - Is j reachable from i? Find(i) == Find(j)

- **Naive implementations**
  - **Arrays**: The smallest i in each set is its identifier
    - Have an array smallest[] that stores the smallest member's ID for each
      element of all sets
      - Problem: `Union(x, y)` is expensive, O(n).
  - **Linked lists**:  because merging two Linked Lists is cheap!
    - Treat the tail of a list as the corresponding set's ID
    - Then `Union` is O(1) too, you change only one pointer. But: You must store
      the pointer to `tail` of a list in each node
    - Disadvantage: `Find` is O(n) now

##### Disjoint Sets: Efficient Implementation

- Use **Trees**! ID of a set is the root of the tree
- When Union-ing two sets, don't point A's tail to B's head, but instead to B's
  *tail*. Then you have a tree.
- Use an array `parent`: `parent[i]` is its parent's ID, or `i` if i is the root

Then the operations can be implemented:

- `MakeSet(i)` just sets parent[i] = i
  - Running time: O(1)
- `Find(i)`:
  - while i != parent[i]
        i = parent[i]
    return i
  - Running time: O(tree height)
- `Union(x, y)`: *union by rank*
  - Just hang the shorter tree under the root of the longer (so the resulting
    tree is as shallow as possible): E.g. set root(y)'s parent to root(x)
	- Shallow trees make `Union` and `Find` in O(log n)
- To quickly find a tree's height, we keep it stored in an array:
  - rank[i] is the height of the *sub*tree whose root is i
  - Now we must append `MakeSet(i)`: set rank[i] = 0
    - and append `Union(i, j)`: The union only increases a subtree's height if
      both subtrees have the same rank. Then rank[j] += 1 

- **Path Compression** reduces the running time to nearly a constant!
  - When traversing the tree once to find a root, you also find the root of all
    nodes on the way.
	- Reattach *all nodes* found on the way directly under the root node.
    - The tree will become broad as fuck, but that's ok
  - Modify `Find(i)` thusly:
    if i != parent[i]:
	    parent[i] = Find(parent[i])  # attach node to root
    return parent[i]
  - The *iterated logarithm* `log* n`: How many times to log_2 something until
    it's less than 1?
	- That's a *very* slow growing function. It's <=5 for n <= 2^65536
    - So for all *practical* numbers, it's a "constant" operation.
	- The actual running time for m operations, including n calls to MakeSet, is
      O(m log* n)
      - The amortized running time of a single operation is O(log* n),
        i.e. *nearly* constant for n <= 2^65536
  - The rank array gets messed up, but that's okay (details in the Analysis
    video)

### Week 4 - Hash Tables

### Week 5 - Binary Search Trees

### Week 6 - Binary Search Trees 2
