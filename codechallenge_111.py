'''
Date: 04/28/2022

Problem description:
====================
This problem was asked by Fitbit.

Given a linked list, rearrange the node values such that they appear in 
alternating low -> high -> low -> high ... form. 
For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4. 

Algorithm:
==========
1. Assume the list is sorted in ascending order.
2. Starting with 2nd node, swap the consecutive nodes for low-->high-->low.
3. Swap the last two nodes for low-->high.

'''

import unittest

# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data = None, next=None): 
        self.data = data
        self.next = next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None
  
    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
                
            current.next = newNode
        else:
            self.head = newNode
  
    # method to swap the consecutive nodes for low-->high-->low-->high.
    def swapLowHigh(self, node):
        # empty list
        if self.head is None:
            return None
        previous = self.head
        current = self.head.next
    
        while current:
            # if previous node is greater than current node, swap
            if previous.data > current.data:
                temp = previous.data
                previous.data = current.data
                current.data = temp
            
            # if the next node is greater than the current node, swap
            if current.next and current.next.data > current.data:
                temp = current.next.data
                current.next.data = current.data
                current.data = temp
        
            # update previou and current node
            previous = current.next
            if current.next is None:
                break
            current = current.next.next
            
        return self.head
            
      
  
    # print method for the linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.data, end=' --> ')
            current = current.next
        print('None')
        
# Test cases
class Test111(unittest.TestCase):
    def test_swapLowHigh(self):
        ll = LinkedList()
        ll.insert(1)
        ll.insert(2)
        ll.insert(3)
        ll.insert(4)
        ll.insert(5)
        ll.insert(6)
        ll.insert(7)
        ll.insert(8)
        ll.insert(9)
        ll.insert(10)
        ll.insert(11)
        ll.insert(12)
        ll.insert(13)
        ll.insert(14)
        ll.insert(15)
        
        self.assertTrue(ll.swapLowHigh(ll.head),  [1,3,2,5,4,7,6,9,8,11,10,13,12,15,14])       
        
        ll.printLL()
        
if __name__ == '__main__':
    # Singly Linked List with insertion and print methods
    LL = LinkedList()
    LL.insert(1)
    LL.insert(2)
    LL.insert(3)
    LL.insert(4)
    LL.insert(5)
    LL.insert(6)
    LL.insert(7)
    LL.insert(8)
    LL.insert(9)
    LL.insert(10)
    LL.printLL()
    LL.swapLowHigh(LL.head)
    LL.printLL()

    # unit test
    unittest.main()


'''
Runtime output:
===============
PS D:\devel\GIT\DailyCodingChallenge> python .\codechallenge_111.py
1 --> 2 --> 3 --> 4 --> 5 --> 6 --> 7 --> 8 --> 9 --> 10 --> None
1 --> 3 --> 2 --> 5 --> 4 --> 7 --> 6 --> 9 --> 8 --> 10 --> None
1 --> 3 --> 2 --> 5 --> 4 --> 7 --> 6 --> 9 --> 8 --> 11 --> 10 --> 13 --> 12 --> 15 --> 14 --> None
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''