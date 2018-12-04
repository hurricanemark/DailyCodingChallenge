'''
Date: 11/30/2018
This problem was asked by Google.

Problem description:
-------------------
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''

import random, time

'''
Brute force using nested loop
'''
def isSumOfK(nums, k):
	# keep elements in nums that are less than k
	nums.sort()
	nums = [n for n in nums if n < k]

	for i in range(len(nums),-1,-1):
		for idx, val in reversed(list(enumerate(nums))):
			if idx > i:
				if val < k and (nums[i]+val)==k:
					return True

	return False

'''
Bonus:
The objective is to do the function in one pass.
'''
def isSumEqualK(nums, k):
	nums.sort()
	num = [n for n in nums if n < k]
	for i in range(0, len(nums)):
		# cheating it by iterate over range of nums in this if statement
		if k - nums[i] in nums: 
			return True
	return False

'''
tests
'''
def test_BruteForceCode():
	try:	
		start = time.time()
		nums = [4,20,15,3,72,2,7,90,8,7,9,10,22]
		k = 28
		assert isSumOfK(nums,k) == True
		end = time.time()
		print("Elapsed time: {}".format(end-start))

		nums = random.sample(range(1,1000),50)
		k=nums[0]+nums[-1] #this ensure the test returns True
		assert isSumOfK(nums,k) == True
	except:
		print("\tLogical condition tests failed on isSumOfK()==True!")

	try:	
		nums = [4,20,15,3,72,2,7,90,8,7,9,10,22]
		k=1000
		assert isSumOfK(nums,k) == False
	except:
		print("\tLogical condition tests failed on isSumOfK()==False!")


def test_BonusCode():
	try:
		start = time.time()
		nums = [4,20,15,3,72,2,7,90,8,7,9,10,22]
		k = 28
		assert isSumEqualK(nums, k) == True
		end = time.time()
		print("Elapsed time: {}".format(end-start))

		k=nums[0]+nums[-1] #this ensures the test returns True
		assert isSumEqualK(nums, k) == True
	except AssertionError:
		print("\tLogical condition tests failed on isSumEqualK()==True!")
		
	try:
		k = 1000
		assert isSumEqualK(nums, k) == False
	except AssertionError:
		print("\tLogical condition tests failed on isSumEqualK()==False!")


if __name__ == "__main__":
	print("Test function isSumOfK:")
	test_BruteForceCode()


	print("\nTest function isSumEqualK  --(one pass solution):")
	test_BonusCode()
