# Course 1 - Algorithmic Toolbox

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

- DP is nice if greedy algorithms don't work (e.g. in the Change Problem below)
- And if a recursive solution (e.g. Fibonacci recursively) takes forever.
- Simply: DP's key idea is to avoid recomputing the same thing again.
- The difference between DP and Div-and-Conq is that in Div-and-Conq the
  subproblems are disjoint, whereas in DP they are overlapping.


- The crucial part in DP is to come up with the right notion of a subproblem and
  a recurrence relation.
- You can also just implement a brute force solution, then optimize it

##### Change Problem

- How to change $5 when you buy coffee for $1.49?
  - Find the *minimum* number of coins
- **Greedy change**: Add the largest denomination coin that doesn't exceed the
  remaining amount.
  - **But**: This fails if you need 40ct, and have coins of 100, 50, 25, 20, 10,
    5, 1. Because greedy would yield 25+10+5, while 20+20 would be better.
- **Recursive change**: Create n_coins subproblems, one for each coin
  denomination: The result is the minimum of those, plus 1 coin.
  - It's guaranteed to find the best value, but a slow algorithm: For amount=76
    and coins=1,5,6, the recursive tree will contain three repetitions of
    changing 70ct, but *trillions* of repetitions of changing 30ct.
	- Caching/Memoization would solve this.
- **Dynamic Programming**: By Richard Bellman 1953. Don't fill recursive calls
  from top to bottom, but instead bottom-up!

##### Two Rocks Game

- Two piles of ten rocks each
- Opponent starts: Moves are: Take one rock from left, take one rock from right,
  or take one rock from both.
- How do you win?
- Dynamic Programming: Bottom-up: I win if I leave my opponent with two rocks in
  each pile. I therefore also win if I leave him with four rocks per pile. Also
  with (6, 6), (8, 8), and (10, 10). And also with (4, 6) or (4, 8) etc.

##### String Comparison

- 1980s: The hunt for the gene responsible for Cystic Fibrosis in a 1mil bp
  region on chromosome 7.
- It was found by comparing strings: The known sequence of a gene with a similar
  function was compared with the 1Mbp region
- **The Alignment Game**. How to align two gene sequences
- **Edit Distance**: Find the minimum number of insertions, deletions, and
  mismatches to get two strings to be equal.
  - example: EDITING and DISTANCE into 4 matches, 2 mismatches, 2 ins, 1 del
    - EDI-TING-
    - -DISTANCE
- Maximizing the alignment game is identical to minimizing the edit distance
- Dynamic Programming:
  - Compute the min edit distance from the substrings A[0:i] and B[0:i].
  - The last column of an optimal alignment is either ins, del, mis, or match
  - If you remove this last column, you're left with an optimal alignment of the
    two substrings of A and B
- Let D(i, j) be the edit distance of A[:i] and B[:j]
  - Then D(i, j) equals the minimum of
    - D(i, j-1) + 1  # insertion
    - D(i-1, j) + 1  # deletion
    - D(i-1, j-1) + 1  if A[i] != B[j]  # mismatch
    - D(i-1, j-1)   if A[i] == B[j]  # match
- Draw a 8x9 grid to draw the optimal path for the edit distance between EDITING
  and DISTANCE
- You can then compute the edit distance. But you don't know the optimal
  alignment yet. You have to beacktrack the path for that. A diagonal move means
  [mis-]match, and a horizontal/vertical jump means insertion/deletion.

### Week 6 - Dynamic Programming 2

##### Knapsack

- Remember: Fractional knapsack can be done with a greedy algorithm

- **Knapsack with Repetitions**
  - The subproblems are (i) overlapping and (ii) each are optimal solutions.
  - Those are the two prerequisites for using DP.
  - value(w) = max_{i: w_i <= w} (value(w-w_i) + v_i)

- **Knapsack without Repetitions**
  - When each item can only be used once, the above algo doesn't work
  - because the subproblem may not be optimal anymore
  - You need 2dimensional looping in the subproblems now: Not only w=1,...,W,
    but also i=0,...n (the number of available items)
- The algo is fun, but google it.
- Reconstructing the solution (which items are used?) from the final value
  matrix is tricky but cool!

- **Running time**: I didn't understand the reasoning, but the running time is
  exponential (or maybe pseudo-polynomial), not polynomial. It's O(n * 2^(log
  W))
  - https://stackoverflow.com/questions/4538581/why-is-the-knapsack-problem-pseudo-polynomial#answer-4538668
  - Solve this knapsack in polynomial time, you get $1M :)

- **[Memoized] Recursive (top-down) or iterative (bottom-up)?**
  - If all subproblems must be solved anyway, then iterative is usually faster
    since it has no recursion overhead (storing return addresses on the stack
    etc.).
  - But when e.g. all weights are multiples of 100, then you don't need to solve
    subproblems of w%100 != 0.

##### Placing Parentheses

- Input: An arithmetic expression. 1+2-3*4-5
  - Find parentheses (i.e. an execution order) so the result is maximal
- Naive solution is O(n!), a DP solution is O(n^3)
