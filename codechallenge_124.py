'''
Date: 06/30/2022

Challenge description:
=======================
CombinationSum of a given array of integers to a given target sum.
The number can be choosen more than once.

Return all unique combinations of the array that sum to the target sum.

Example:
  
Input: [1, 2, 3, 4, 5], target sum = 6
Output: [[1,1,1,1,1,1], [1,1,1,1,2], [1,1,2,2], [1,2,3],
        [2,2,2], [2,3,1], [2,4], 
        [3,1,1,1], [3,3], 
        [4, 1, 1], 
        [5, 1]]

Complexity: O(n^2)
'''
from pickle import TRUE
import unittest
import os, time
from unittest.runner import TextTestResult

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        
        # edge case
        if target == 0:
            result.append([])
            
        def sumHelper(idx, curr, sum):
            # base cases
            if sum == target:
                result.append(curr.copy())
                return
            
            if idx >= len(candidates) or sum > target:
                return
            
            # recursive case
            curr.append(candidates[idx])
            sumHelper(idx, curr, sum + candidates[idx])
            curr.pop()
            sumHelper(idx + 1, curr, sum)    
        
        # call the helper function
        sumHelper(0, [], 0)
        
        return result        
    
# Unit test
class TestCombinationSum(unittest.TestCase):
    def testCS(self):
        nums = [2,3,5,7]
        target = 7
        self.assertEqual(Solution().combinationSum(nums, target), [[2,2,3], [2,5], [7]])
                               
def main():
    nums = [1, 2, 3, 4, 5]
    target = 6
    print("Test 1:")
    print("Given array: '{}' and target: '{}'".format(nums, target))
    print("Unique combination of numbers whose sum equals '{}' is \n{}".format(target, Solution().combinationSum(nums, target)))
    
    nums = [2,3,6,7]
    target = 7
    print("\nTest 2:")
    print("Given array: '{}' and target: '{}'".format(nums, target))
    print("Unique combination of numbers whose sum equals '{}' is \n{}".format(target, Solution().combinationSum(nums, target)))

if __name__ == "__main__":
    if os.environ.get('UNITTEST_ONLY') != TRUE:
        main()
    else:
        try:
            unittest.main()
        except Exception as e:
            print(e)            

'''
Runtime output:
===============
PS D:\DEVEL\GIT\DailyCodingChallenge> python .\codechallenge_124.py
Test 1:
Given array: '[1, 2, 3, 4, 5]' and target: '6'
Unique combination of numbers whose sum equals '6' is
[[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2], [1, 1, 1, 3], [1, 1, 2, 2], [1, 1, 4], [1, 2, 3], [1, 5], [2, 2, 2], [2, 4], [3, 3]]

Test 2:
Given array: '[2, 3, 6, 7]' and target: '7'
Unique combination of numbers whose sum equals '7' is
[[2, 2, 3], [7]]

Unit test output:
=================
PS D:\DEVEL\GIT\DailyCodingChallenge> python .\codechallenge_124.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''