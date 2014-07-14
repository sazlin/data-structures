# data-structures [![Build Status](https://travis-ci.org/sazlin/data-structures.svg?branch=weighted)](https://travis-ci.org/sazlin/data-structures)
===============

### This repo holds sample code for a number of classic data structures implemented in Python.

### Co-Authors:
* Perry Hook
* Sean Azlin

### Implemented Data Structures
* linked list as l_list class
* stack as Stack class
* queue as Queue class
* doubly linked list as DLinkedList
* min binary heap
* prioirity queue
* graph as Graph class
* binary search tree as BinarySearchTree
* hash table as HashTable

###Linked List
Description TBD

###Stack
Description TBD

###Queue
Description TBD

###Doubly Linked List:
Strengths:
* Good way to implement a Queue
* Insertion at head or tail is O(1)
* Insertion in general does not require reallocating space for the entire list as the list grows
* Concatinating a list to a doubly linked list is O(1)

Weaknesses:
* Removing an arbitrary value in the list is O(n) worst case ( Remove() )
* Our implementation doesn't allow insertion other than at the head or tail, but if it did the insertion time complexity would be O(n) worst case
* Our implementation doesn't have a way to access values that aren't at the head or tail. If it did, the search would be O(n)

###Min Binary Heap:
The min binary heap is implemented using a list.  It can be constructed by passing an iterable upon creation, otherwise it is left empty.  The public interface includes methods for push(val), pop(), peek().  

###Prioirty Queue
Description TBD

###Graph
An object-oriented adjacency list-style implementation of a graph.  Graph
supports weighted edges between nodes.  By default, if no weight is specified,
new edges will have weight 1.

Graph has methods depth_first_traversal and breadth_first_traversal that return
a list of the nodes visited, in order, during the traversal.

For shortest path finding, the classic Dijkstra's algorithm is implemented as shortest_path_dijkstra(source, destination) for a source and destination node.  This method returns a tuple containing a list of the nodes in the path (in reverse order - starting with the destination and working it's way back to the source) and the cost of that path.  

Also implemented is the Bellman-Ford shortest path algorithm, shortest_path_Bellman-Ford(source, destination), which adds shortest-path finding for graphs with negative weight edges.  Bellman-Ford works similarly to Dijkstra's in that providing a source and destination node will return a tuple containing the list which is the path, and the cost of that path.  Bellman-Ford will detect negative-weight cycles in a graph and raise a NegativeWeightCycleError.

If you are finding a path in a graph with negative edge weights, use Bellman-Ford.  It is not as efficient as Dijkstra's algorithm, however, for graphs with all positive edge-weights.  Our implementation of Dijkstra runs in O(|V|^2) as we did not use a priority queue.  Bellman-Ford runs in O(|V||E|), since the "relaxation" step in Bellman-Ford must go through the all the edges in the graph.

Both shortest path algorithms follow Wikipedia's pseudocode fairly closely.

###Binary Search Tree
Description TBD

###Hash Table
A simple hash table implementation using a list of buckets. Each bucket is a list of key, value tuples where the key was hashed to the same index. Our hash table has 4 methods:
* __init__(size=1024): creates a hashtable of size 1024 by default. The size can be set manually.
* set(key, value): adds the key and value as a tuple to the bucket found at the _hash(key) index of the hash table's bucket list. If the key is already present in the bucket then that key's value is overwritten with the new value. Set is O(1) except for when collisions occur, then set() is O(N) where N is the number of keys already present in that bucket.
* get(key): returns the value associated with this key. If the key is not found in the _hash(key) bucket then a KeyError is raised. get() is O(1) except when collisions occur, then get() is O(N) where N is the number of keys present in that bucket.
* _hash(key): A very simple hash function that generates a bucket index using a given key. Key is generated using the sum of the ord() of each character in the key string and then modding the sum with the size of the hashtable. This is a very simple implementation of a hash function that results in collisions often for lots of strings, especially strings that are anagrams of eachother. Key must be an instance of basestring, else a TypeError will be raised. Because a for-loop is used to iterate over the chars in a key string, _hash() is O(N) where N is the number of characters in the key string. 

### Sources and inspirations:
* Python Reference Docs on Data Structures (https://docs.python.org/2/tutorial/datastructures.html)
* Ideas for creating a custom exception (http://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python)
* Heap Visualization (http://www.cs.usfca.edu/~galles/JavascriptVisual/Heap.html)
* Python Rich Comparison Methods (http://www.voidspace.org.uk/python/articles/comparison.shtml)
* Adjacency Lists (http://en.wikipedia.org/wiki/Adjacency_list)
* Example DFS and BFS Implementations (http://code.activestate.com/recipes/576723-dfs-and-bfs-graph-traversal/)
* Wikipedia entry on graph traversal (http://en.wikipedia.org/wiki/Graph_traversal)
* Wikipedia entry on Dijkstra's Algorithm (http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
* Wikipedia entry on Bellman-Ford Algorithm (http://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)
