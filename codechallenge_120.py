'''
Date: 06/28/2022

Two pointers problem: (from leetcode)
=======================
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Constraints:
============
    2 <= numbers.length <= 3 * 104
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.

Example 1:
==========
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
==========
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
==========
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
    
'''

import unittest
import os, time
from unittest.runner import TextTestResult

# worst case time complexity of O(n)
def sum2numbers(numbers, target):
    
    i = 0 # start from the beginning of the list
    j = len(numbers) - 1 # start from the end of the list
    
    # traverse the list from both ends going toward the middle
    while i < j:
        if numbers[i] + numbers[j] == target:
            return [i + 1, j + 1]
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            j -= 1
    return []

def main():
    numbers = [2,7,11,15]
    target = 9
    print("Test case #1:")
    print("Given a 1-indexed sorted in non-decreasing order array of integers numbers {}".format(numbers))
    print("The indices of two numbers that add up to a target number: {}".format(sum2numbers(numbers, target)))
    
    print("\nTest case #2:")
    numbers = [2,3,4] 
    target = 6
    print("Given a 1-indexed sorted in non-decreasing order array of integers numbers {}".format(numbers))
    print("The indices of two numbers that add up to a target number: {}".format(sum2numbers(numbers, target)))
    
    print("\nTest case #3:")
    numbers = [-1,0] 
    target = -1
    print("Given a 1-indexed sorted in non-decreasing order array of integers numbers {}".format(numbers))
    print("The indices of two numbers that add up to a target number: {}".format(sum2numbers(numbers, target)))
    
    print("\n\n")


class TestSum2Numbers(unittest.TestCase):
    def testCase1(self):
        assert sum2numbers([2,7,11,15], 9) == [1, 2]
    def testCase2(self):
        assert sum2numbers([2,3,4], 6) == [1, 3]
    def testCase3(self):
        assert sum2numbers([-1,0], -1) == [1, 2]
    
if __name__ == '__main__':
    if os.environ.get('UNITTEST_ONLY') != 'True':
        main()
    else:
        try:
            unittest.main()
        except Exception as e:
            print(e)    
            
'''
Unit test output:
=================
PS D:\DEVEL\GIT\DailyCodingChallenge> pipenv run python .\codechallenge_120.py
Loading .env environment variables...
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

Runtime main():
==============

Loading .env environment variables...
Test case #1:
Given a 1-indexed sorted in non-decreasing order array of integers numbers [2, 7, 11, 15]
The indices of two numbers that add up to a target number: [1, 2]

Test case #2:
Given a 1-indexed sorted in non-decreasing order array of integers numbers [2, 3, 4]
The indices of two numbers that add up to a target number: [1, 3]

Test case #3:
Given a 1-indexed sorted in non-decreasing order array of integers numbers [-1, 0]
The indices of two numbers that add up to a target number: [1, 2]

'''            