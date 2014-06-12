# data-structures
===============

### This repo holds sample code for a number of classic data structures implemented in Python.

### Co-Authors:
* Perry Hook
* Sean Azlin

### Source and inspirations:
* Python Reference Docs on Data Structures (https://docs.python.org/2/tutorial/datastructures.html)
* Ideas for creating a custom exception (http://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python)
* Heap Visualization (http://www.cs.usfca.edu/~galles/JavascriptVisual/Heap.html)
* Python Rich Comparison Methods (http://www.voidspace.org.uk/python/articles/comparison.shtml)

### Implemented Data Structures
* linked list as l_list class
* stack as Stack class
* queue as Queue class
* doubly linked list as DLinkedList
* min binary heap


###Strength & Weakness of Each Data Structure
####Doubly Linked List:
Strengths:
* Good way to implement a Queue
* Insertion at head or tail is O(1)
* Insertion in general does not require reallocating space for the entire list as the list grows
* Concatinating a list to a doubly linked list is O(1)

Weaknesses:
* Removing an arbitrary value in the list is O(n) worst case ( Remove() )
* Our implementation doesn't allow insertion other than at the head or tail, but if it did the insertion time complexity would be O(n) worst case
* Our implementation doesn't have a way to access values that aren't at the head or tail. If it did, the search would be O(n)


####Min Binary Heap:
The min binary heap is implemented using a list.  It can be constructed by passing an iterable upon creation, otherwise it is left empty.  The public interface includes methods for push(val), pop(), peek().  
