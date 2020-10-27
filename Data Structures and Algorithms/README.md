# Data Structures and Algorithms

- Coursera's Data Structures and Algorithms Specialization
  - https://www.coursera.org/specializations/data-structures-algorithms?
- There's a companion book out:
  - http://learningalgorithms.tilda.ws
  - https://www.amazon.com/dp/0985731214
- Also nice, recommended as a prerequisite, is this course:
  - https://www.coursera.org/specializations/discrete-mathematics

### Notes

- Often, to find the key algorithm, you need to know something interesting about
  the problem. Example: Knowing about the key lemmma for Euclidean Algorithm to
  efficiently compute the Greatest Common Divisor (in Week 1).

### Contents

#### I - Algorithmic Toolbox

- Week 1 - Programming Challenges
- Week 2 - Algorithmic Warm-up
- Week 3 - Greedy Algorithms
- Week 4 - Divide-and-Conquer
- Week 5 - Dynamic Programming 1
- Week 6 - Dynamic Programming 2

#### II - Data Structures

- Week 1 - Basic Data Structures
- Week 2 - Dynamic Arrays and Amortized Analysis
- Week 3 - Priority Queues and Disjoint Sets
- Week 4 - Hash Tables
- Week 5 - Binary Search Trees
- Week 6 - Binary Search Trees 2

#### III - Algorithms on Graphs

- Week 1 - Decomposition of Graphs 1
- Week 2 - Decomposition of Graphs 2
- Week 3 - Paths in Graphs 1
- Week 4 - Paths in Graphs 2
- Week 5 - Minimum Spanning Trees
- Week 6 - Advanced Shortest Paths Project (Optional)

#### IV - Algorithms on Strings

- Week 1 - Suffix Trees
- Week 2 - Burrows-Wheeler Transform and Suffix Arrays
- Week 3 - Knuth–Morris–Pratt Algorithm
- Week 4 - Constructing Suffix Arrays and Suffix Trees

#### V - Advanced Algorithms and Complexity

- Week 1 - Flows in Networks
- Week 2 - Linear Programming
- Week 3 - NP-complete Problems
- Week 4 - Coping with NP-completeness
- Week 5 - Streaming Algorithms (Optional)

#### VI - Genome Assembly Programming Challenge

- Week 1 - The 2011 European E. coli Outbreak
- Week 2 - Assembling Genomes Using de Bruijn Graphs
- Week 3 - Genome Assembly Faces Real Sequencing Data

### Detailed Contents

#### I - Algorithmic Toolbox

The course covers basic algorithmic techniques and ideas for computational
problems arising frequently in practical applications: sorting and searching,
divide and conquer, greedy algorithms, dynamic programming. We will learn a lot
of theory: how to sort data and how it helps for searching; how to break a large
problem into pieces and solve them recursively; when it makes sense to proceed
greedily; how dynamic programming is used in genomic studies. You will practice
solving computational problems, designing new algorithms, and implementing
solutions efficiently (so that they run in less than a second).

##### Week 1 - Programming Challenges

Welcome to the first module of Data Structures and Algorithms! Here we will
provide an overview of where algorithms and data structures are used (hint:
everywhere) and walk you through a few sample programming challenges. The
programming challenges represent an important (and often the most difficult!)
part of this specialization because the only way to fully understand an
algorithm is to implement it. Writing correct and efficient programs is hard;
please don’t be surprised if they don’t work as you planned—our first programs
did not work either! We will help you on your journey through the specialization
by showing how to implement your first programming challenges. We will also
introduce testing techniques that will help increase your chances of passing
assignments on your first attempt. In case your program does not work as
intended, we will show how to fix it, even if you don’t yet know which test your
implementation is failing on.

##### Week 2 - Algorithmic Warm-up

In this module you will learn that programs based on efficient algorithms can
solve the same problem billions of times faster than programs based on naïve
algorithms. You will learn how to estimate the running time and memory of an
algorithm without even implementing it. Armed with this knowledge, you will be
able to compare various algorithms, select the most efficient ones, and finally
implement them as our programming challenges!

