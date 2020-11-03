### Week 1 - Programming Challenges

- Often, to find the key algorithm, you need to know something interesting about
  the problem. Example: Knowing about the key lemmma for Euclidean Algorithm to
  efficiently compute the Greatest Common Divisor (in Week 1).

### Week 2 - Algorithmic Warm-up

- You can't teach a generic procedure for designing goog algorithms.
- But: You can
  - practice designing algorithms
  - learn common algorithmic design techniques. We'll look at:
    - Greedy algorithms
    - Divide and Conquer
    - Dynamic Programming


- Levels of Design
  - **Naive Algorithm**: Often just typing out the definition of the
    algorithm. Slow.
  - **Algorithm with standard tools**: E.g. by using a greedy algorithm
  - **Optimized algorithm**: Improve the existing algo. E.g. by rearranging
    steps or by introducing a specific **data structure**
  - **Magic algorithm**: But sometimes you need some unique insight, a clever
    new idea, sometimes no one else had that before you.

### Week 3 - Greedy Algorithms

- Greedy: Take the first, greediest option, then reduce your problem by one step
  to a new **subproblem**. Take the greediest option again etc.  until you're
  done.
  - The subproblem thing suggests recursion!
- You have to prove that your greedy choice is a *safe move*, i.e. consistent
  with an optimal solution.

- Largest number problem:
  - Concatenate the following numbers so that the largest possible integer comes
	out:
  
	  5, 52, 57, 517, 532, 569, 581
  
    Result:
  
	  581 57 569 5 532 52 517

### Week 4 - Divide-and-Conquer

- Divide and conquer often leads to recursive implementations,
  but you can always program an iterative loop as well, especially
  if recursion goes to deep and the stack trace becomes too long
- Linear search vs. Binary search:
  - Binary search is O(log n), but requires a sorted array.
- Polynomial Multiplication
  - many applications in IT: error-correcting codes, convolution in signal
    processing, etc.
  - multiplying thousand-digit integers works quicker using this tactic
  - Use it to multiply large numbers by building a polynomial and setting x=10,
    duh!
  - The Karatsuba algorithm is O(n^1.58)


##### The Master Theorem

  - Transforms a **recurrence tree** into an O(..) runtime:

```
If T(n) = a * T( ceil(n/b) ) + O(n^d), then

T(n) = O(n^d),          if d > log_b(a)
       O(n^d * log(n)), if d = log_b(a)
       O(n^(log_b a)),  if d < log_b(a)
```	

  - Examples: 
    - Binary search:
      - T(n) = 1*T(n/2) + O(1)
      - T(n) = O(log n)
    - Polynomial multiplication, naive algorithm:
      - T(n) = 4*T(n/2) + O(n)
      - T(n) = O(n^2)
    - Polynomial multiplication, Karatsuba algorithm:
      - T(n) = 3*T(n/2) + O(n)
      - T(n) = O(n^(log_2 3)) ~= O(n^1.5)

##### Sorting

- **Selection Sort**
  - Scan for minimum, swap it with leftmost element
  - Do same for elements 2...n
- Runs in O(n^2)
  - Even if the inner loop's iterations decrease. It's actually n^2 / 2, 
    because of the arithmetic series n(n+1)/2, but constants don't matter
- Selection Sort's running time does not depend on input data order
  - Check it out on https://www.toptal.com/developers/sorting-algorithms

- **Merge Sort**
  - Is a divide-and-conquer based algorithm
  - Running time: O(n logn)

- The optimal running time for any **comparison-based** sorting algorithm
  (i.e. that sorts objects by comparing pairs of them) is O(n log n)
- **Non-comparison based sorting algorithms**
  - **Counting Sort**
    - e.g. for small integers: Just create a frequency table and roll it out!
    - O(n+m), usually O(n)
    - Key: **one can do better than O(n log n) if soumething about the input
      array is known in advance (e.g. it contains small integers)**
    - It doesn't work if you have to sort *real* numbers instead of integers,
      because you'd need an infinite amount of buckets

- **Quick Sort**
  - Is O(n log n) *on average*. Merge Sort was O(n log n) *worst case*
  - Still, it's very efficient.
  - Worst case, if you partition always into 2 parts of size (1, n-1), quicksort
    is O(n^2)

### Week 5 - Dynamic Programming 1

### Week 6 - Dynamic Programming 2
