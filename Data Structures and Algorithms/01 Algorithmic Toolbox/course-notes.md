### Week 1 - Programming Challenges

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

### Week 5 - Dynamic Programming 1

### Week 6 - Dynamic Programming 2
