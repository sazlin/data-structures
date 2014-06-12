# data-structures
===============

### This repro holds sample code for a number of classic data structures implemented in Python.

### Co-Authors:
* Perry Hook
* Sean Azlin

### Source and inspirations:
* Python Reference Docs on Data Structures (https://docs.python.org/2/tutorial/datastructures.html)
* Ideas for creating a custom exception (http://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python)
* Heap Visualization (http://www.cs.usfca.edu/~galles/JavascriptVisual/Heap.html)

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
* Removing head or tail of list is O(1) ( Pop() and Shift() )
* Concatinating a list to a doubly linked list is O(1)

Weaknesses:
* Removing an arbitrary value in the list is O(n) worst case ( Remove() )
* Our implementation doesn't allow insertion other than at the head or tail, but if it did the insertion time complexity would be O(n) worst case
* Our implementation doesn't have a way to access values that aren't at the head or tail. If it did, the search would be O(n)
