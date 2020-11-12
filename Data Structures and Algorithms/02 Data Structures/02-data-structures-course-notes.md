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

### Week 3 - Priority Queues and Disjoint Sets

### Week 4 - Hash Tables

### Week 5 - Binary Search Trees

### Week 6 - Binary Search Trees 2
