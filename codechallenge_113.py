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

Note: Due to increase complexity, we will skip steps 2,3,4 and make further assumption that the 
      given list should be checked for assending order only.

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


Executing command:
=================
- For unittest:  `pipenv run python .\codechallenge_113.py`
- Normal execution: `python .\codechallenge_113.py`

'''

import unittest
import HtmlTestRunner
import os, time
from unittest.runner import TextTestResult


#
# Return True is list is in descending order
# O(n) complexity
#
def isDescendingSorted(lst):
    # Check for Descending Sorted List
    flag = False
    test_list1 = lst[:]
    test_list1.sort(reverse = True)
    if (test_list1 == lst):
        flag = True
        
    return flag   



def findSmallestUnsortedWindow(lst):
    # Base cases:
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return None
    
    # Check if the input list is sorted.  This incurs O(n) and will be striked out of the algorithm
    # if all(lst[i] <= lst[i+1] for i in range(len(lst) - 1)) == True:
    #     bAssencding = True
    #     return None
    
    # Check for Descending Sorted List
    # bDescending = isDescendingSorted(lst)
    
    # Define resulting indices
    startingIdx = endingIdx = 0
        
    # iterate from right to left:
    idx = 0
    while idx < len(lst):
        if lst[idx] < lst[idx-1]:
            idx += 1
        else:
            startingIdx=idx
            break
    
    # iterate from left to right:
    idx = len(lst) - 1
    while idx > 0:
        if lst[idx] > lst[idx-1]:
            idx -= 1
        else:
            endingIdx = idx + 1
            break
        
    #print(startingIdx, endingIdx)
    return (startingIdx, endingIdx)
        
#
# Unittest
#
class TestSmallestUnorderedWindow(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    
    def test_SortedList(self):
        time.sleep(1)
        Slst = [1,2,3,4,5,6,7,8,9]
        assert findSmallestUnsortedWindow(Slst) == (0,0)
        Slst = []
        assert findSmallestUnsortedWindow(Slst) == None
        Slst = [12]
        assert findSmallestUnsortedWindow(Slst) == None
        time.sleep(1)
                    
    def test_SmallWindow(self):
        Slst = [51,3,4,5,2,6,7,8,9,10,17,12,50]
        assert findSmallestUnsortedWindow(Slst) == (1, 11)

#
# main driver
#
def main():
    Slst = [3,7,5,6,8,9,10,17,12,15,14,11]
    print('Given ', Slst, end=' ')
    print(' the bounds of the smallest window is ', findSmallestUnsortedWindow(Slst))
    Slst = [51,3,4,5,2,6,7,8,9,10,17,12,50]
    print('Given ', Slst, end=' ')
    print(' the bounds of the smallest window is ', findSmallestUnsortedWindow(Slst))    
    Slst = [1,2,3,4,5,6,7,8,9]
    print('Given ', Slst, end=' ')
    print(' the bounds of the smallest window is ', findSmallestUnsortedWindow(Slst))
    Slst = []
    print('Given ', Slst, end=' ')
    print(' the bounds of the smallest window is ', findSmallestUnsortedWindow(Slst))
    Slst = [12]
    print('Given ', Slst, end=' ')
    print(' the bounds of the smallest window is ', findSmallestUnsortedWindow(Slst))
    Slst = [3, 7, 5, 6, 9]
    print('Given ', Slst, end=' ')
    print(' the bounds of the smallest window is ', findSmallestUnsortedWindow(Slst))


if __name__ == '__main__':
    if os.environ.get('UNITTEST_ONLY') == 'True':
        main()
    else:
        try:
            # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))    
            unittest.main()
        except Exception as e:
            print(e)

        
'''
Run-time output:
===============
$ pipenv run python ./codechallenge_113.py 
Loading .env environment variables...
Given  [3, 7, 5, 6, 8, 9, 10, 17, 12, 15, 14, 11]  the bounds of the smallest window is  (1, 12)
Given  [51, 3, 4, 5, 2, 6, 7, 8, 9, 10, 17, 12, 50]  the bounds of the smallest window is  (0, 12)
Given  [1, 2, 3, 4, 5, 6, 7, 8, 9]  the bounds of the smallest window is  (1, 0)
Given  []  the bounds of the smallest window is  None
Given  [12]  the bounds of the smallest window is  None
Given  [3, 7, 5, 6, 9]  the bounds of the smallest window is  (1, 3)


unittest output:
================
PS D:\devel\GIT\DailyCodingChallenge> pipenv run python .\codechallenge_113.py
Loading .env environment variables...

Running tests... 
----------------------------------------------------------------------
 test_SmallWindow (__main__.TestSmallestUnorderedWindow) ... OK (0.000000)s
 test_SortedList (__main__.TestSmallestUnorderedWindow) ... OK (2.001912)s

----------------------------------------------------------------------
Ran 2 tests in 0:00:02

OK

Generating HTML reports...
test_reports\TestResults___main__.TestSmallestUnorderedWindow_2022-05-03_13-31-36.html
'''