'''
Date: 01/01/2019

Problem description:
===================
This problem was asked by Microsoft.
Compute the running median of a sequence of numbers. That is, given a stream of numbers, 
print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
2
1.5
2
3.5
2
2
2


Algorithm:
=========
Input: A list of numbers
Output: a sequnce of numbers
Pseudo code:
1.  Check for valid input
2.  Traverse the list,
    for each new element, sort the traversed elements to find the median
3.  print out the middle element if odd-numbered list
    else print the average of the two middle elements if it is an even-numbered list
'''


from __future__ import division
def runningMedian(nums=[]):
	if len(nums) == 0:
		return None
	if len(nums) == 1:
		return nums[0]

	growinglist = []
	for n in nums:
		if n == 0:
			print(n)
		growinglist.append(n)
		growinglist.sort()
		mid_idx = len(growinglist)//2
		median = 0 

		'''
		dbugstr = ','.join(str(n) for n in growinglist)
		print("DBUG-- Array:{}  mid_idx:{}".format(dbugstr, mid_idx))
		'''

		if len(growinglist) == 1:
			median = growinglist[0]
		elif len(growinglist) % 2 == 0:
			#even-numbered list
			median = (growinglist[mid_idx] + growinglist[mid_idx-1]) / 2
		else:
			#odd-numbered list
			median = growinglist[mid_idx]	

		print(median)

if __name__ == '__main__':
	Arr = [2, 1, 5, 7, 2, 0, 5]
	runningMedian(Arr)
'''
Run-time output:
===============
2
1.5
2
3.5
2
0
2.0
2
'''

