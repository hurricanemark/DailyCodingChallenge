'''
This problem was asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''

import random

'''
Bruce force using nested loop
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
Better solution
'''
def isSumEqualK(nums, k):
    nums.sort()
    num = [n for n in nums if n < k]
    for i in range(0, len(nums)):
	# n + x = k and x = k - n
        if k - nums[i] in nums:
            return True
    return False  


def test_code():
	nums = [4,20,15,3,72,2,7,90,8,7,9,10,22]
	k = 28
	assert isSumOfK(nums,k) == True

	k=1000
	assert isSumOfK(nums,k) == False

	nums = random.sample(range(1,1000),50)
	k=nums[1]+nums[-1]
	assert isSumOfK(nums,k) == True

	nums = [4,20,15,3,72,2,7,90,8,7,9,10,22]
	k = 28
	assert isSumEqualK(nums, k) == True

	nums = [4,20,15,3,72,2,7,90,8,7,9,10,22]
	k = 28
	assert isSumEqualK(nums, k) == True
	k=1000
	assert isSumEqualK(nums, k) == False


if __name__ == "__main__":
	nums = [4,20,15,3,72,2,7,90,8,7,9,10,22]
	k = 28
	print("Test True case:")
	print(isSumOfK(nums,k))

	print("Test False case:")
	k=1000
	print(isSumOfK(nums,k))

	print("Test using random generator case:")
	nums = random.sample(range(1,1000),50)
	k=nums[1]+nums[-1]
	print(isSumOfK(nums,k))

	test_bettercode()