##### Week 3 - Greedy Algorithms

In this module you will learn about seemingly naïve yet powerful class of
algorithms called greedy algorithms. After you will learn the key idea behind
the greedy algorithms, you may feel that they represent the algorithmic Swiss
army knife that can be applied to solve nearly all programming challenges in
this course. But be warned: with a few exceptions that we will cover, this
intuitive idea rarely works in practice! For this reason, it is important to
prove that a greedy algorithm always produces an optimal solution before using
this algorithm. In the end of this module, we will test your intuition and taste
for greedy algorithms by offering several programming challenges.

##### Week 4 - Divide-and-Conquer

In this module you will learn about a powerful algorithmic technique called
Divide and Conquer. Based on this technique, you will see how to search huge
databases millions of times faster than using naïve linear search. You will even
learn that the standard way to multiply numbers (that you learned in the grade
school) is far from the being the fastest! We will then apply the
divide-and-conquer technique to design two efficient algorithms (merge sort and
quick sort) for sorting huge lists, a problem that finds many applications in
practice. Finally, we will show that these two algorithms are optimal, that is,
no algorithm can sort faster!

##### Week 5 - Dynamic Programming 1

In this final module of the course you will learn about the powerful algorithmic
technique for solving many optimization problems called Dynamic Programming. It
turned out that dynamic programming can solve many problems that evade all
attempts to solve them using greedy or divide-and-conquer strategy. There are
countless applications of dynamic programming in practice: from maximizing the
advertisement revenue of a TV station, to search for similar Internet pages, to
gene finding (the problem where biologists need to find the minimum number of
mutations to transform one gene into another). You will learn how the same idea
helps to automatically make spelling corrections and to show the differences
between two versions of the same text.

##### Week 6 - Dynamic Programming 2

In this module, we continue practicing implementing dynamic programming
solutions.

#### II - Data Structures

A good algorithm usually comes together with a set of good data structures that
allow the algorithm to manipulate the data efficiently. In this course, we
consider the common data structures that are used in various computational
problems. You will learn how these data structures are implemented in different
programming languages and will practice implementing them in our programming
assignments. This will help you to understand what is going on inside a
particular built-in implementation of a data structure and what to expect from
it. You will also learn typical use cases for these data structures.

A few examples of questions that we are going to cover in this class are the
following: 1. What is a good strategy of resizing a dynamic array? 2. How
priority queues are implemented in C++, Java, and Python? 3. How to implement a
hash table so that the amortized running time of all operations is O(1) on
average? 4. What are good strategies to keep a binary tree balanced? You will
also learn how services like Dropbox manage to upload some large files instantly
and to save a lot of storage space!

##### Week 1 - Basic Data Structures

In this module, you will learn about the basic data structures used throughout
the rest of this course. We start this module by looking in detail at the
fundamental building blocks: arrays and linked lists. From there, we build up
two important data structures: stacks and queues. Next, we look at trees:
examples of how they’re used in Computer Science, how they’re implemented, and
the various ways they can be traversed. Once you’ve completed this module, you
will be able to implement any of these data structures, as well as have a solid
understanding of the costs of the operations, as well as the tradeoffs involved
in using each data structure.

##### Week 2 - Dynamic Arrays and Amortized Analysis

In this module, we discuss Dynamic Arrays: a way of using arrays when it is
unknown ahead-of-time how many elements will be needed. Here, we also discuss
amortized analysis: a method of determining the amortized cost of an operation
over a sequence of operations. Amortized analysis is very often used to analyse
performance of algorithms when the straightforward analysis produces
unsatisfactory results, but amortized analysis helps to show that the algorithm
is actually efficient. It is used both for Dynamic Arrays analysis and will also
be used in the end of this course to analyze Splay trees.

##### Week 3 - Priority Queues and Disjoint Sets

