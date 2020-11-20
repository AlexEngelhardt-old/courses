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

##### Introduction, Direct Addressing and Chaining

- Examples
  - Python's `dict`
  - keywords of a programming language (for, if, while) to highlight it
    are often stored in a hash table
  - File systems: The mapping from path+file to the physical location
  - Password hashes, using special cryptographic hash functions
  - Storage optimization, e.g. for Dropbox storing duplicate files

- Web Service
  - hosts with different 32-bit IPv4 addresses access it
    - IPv6 uses 128-bit
  - You want to defend against DOS attacks by analyzing access logs:
    datetime, IP address
  - 1h of log file can contain millions of lines
    - so keep **count**: how many times each IP appears in the last 1h of logs
	  - increment the counts for "now", decrement it for those that will now be
        more than 1h ago
	- **Use a data structure C (like Python's dict) to map IP to counters**

```
# i counts the first not-yet-processed row in the logfile
# j counts the first row in the current 1h-spanning window
# each second, we'll increase the 1h-counter for each new log, and decrease it
#   for each now-deprecated log

while log[i].time <= now():
    C[log[i].IP] += 1
    i += 1
while log[j].time <= now()-3600sec:
    C[log[j].IP] -= 1
    j += 1
```

- **Direct Addressing**
  - How to implement a O(1) access data structure `C`?
  - Surely not with a size 2^32 array :)
    - Access and update would be O(1), but you need 2^32 memory cells. IPv6
      wouldn't work anymore
- **List-based mapping**
  - Storing all IPs in a list (multiple times if it accessed the website
    multiple times) solves the memory problem, but now searching for an IP and
    counting accesses is O(n)
- **Hash Functions** solve the two drawbacks mentioned above
  - A hash function h encodes *any* object from a set S into a "small" integer
    <= m (m is called the **cardinality** of a hash function h)
    - h should be fast to compute
    - We want different values for different objects
	  - impossible for |S| > m
    - We want direct addressing with O(m) memory
  - A **map** from S to V is a data structure with methods:
    - `HasKey(s)`
    - `Get(s)`
    - `Set(s, v)`
  - A **collision** is when two objects result in the same hash
    - Solve collisions via **chaining**: Combine direct addressing and
      list-based mapping
      - Each possible hash value gets a *chain* of hashed IPs
      - Then `HasKey` is implemented by running through the (entire!) respective
        hash's list
    - Memory consumption is O(n+m) for n elements and hash cardinality m
    - Time consumption is O(c+1), c is length of longest sublist
    - **Goal**: make both m and c small, by using a clever hash function

- A **Set** is a data structure with methods
  - `Add(o)`
  - `Remove(o)`
  - `Find(o)`
- Implement a set like a *map*, but store just the keys, no values

- A **hash table** is an implementation of a set or map using hashing

##### Hash Functions

- The speed of a Hash Table depends a lot on the choice of hash function
- **Phone book problem**
  - add and delete contacts
  - look up name given phone#
  - look up phone# given name
- You need **two maps**. name->number and number->name


- `n` phone numbers stored
- `m` - cardinality of hash function
- `c` - length of the longest chain
- `O(n+m)` memory is used
- `alpha = n/m` is called the *load factor*: How "filled up" is the hash table?
  - You want alpha to be between 0.5 and 1. So on average, each hash value
    should contain at most 1 element!
- We want small m and small c


- **Dynamic Hash Tables**, if you don't know the number of keys in advance
  - Copy the idea of dynamic arrays! Start with a **small hash table**, then
    increase it as soon as alpha becomes too large
	- That requires a *re-hash*, a new hash function with twice the cardinality
	  - Remember, the *amortized* runtime of that move is O(1)


- **Universal Family**: A set of hash functions where the probability of
  collision for two distinct elements is < 1/m
    - "Probability" taken over a random choice from the hash function family
- Choose your hash function h **randomly** from the universal family H
  - Do that random choice only once, at the beginning, woah?
- **Hashing integers**
  - A universal family for hashing integers efficiently:
  - hash phone numbers up to length 7
  - Choose prime number p larget than 10^7, e.g. p=10 000 019
  - Choose hash table size, e.g. m=1 000
  - Lemma: This hash family is a universal family:
    h(x) = ((ax + b) mod p) mod m
    for a and b from 0 (bzw. 1) to p-1,
	x must be < p; otherwise there exists x and y s.t. *any* hash function of
    the family has a colision
- **Hashing strings**
  - we should use *all* characters to avoid collisions
  - convert each char to an int, and a big prime number p
  - Define **polynomial hash functions**
    - Probability of collision is at most L/p, where L is the max string length
	  - shorter strings => less collision probability!!!
      - runtime: O(L), doesn't depend on p
      - it's important to know and use *large* prime numbers p
    - Their cardinality is p-1. Fix it to m by integer hashing the resulting hash :)
	  - Then the collision probability is at most 1/m + L/p
        - That's *not a universal family* because the prob is > 1/m. *But* we
          can choose a huge p (p > mL) so that the probability is < 2/m, i.e. O(1/m)


##### Searching Patterns

- Given a text T and a pattern P, find all occurrences of P in T
- Define substring notation: S="abcde", then S[0..4] = "abcde", S[1..3] = "bcd",
  S[2..2] = "c"
- **Find pattern in text**
  - Input: Strings T and P
  - Output: All positions i in T, s.t. T[i .. i+|P|-1] = P
  - Naive algo running time is O(|T| * |P|)
  - **Rabin-Karp Algorithm** is faster by using hashing
    - Note: If h(P) != h(S), then *definitely* P != S
      - If h(P) == h(S), then *maybe* P == S. And *only then* call the expensive
        function `StringsAreEqual(P, S)`
    - Hash all of T's substrings of length |P|. If the hashes are equal, then
      check if the strings are equal.
    - The prob. of a "false alarm" can be made small by choosing a large p >> |T|*|Þ|
    - Right now, this is still `O(|T|*|P|)`. We'll improve it by 
	- *Precomputing all hashes in a recurrent manner (from back to front)*:
    - Idea: The polynomial hashes of two consecutive substrings of T are very
      similar. One, given the other, can be computed in constant time:
      - H[i] = x * H[i+1] + stuff mod p
    - Now we're `O(|T| + |P|)`, woo hoo!

##### Distributed Hash Tables (optional)

- **Applications for hashes**
  - Strings, texts, pattern matching
  - Data Science (huh!!)
  - *Distributed systems (this lesson)*
- Dropbox stores file copies just once:
  - Compare hashes of newly to-be-uploaded file
  - If there's something equal, compare files byte-by-byte, and if equal, don't
    upload, just store a link
  - Compute *multiple* different hash functions. If they're all equal, don't
    even compare the file byte-by-byte, but assume the files are equal :)


- **Big Data**
- Problem: Billions of files uploaded daily, trillions of files stored
- Too big for a simple hash table
- Solution
  - Get 1000 computers
  - Create a hash table on each of them
  - Computer i owns the object `h(object) mod 1000 == i`
  - Store several copies of the data to defend against computers breaking
  - Use **Consistent Hashing** now.

### Week 5 - Binary Search Trees

### Week 6 - Binary Search Trees 2
