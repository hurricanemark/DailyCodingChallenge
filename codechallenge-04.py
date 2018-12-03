'''
Date: 12/03/2018
Prolem description:
==================
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
''' 

'''
Pseudo code:
1.  Sort the array and remove duplicates
2.  Shorten the array by eliminate elements having negative value.
3.  Traverse the array comparing index to its value.  The missing number should be last value+1.  Return the first missing number.
    Note, zero is neither negative or positive, so in step two, eliminate element with value zero as well.
    
    Altenatively, the array can be converted into a dictionary, then determine the firt pair that key != value.


Performance wise, there is no appreciative difference between the three functions since it is in the order O(n)

Ways to shave on performance:
- split the array and search first half, then second half
'''


def findFirstMissing(arr):
	if len(arr) == 0:
		return None
	else:
		# sort, remove duplicates
		arr = list(set(arr))
		# remove negative values from the array 	
		arr = [n for n in arr if n > 0] 

		# use list comprehesion to get the first missing number
		# this yields a list instead of sing number. Hmmm...
		missing = [arr[i-1]+1 for i, val in enumerate(arr) if val > arr[i-1]+1]
		print(missing[0])
		return missing[0]

def firstMissingValA(arr):
	if len(arr) == 0:
		return None
	else:
		# sort, remove duplicates
		arr = list(set(arr))
		# remove negative values from the array 	
		arr = [n for n in arr if n > 0] 

		# use iterative loop
		for i,n in enumerate(arr):
			print("idx:{} val:{}".format(i,n))
			if (n > arr[i-1]+1):
				missing = arr[i-1]+1
				print(missing)
				break
	return missing

def firstMissingValB(arr):
	if len(arr) == 0:
		return None
	else:
		# sort, remove duplicates
		arr = list(set(arr))
		# remove negative values from the array 	
		arr = [n for n in arr if n > 0] 

		# use ditionary to get to the missing number
		dArr = { i+1 : arr[i] for i in range(0, len(arr) ) }
		for k,v in dArr.items():
			if k != v:
				missing = k
				print("k:{} v:{}  missing:{}".format(k, v, missing))
				break
	return missing

def test_missingvalue():
	missing = 13
	A = list(range(-20, missing))
	A.append(missing+2)
	A.append(missing+20)
	assert findFirstMissing(A) == missing 
	assert firstMissingValA(A) == missing 
	assert firstMissingValB(A) == missing 

if __name__ == "__main__":
	A = list(range(-5,5))
	A.append(10)
	test_missingvalue(A)
	firstMissingValA(A)
	firstMissingValB(A)
