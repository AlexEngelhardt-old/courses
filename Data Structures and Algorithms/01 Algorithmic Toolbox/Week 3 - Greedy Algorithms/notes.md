# Greedy Algorithms

- Greedy: Take the first, greediest option, then reduce your problem by one step
  to a new **subproblem**. Take the greediest option again etc.  until you're
  done.
  - The subproblem thing suggests recursion!
- You have to prove that your greedy choice is a *safe move*, i.e. consistent
  with an optimal solution.

## Largest number

- Concatenate the following numbers so that the largest possible integer comes
  out:
  
  5, 52, 57, 517, 532, 569, 581

  Result:

  581 57 569 5 532 52 517