We start this module by considering priority queues which are used to
efficiently schedule jobs, either in the context of a computer operating system
or in real life, to sort huge files, which is the most important building block
for any Big Data processing algorithm, and to efficiently compute shortest paths
in graphs, which is a topic we will cover in our next course. For this reason,
priority queues have built-in implementations in many programming languages,
including C++, Java, and Python. We will see that these implementations are
based on a beautiful idea of storing a complete binary tree in an array that
allows to implement all priority queue methods in just few lines of code. We
will then switch to disjoint sets data structure that is used, for example, in
dynamic graph connectivity and image processing. We will see again how simple
and natural ideas lead to an implementation that is both easy to code and very
efficient. By completing this module, you will be able to implement both these
data structures efficiently from scratch.

##### Week 4 - Hash Tables

In this module you will learn about very powerful and widely used technique
called hashing. Its applications include implementation of programming
languages, file systems, pattern search, distributed key-value storage and many
more. You will learn how to implement data structures to store and modify sets
of objects and mappings from one type of objects to another one. You will see
that naive implementations either consume huge amount of memory or are slow, and
then you will learn to implement hash tables that use linear memory and work in
O(1) on average! In the end, you will learn how hash functions are used in
modern disrtibuted systems and how they are used to optimize storage of services
like Dropbox, Google Drive and Yandex Disk!

##### Week 5 - Binary Search Trees

In this module we study binary search trees, which are a data structure for
doing searches on dynamically changing ordered sets. You will learn about many
of the difficulties in accomplishing this task and the ways in which we can
overcome them. In order to do this you will need to learn the basic structure of
binary search trees, how to insert and delete without destroying this structure,
and how to ensure that the tree remains balanced.

##### Week 6 - Binary Search Trees 2

In this module we continue studying binary search trees. We study a few
non-trivial applications. We then study the new kind of balanced search trees -
Splay Trees. They adapt to the queries dynamically and are optimal in many ways.

#### III - Algorithms on Graphs

If you have ever used a navigation service to find optimal route and estimate
time to destination, you've used algorithms on graphs. Graphs arise in various
real-world situations as there are road networks, computer networks and, most
recently, social networks! If you're looking for the fastest time to get to
work, cheapest way to connect set of computers into a network or efficient
algorithm to automatically find communities and opinion leaders in Facebook,
you're going to work with graphs and algorithms on graphs.

In this course, you will first learn what a graph is and what are some of the
most important properties. Then you'll learn several ways to traverse graphs and
how you can do useful things while traversing the graph in some order. We will
then talk about shortest paths algorithms — from the basic ones to those which
open door for 1000000 times faster algorithms used in Google Maps and other
navigational services. You will use these algorithms if you choose to work on
our Fast Shortest Routes industrial capstone project. We will finish with
minimum spanning trees which are used to plan road, telephone and computer
networks and also find applications in clustering and approximate algorithms.

##### Week 1 - Decomposition of Graphs 1

Graphs arise in various real-world situations as there are road networks,
computer networks and, most recently, social networks! If you're looking for the
fastest time to get to work, cheapest way to connect set of computers into a
network or efficient algorithm to automatically find communities and opinion
leaders hot in Facebook, you're going to work with graphs and algorithms on
graphs. In this module, you will learn ways to represent a graph as well as
basic algorithms for decomposing graphs into parts. In the programming
assignment of this module, you will apply the algorithms that you’ve learned to
implement efficient programs for exploring mazes, analyzing Computer Science
curriculum, and analyzing road networks. In the first week of the module, we
focus on undirected graphs.

##### Week 2 - Decomposition of Graphs 2

This week we continue to study graph decomposition algorithms, but now for
directed graphs.

##### Week 3 - Paths in Graphs 1

In this module you will study algorithms for finding Shortest Paths in
Graphs. These algorithms have lots of applications. When you launch a navigation
app on your smartphone like Google Maps or Yandex.Navi, it uses these algorithms
to find you the fastest route from work to home, from home to school, etc. When
you search for airplane tickets, these algorithms are used to find a route with
the minimum number of plane changes. Unexpectedly, these algorithms can also be
used to determine the optimal way to do currency exchange, sometimes allowing to
earh huge profit! We will cover all these applications, and you will learn
Breadth-First Search, Dijkstra's Algorithm and Bellman-Ford Algorithm. These
algorithms are efficient and lay the foundation for even more efficient
algorithms which you will learn and implement in the Shortest Paths Capstone
Project to find best routes on real maps of cities and countries, find distances
between people in Social Networks. In the end you will be able to find Shortest
Paths efficiently in any Graph. This week we will study Breadth-First Search
algorithm.

