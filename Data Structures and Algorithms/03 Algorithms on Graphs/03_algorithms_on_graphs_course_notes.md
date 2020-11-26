# Course 3 - Algorithms on Graphs

- Graphs:
  - Webpages connected by links
  - Computer networks
  - Social networks
  - Maps, e.g. navigation systems
  - Robot arms: Configurations/positions connected to each other by certain
    motions
	- (that's a lot like a (mathematical) group, right?)

# Week 1 - Decomposition of Graphs 1 (Undirected Graphs)

### Graph Basics

- A graph is a collection V of vertices, connected by a set of edges E
- Example: V = (A, B, C, D), Edges: (A, B), (B, D)
- A **loop** connects an edge to itself
- Sometimes two vertices can have multiple edges

- **Operations we want to implement**
  - `Is Edge?` - Is there an edge between vertex A and C?
  - `List Edge` - List all edges in the graph
  - `List Neighbors` - List all neighbors of a given vertex

- **Representing Graphs**
  - Multiple ways, each effecting the runtime. Depends on: is it a sparse or
    dense graph?
  - **Adjacency Matrix, where Entry is 1 if there is an edge, and 0 else.**
    - Is Edge? - O(1)
    - List Edge - O(|V|^2)
    - List Neighbors - O(|V|)
  - **Just store a list of all edges**
    - Is Edge? - O(|E|)
    - List Edge - O(|E|)
    - List Neighbors - O(|E|)
  - **Adjacency List: For each vertex, store a list of its connected vertices**
    - Is Edge? - O(deg) (the degree of the vertex: its number of neighbors)
    - List Edge - O(|E|)
    - List Neighbors - O(deg)

- **Runtimes**
  - depend on |V| and |E|, e.g. O(|V| + |E|) or O(|V| log |V| + |E|)
  - Which is faster? O(|V|^3/2) or O(|E|) ?
    - Depends on the **density** of the graph.
	  - Dense graph, e.g. routes between cities: |E| \approx |V|^2
      - Sparse graph, e.g. webpage links: |E| \approx |V|

### Exploring Undirected Graphs

- **Exploring**: Find everything in a "computer level", e.g. a maze, represented
  as a graph.
  - Finding routes
  - Ensuring connectivity between all vertices
  - Solving puzzles and mazes: Can I get from the start to the finish?

- A **path** is a sequence of *vertices* (not edges) s.t. for all i, `(v_i,
  v_i+1)` is an edge of G

- Basic idea: Explore every edge leaving every vertex you know
  - How to keep track of which vertices you know and which edges are still TODO?
  - Which order do you explore new edges in?
    - **Depth First**: Follow a long path forward, only backtracking when you
      hit a dead end or reach an already known vertex

- Depth first is super easy to implement recursively:
```
def explore(v):
	visited[v] = True
	for (v, w) in Edges:
		if not visited(w):
			explore(w)
```
- Need the Adjacency list representation for this algo

- **Depth First Search** can also discover **all** vertices in a graph G, not
  just the ones reachable from vertex v.
  - Just "pick" a new unvisited vertex if your `explore(v)` call finishes.
  - Total runtime: O(1) per vertex + O(1) per edge = O(|V| + |E|)

- **Connectivity** in an undirected graph
  - Partition it into **connected components** so that all nodes in a CC
    ("island") are reachable
  - Reachability is an **equivalence relation**:
    - v = v
    - if v=w then w=v
    - if v=u and v=w then u=w
- How to find all connected components?
  - Each `explore(v)` finds one complete island
  - Modify DFS to label CCs with different IDs

```
def DFS(G):
	for all v: mark v unvisited
	cc = 1  # island's ID
	for v in V:
		if not visited(v):
			explore(v)
			cc = cc + 1
```

- **Previsit and Postvisit Orderings**
  - The preorder and postorder numbers will be useful in later algorithms
  - Augment some functions to store additional information:

```
def explore(v):
	visited[v] = True
	previsit(v)
	for (v, w) in Edges:
		if not visited(w):
			explore(w)
	postvisit(v)

def previsit(v):  # same for postvisit
	pre(v) = clock
	clock = clock + 1
```

  - **Clock**
    - it ticks at each call to previsit and postvisit
    - record the time for each vertex's previsit **and postvisit** times.
  - Lemma: For any two vertices u and v, the pre(v) and post(v) times are
    **either nested or disjoint** (i.e. not interleaved).

# Week 2 - Decomposition of Graphs 2 (Directed Graphs)

# Week 3 - Paths in Graphs 1

# Week 4 - Paths in Graphs 2

# Week 5 - Minimum Spanning Trees

# Week 6 - Advanced Shortest Paths Project
