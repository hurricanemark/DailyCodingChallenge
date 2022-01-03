'''
This problem was asked by Twitter.

Problem statement:
==================
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

-  record(order_id): adds the order_id to the log
-  get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.

Forethought:
============
Data structures in this case is used for the Relational Database Management System (Array of structure). so, possible structure where all entries 
must be of the same data type such as list can be classified into linear and non-linear data structures.
Although not the best at efficency, linear data structures contain Stacks and Queues fits the requiremnts.
Otherwise, non-linear data structure such as a hash table would be more efficient.

Note, Stack is a container of objects that can be inserted or removed according to LIFO (Last in First Out) pop() method is used during disposal in Python

'''

      