##### Week 4 - Paths in Graphs 2

This week we continue to study Shortest Paths in Graphs. You will learn
Dijkstra's Algorithm which can be applied to find the shortest route home from
work. You will also learn Bellman-Ford's algorithm which can unexpectedly be
applied to choose the optimal way of exchanging currencies. By the end you will
be able to find shortest paths efficiently in any Graph.

##### Week 5 - Minimum Spanning Trees

In this module, we study the minimum spanning tree problem. We will cover two
elegant greedy algorithms for this problem: the first one is due to Kruskal and
uses the disjoint sets data structure, the second one is due to Prim and uses
the priority queue data structure. In the programming assignment for this module
you will be computing an optimal way of building roads between cities and an
optimal way of partitioning a given set of objects into clusters (a fundamental
problem in data mining).

##### Week 6 - Advanced Shortest Paths Project (Optional)

In this module, you will learn Advanced Shortest Paths algorithms that work in
practice 1000s (up to 25000) of times faster than the classical Dijkstra's
algorithm on real-world road networks and social networks graphs. You will work
on a Programming Project based on these algorithms. You will find the shortest
paths on the real maps of parts of US and the shortest paths connecting people
in the social networks. We encourage you not only to use the ideas from this
module's lectures in your implementations, but also to come up with your own
ideas for speeding up the algorithm! We encourage you to compete on the forums
to see whose implementation is the fastest one :)

#### IV - Algorithms on Strings

World and internet is full of textual information. We search for information
using textual queries, we read websites, books, e-mails. All those are strings
from the point of view of computer science. To make sense of all that
information and make search efficient, search engines use many string
algorithms. Moreover, the emerging field of personalized medicine uses many
search algorithms to find disease-causing mutations in the human genome.

##### Week 1 - Suffix Trees

How would you search for a longest repeat in a string in LINEAR time? In 1973,
Peter Weiner came up with a surprising solution that was based on suffix trees,
the key data structure in pattern matching. Computer scientists were so
impressed with his algorithm that they called it the Algorithm of the Year. In
this lesson, we will explore some key ideas for pattern matching that will -
through a series of trials and errors - bring us to suffix trees.

##### Week 2 - Burrows-Wheeler Transform and Suffix Arrays

Although EXACT pattern matching with suffix trees is fast, it is not clear how
to use suffix trees for APPROXIMATE pattern matching. In 1994, Michael Burrows
and David Wheeler invented an ingenious algorithm for text compression that is
now known as Burrows-Wheeler Transform. They knew nothing about genomics, and
they could not have imagined that 15 years later their algorithm will become the
workhorse of biologists searching for genomic mutations. But what text
compression has to do with pattern matching??? In this lesson you will learn
that the fate of an algorithm is often hard to predict – its applications may
appear in a field that has nothing to do with the original plan of its
inventors.

##### Week 3 - Knuth–Morris–Pratt Algorithm

Congratulations, you have now learned the key pattern matching concepts: tries,
suffix trees, suffix arrays and even the Burrows-Wheeler transform! However,
some of the results Pavel mentioned remain mysterious: e.g., how can we perform
exact pattern matching in O(|Text|) time rather than in O(|Text|*|Pattern|) time
as in the naïve brute force algorithm? How can it be that matching a
1000-nucleotide pattern against the human genome is nearly as fast as matching a
3-nucleotide pattern??? Also, even though Pavel showed how to quickly construct
the suffix array given the suffix tree, he has not revealed the magic behind the
fast algorithms for the suffix tree construction!In this module, Miсhael will
address some algorithmic challenges that Pavel tried to hide from you :) such as
the Knuth-Morris-Pratt algorithm for exact pattern matching and more efficient
algorithms for suffix tree and suffix array construction.

##### Week 4 - Constructing Suffix Arrays and Suffix Trees

