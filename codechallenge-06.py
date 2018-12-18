'''
Date: 12-17-2018
Problem description:
===================
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, 
we should get: [10, 7, 8, 8], since:
	10 = max(10, 5, 2)
	7 = max(5, 2, 7)
	8 = max(2, 7, 8)
	8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place 
and you do not need to store the results. 
You can simply print them out as you compute them.
'''


import time

'''brute force'''
def maxValInArray(arr, k):
	''' check edge case '''
	assert k >= 1
	assert k <= len(arr)

	if k == 1:
		#print( arr )
		return arr
	else:
		subarr = list()
		listofmax = list()

		while (len(arr) >= k):
			x = 0
			for x in range(x, (k+x)):
				subarr.append(arr[x])
			#listofmax.append(sorted(subarr, reverse=True)[:1])
			listofmax.append(max(subarr))
			subarr = []
			arr.pop(0)

		#print (listofmax)
		return listofmax
			

''' O(n) time and O(k) space '''
def maxValsList(arr, k):
	''' check edge case '''
	assert k >= 1
	assert k <= len(arr)

	if k == 1:
		#print( arr )
		return arr
	else:
		retarr = list()
		while len(arr) >= k:
			#print(max([a[i] for i in range(k)]))
			retarr.append(max([arr[i] for i in range(k)]))
			arr.pop(0)

		return retarr


def test_code():
	A = [10, 5, 2, 7, 8, 7]
	K = 3
	assert maxValInArray(A, K) == [10, 7, 8, 8] 

	A = [10, 5, 2, 7, 8, 7]
	assert maxValsList(A, K) == [10, 7, 8, 8]

	A = [10, 5, 2, 7, 8, 7]
	K = 1
	assert maxValsList(A, K) == [10, 5, 2, 7, 8, 7]
if __name__ == "__main__":
	A = [10, 5, 2, 7, 8, 7]
	K = 3

	print ("Original array: {}".format(A))
	starttime = time.time()
	print( maxValInArray(A, K)) 
	endtime = time.time()
	print("Elapsed time in brute force methob: {} secs".format(endtime - starttime))

	A = [10, 5, 2, 7, 8, 7]
	starttime = time.time()
	print( maxValsList(A, K))
	endtime = time.time()
	print("Elapsed time in O(n) method: {} secs".format(endtime - starttime))
	
