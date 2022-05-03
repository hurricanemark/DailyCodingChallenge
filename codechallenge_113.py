'''
Date: 05/02/2022

Problem description:
====================
This problem was asked by WhatsApp.

Given an array of integers out of order, determine the bounds of the smallest window 
that must be sorted in order for the entire array to be sorted. 
For example, given [3, 7, 5, 6, 9], you should return (1, 3)

Input: A list of integers
Output: (starting index, ending index) of the sublist that is unsorted.

Algorithm 1:
============
Assumption -- The input list contains multiple windows of unsorted elements.
[1,2,3, 7,5,6, 8,9,10, 17,12,15,14,11]
1.  Validate input.
2.  Base case: is sorted?  Hmmm, might not be part of the solution but does cover the basic.
3.  Base case: is assending order or descending order?
4.  Base case: are the duplicates?
5.  Traverse the list from right to left until we hit the first unsorted element, make this the 
    starting index of the window by backtracking to one previous index.
6.  Continue traversal until we hit another starting index of sorted element, i.e. the next element 
    that is out of order.  Make this the ending of the window.
7.  Repeat steps 3 and 4 until the end of the list.  Compare length of windows and return the smallest length.


Algorithm 2:
============
Assumption -- The input list is out of order at the first index from right to left.  
The ending index should be found from left to right.  Worst case is we have n elements to sort.
Example: [50,1,2,3,4,6,5,7,8,9,51]
1.  Validate input
2.  Traverse the list from right to left until we hit the first unordered element, make it starting index
3.  Traverse the list from left to right until we hit the first unorder element, make it the ending index
4.  Return the starting, ending index.

Note: Algorithm #1 answers the main question.  Algorithm #2 is an alternate that roughly answers the main question, but not quite.
=====

'''

import unittest
import HtmlTestRunner
import os, time
from unittest.runner import TextTestResult


def findSmallestUnsortedWindow(lst):
    # Base cases:
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return None
    
    # Check if the input list is sorted.  This incurs O(n) and will be striked out of the algorithm
    if all(lst[i] <= lst[i+1] for i in range(len(lst) - 1)) == True:
        return None
    

class TestSmallestUnorderedWindow(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    
    def test_SortedList(self):
        time.sleep(1)
        Slst = [1,2,3,4,5,6,7,8,9]
        assert findSmallestUnsortedWindow(Slst) == None
        Slst = []
        assert findSmallestUnsortedWindow(Slst) == None
        Slst = [12]
        assert findSmallestUnsortedWindow(Slst) == None
        time.sleep(1)
                    
    def test_SmallWindow(self):
        pass


def main():
    pass


if __name__ == '__main__':
    if os.environ.get('UNITTEST_ONLY') != 'True':
        main()
    else:
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))    