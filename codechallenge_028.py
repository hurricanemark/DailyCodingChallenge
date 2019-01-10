'''
Date: 01/10/2019

Problem description:
===================
This problem was asked by Google.

Given a list of integers S and a target number k, write a function 
that returns a subset of S that adds up to k. If such a subset cannot 
be made, then return null.

Integers can appear more than once in the list. You may assume all 
numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, 
return [12, 9, 2, 1] since it sums up to 24.


Algorithm:
=========
Input: A list of positive integers
Output: A subset of the given list or None
Assumption: Integers can appear more than one in the output list.
Psuedo code:
1.  Check for valid input
2.  Create a recursive function with 
    -  Base case: list of length 1
    -  Change state by decrementing the list index finding sum equals to k
       Append elements to the subset list 
	-  Call itself until it reaches the base case.

3.  Return the subset list

Alternatively, 
1.  Check for valid input
2.  Assume that numbers can appear more than once in the subset,
	Iterate through the given set and add the number in the cumulative sum
	Compare cumulative sum to k.  If cumulative sum equals to k return subset
	Else if cumulaive sum > k return empty set.
	

'''

import sys

#
# return subset using recursive calls
#
def subset(S, k):
	pass

#
# Alternaively, return a subset using some 
# elements in the given list more than once
#
def get_subset(S, k):
	subset = []
	if len(S) == 0:
		return subset

	sum_so_far = 0
	while len(S) >= 1:
		for i in S:
			if i > k:
				S.remove(i)				
			else:
				if (sum_so_far + i) == k:
					subset.append(i)
					sum_so_far += i	
					return subset
				elif (sum_so_far + i) < k:
					subset.append(i)
					sum_so_far += i	

	if sum_so_far > k:
		return []

		
def test_get_subset():
	S = [12, 1, 61, 5, 9, 2]
	k = 24
	assert get_subset(S, k) == [12, 1, 9, 2]

	S = []
	k = 'a'
	assert get_subset(S, k) == []

def main():
	S = [12, 1, 61, 5, 9, 2]
	k = 24
	s_set = get_subset(S, k)

	if len(s_set) > 0:
		print("Test1:\nGiven a set of numbers: [{}] and a number k: {}.".format(\
			', '.join(str(n) for n in S), k))
		print("A subset that adds up to k is [{}]".format(' '.join(str(i) for i in s_set)))

	k = 100
	s_set = get_subset(S, k)
	if len(s_set) > 0:
		print("\nTest2:\nGiven a set of numbers: [{}] and a number k: {}.".format(\
			', '.join(str(n) for n in S), k))
		print("A subset that adds up to k is [{}]".format(' '.join(str(i) for i in s_set)))

if __name__ == '__main__':
	main()


'''
Run-time output:
===============
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_028.py
Test1:
Given a set of numbers: [12, 1, 5, 9, 2] and a number k: 24.
A subset that adds up to k is [12 1 9 2]

Test2:
Given a set of numbers: [12, 1, 5, 9, 2] and a number k: 100.
A subset that adds up to k is [12 1 5 9 2 12 1 5 9 2 12 1 5 9 2 12 1]
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_028.py
===================================== test session starts ======================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_028.py .                                                                   [100%]

=================================== 1 passed in 0.03 seconds ===================================
'''
