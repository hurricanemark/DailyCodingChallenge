'''
Date: 01/17/2019

Problem description:
===================
This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, 
since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.


Algorithm:
==========
Input: A list of numbers
Output: An integer

Pseudo code:
1.  Check for valid input
2.  Write a generator to yield all sub arrays from the given array
3.  Write a function that take a sub array of numbers and iterate though
    determine if the direction of flow from items[1]..items[len(items)-2] is uni-directional.
	if yes, sum them up.  Keep the sum value in an array.
4.  return max(sum_array)
 
'''


def isContiguous(arr=[]):
	pass
#
# return all sub arrays 
#
def all_subarrays(arr=[]):
    start,end=0,len(arr)
    j=end
    results=[]

    while start < end-1:
        temp = arr[start:j] #Time complexity O(k)
        #print("DBUG-- {}".format(temp))
        j-=1

        if isContiguous(temp):
            results.append(temp)

        if j<start+2:
            start+=1
            j=end

    return list(set(results))

