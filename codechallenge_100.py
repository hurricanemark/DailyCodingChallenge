#!/bin/python3
'''
Date: 12/19/2021
This problem was asked by HackerRank.
Problem Statement: 
=================
Given the array of numbers, and a number k, return 'YES' if k exists in the array and 'No' otherwise.

Algorithm:
==========
- Validate input 
- Sort the array
- Traverse the array and check if k exists in the array
- Return 'YES' or 'NO'

Implentation:
=============
+ Sequential Algorithm
+ Shorthand Algorithm

'''

# Sequential Algorithm O(n)
def findNumberSequentialSearch(arr, k):
    # This function returns a STRING of 'YES' or 'NO'
    # arr: a list of numbers
    # k: the number to find in the list
    start, end = 0, len(arr)-1
    if len(arr) == 0:
        return 'NO'

    arr.sort()
    for i in range(len(arr)):
        if arr[i] == k:
            return 'YES'
    return 'NO'


# Shorthand Algorithm: O(n)
def shorthandFindNumber(arr, k):
    # This function returns a STRING of 'YES' or 'NO'
    # arr: a list of numbers
    # k: the number to find in the list
    return 'YES' if k in arr else 'NO'

#
# unittest
#
def test_FindNumber(arr, k):
    print('Sequential Search result: ', findNumberSequentialSearch(arr, k))
    print('Shorthand Search result: ', shorthandFindNumber(arr, k))

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    k = 6
    print("\nTest#1: arr={}, k={}".format(arr, k))
    test_FindNumber(arr, k)
    arr = []
    k = 10
    print("\nTest#2: arr={}, k={}".format(arr, k))
    test_FindNumber(arr, k)
    arr = [21, 12, 73, 34, 85, 16, 97, 58, 29, 10]
    k = '0x10'
    print("\nTest#3: arr={}, k={}".format(arr, k))
    test_FindNumber(arr, k)
    k = 29
    print("\nTest#4: arr={}, k={}".format(arr, k))
    test_FindNumber(arr, k)