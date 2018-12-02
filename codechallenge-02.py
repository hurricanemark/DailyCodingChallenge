'''
Date: 12/01/2018

This problem was asked by Uber.

Problem description:
===================
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
'''

# This implementation uses nested loop and the manipulation of slicing index 
# Not a good performance code because the entire range gets traversed.
# Note that I don't use division.
def doit(a):
	p=[]
	for i in range(len(a)):
		prod=1
		#for x, n in enumerate(range(0, len(a))):
		for x in range(0, len(a)):
			if x != i:
				prod=prod*a[x]
			#print("i={} x={} n={} prod={}".format(i,x,a[x], prod))
		#print(prod)
		p.append(prod)
		pro=1
	print(p)
	return p

def test_code():
	nums=[3, 2, 1]
	assert doit(nums) == [2,3,6]
	nums=list(range(1,6))
	assert doit(nums) == [120,60,40,30,24]

if __name__ == "__main__":
	test_code()