In this module we continue studying algorithmic challenges of the string
algorithms. You will learn an O(n log n) algorithm for suffix array construction
and a linear time algorithm for construction of suffix tree from a suffix
array. You will also implement these algorithms and the Knuth-Morris-Pratt
algorithm in the last Programming Assignment in this course.

#### V - Advanced Algorithms and Complexity

You've learned the basic algorithms now and are ready to step into the area of
more complex problems and algorithms to solve them. Advanced algorithms build
upon basic ones and use new ideas. We will start with networks flows which are
used in more typical applications such as optimal matchings, finding disjoint
paths and flight scheduling as well as more surprising ones like image
segmentation in computer vision. We then proceed to linear programming with
applications in optimizing budget allocation, portfolio optimization, finding
the cheapest diet satisfying all requirements and many others. Next we discuss
inherently hard problems for which no exact good solutions are known (and not
likely to be found) and how to solve them in practice. We finish with a soft
introduction to streaming algorithms that are heavily used in Big Data
processing. Such algorithms are usually designed to be able to process huge
datasets without being able even to store a dataset.

##### Week 1 - Flows in Networks

Network flows show up in many real world situations in which a good needs to be
transported across a network with limited capacity. You can see it when shipping
goods across highways and routing packets across the internet. In this unit, we
will discuss the mathematical underpinnings of network flows and some important
flow algorithms. We will also give some surprising examples on seemingly
unrelated problems that can be solved with our knowledge of network flows.

##### Week 2 - Linear Programming

Linear programming is a very powerful algorithmic tool. Essentially, a linear
programming problem asks you to optimize a linear function of real variables
constrained by some system of linear inequalities. This is an extremely
versatile framework that immediately generalizes flow problems, but can also be
used to discuss a wide variety of other problems from optimizing production
procedures to finding the cheapest way to attain a healthy diet. Surprisingly,
this very general framework admits efficient algorithms. In this unit, we will
discuss some of the importance of linear programming problems along with some of
the tools used to solve them.

##### Week 3 - NP-complete Problems

Although many of the algorithms you've learned so far are applied in practice a
lot, it turns out that the world is dominated by real-world problems without a
known provably efficient algorithm. Many of these problems can be reduced to one
of the classical problems called NP-complete problems which either cannot be
solved by a polynomial algorithm or solving any one of them would win you a
million dollars (see Millenium Prize Problems) and eternal worldwide fame for
solving the main problem of computer science called P vs NP. It's good to know
this before trying to solve a problem before the tomorrow's deadline :) Although
these problems are very unlikely to be solvable efficiently in the nearest
future, people always come up with various workarounds. In this module you will
study the classical NP-complete problems and the reductions between them. You
will also practice solving large instances of some of these problems despite
their hardness using very efficient specialized software based on tons of
research in the area of NP-complete problems.

##### Week 4 - Coping with NP-completeness

After the previous module you might be sad: you've just went through 5 courses
in Algorithms only to learn that they are not suitable for most real-world
problems. However, don't give up yet! People are creative, and they need to
solve these problems anyway, so in practice there are often ways to cope with an
NP-complete problem at hand. We first show that some special cases on
NP-complete problems can, in fact, be solved in polynomial time. We then
consider exact algorithms that find a solution much faster than the brute force
algorithm. We conclude with approximation algorithms that work in polynomial
time and find a solution that is close to being optimal.

##### Week 5 - Streaming Algorithms (Optional)

In most previous lectures we were interested in designing algorithms with fast
(e.g. small polynomial) runtime, and assumed that the algorithm has random
access to its input, which is loaded into memory. In many modern applications in
big data analysis, however, the input is so large that it cannot be stored in
memory. Instead, the input is presented as a stream of updates, which the
algorithm scans while maintaining a small summary of the stream seen so
far. This is precisely the setting of the streaming model of computation, which
we study in this lecture. The streaming model is well-suited for designing and
reasoning about small space algorithms. It has received a lot of attention in
the literature, and several powerful algorithmic primitives for computing basic
stream statistics in this model have been designed, several of them impacting
the practice of big data analysis. In this lecture we will see one such
algorithm (CountSketch), a small space algorithm for finding the top k most
frequent items in a data stream.

#### VI - Genome Assembly Programming Challenge


In Spring 2011, thousands of people in Germany were hospitalized with a deadly
disease that started as food poisoning with bloody diarrhea and often led to
kidney failure. It was the beginning of the deadliest outbreak in recent
history, caused by a mysterious bacterial strain that we will refer to as
E. coli X. Soon, German officials linked the outbreak to a restaurant in Lübeck,
where nearly 20% of the patrons had developed bloody diarrhea in a single
week. At this point, biologists knew that they were facing a previously unknown
pathogen and that traditional methods would not suffice – computational
biologists would be needed to assemble and analyze the genome of the newly
emerged pathogen.

To investigate the evolutionary origin and pathogenic potential of the outbreak
strain, researchers started a crowdsourced research program. They released
bacterial DNA sequencing data from one of a patient, which elicited a burst of
analyses carried out by computational biologists on four continents. They even
used GitHub for the project:
https://github.com/ehec-outbreak-crowdsourced/BGI-data-analysis/wiki The 2011
German outbreak represented an early example of epidemiologists collaborating
with computational biologists to stop an outbreak. In this Genome Assembly
Programming Challenge, you will follow in the footsteps of the bioinformaticians
investigating the outbreak by developing a program to assemble the genome of the
E. coli X from millions of overlapping substrings of the E.coli X genome.

##### Week 1 - The 2011 European E. coli Outbreak

In April 2011, hundreds of people in Germany were hospitalized with a deadly
disease that often started as food poisoning with bloody diarrhea. It was the
beginning of the deadliest outbreak in recent history, caused by a mysterious
bacterial strain that we will refer to as E. coli X. Within a few months, the
outbreak had infected thousands and killed 53 people. To prevent the further
spread of the outbreak, computational biologists all over the world had to
answer the question “What is the genome sequence of E. coli X?” in order to
figure out what new genes it acquired to become pathogenic.

The 2011 German outbreak represented an early example of epidemiologists
collaborating with computational biologists to stop an outbreak. In this Genome
Assembly Programming Challenge, you will follow in the footsteps of the
bioinformaticians investigating the outbreak by developing a program to assemble
the genome of the deadly E. coli X strain. However, before you embark on
building a program for assembling the E. coli X strain, we have to explain some
genomic concepts and warm you up by having you solve a simpler problem of
assembling a small virus.

##### Week 2 - Assembling Genomes Using de Bruijn Graphs

DNA sequencing approach that led to assembly of a small virus in 1977 went
through a series of transformations that contributed to the emergence of
personalized medicine a few years ago. By the late 1980s, biologists were
routinely sequencing viral genomes containing hundreds of thousands of
nucleotides, but the idea of sequencing a bacterial (let alone the human) genome
containing millions (or even billions) of nucleotides remained preposterous and
would cost billions of dollars.

In 1988, three biologists (independently and simultaneously!) came up with an
idea to reduce sequencing cost and proposed the futuristic and at the time
completely implausible method of DNA arrays. None of these three biologists
could have possibly imagined that the implications of his own experimental
research would eventually bring him face-to-face with challenging algorithmic
problems. In this module you will learn about the algorithmic challenge of DNA
sequencing using information about short k-mers provided by DNA arrays. You will
also travel to the 18the century to learn about the Bridges of Konigsberg and
solve a related problem of assembling a jigsaw puzzle!

##### Week 3 - Genome Assembly Faces Real Sequencing Data

Our discussion of genome assembly has thus far relied upon various
assumptions. In this module, we will face practical challenges introduced by
quirks in modern sequencing technologies and discuss some algorithmic techniques
that have been devised to address these challenges. Afterwards, you will
assemble the smallest bacterial genome that lives symbiotically inside
leafhoppers. Its sheltered life has allowed it to reduce its genome to only
about 112,091 nucleotides and 137 genes. And afterwards, you will be ready to
assemble the E. coli X genome!
