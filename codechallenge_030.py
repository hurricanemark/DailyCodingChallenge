'''
Date: 01/12/2019

Problem description:
===================
This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has. 
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller 
element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] 
has three inversions: (2, 1), (4, 1), and (4, 3). 
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

'''
#
# O(N*2) time algorithm
#
def inversion_count(L=[]):
	if len(L) == 0:
		return None
	cnt = 0
	for i in range(len(L)):
		for j in range(i, len(L)):
			if L[i] > L[j]:
				cnt +=1
	return cnt

'''
playing ...
def sublist(L=[]): return [L[i:] for i in range(len(L)-1)]
def shiftlist(L,shift=1): return [L[-shift:]] + L[:-shift]
def comp(s=()): return s[0] > s[1]
'''

def test_inversion_count():
	arr = [5,4,3,2,1]
	assert inversion_count(arr) == 10

def main():
	arr = [2, 4, 1, 3, 5]
	print("Test1:\nGive array: [{}]".format(', '.join(str(s) for s in arr)))
	print("The inversion count is {}".format(inversion_count(arr)))
	arr = [5,4,3,2,1]
	print("\nTest2:\nGive array: [{}]".format(', '.join(str(s) for s in arr)))
	print("The inversion count is {}".format(inversion_count(arr)))

if __name__ == '__main__':
	main()

'''
Run-time output:
===============
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_030.py
Test1:
Give array: [2, 4, 1, 3, 5]
The inversion count is 3

Test2:
Give array: [5, 4, 3, 2, 1]
The inversion count is 10
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_030.py
=============================== test session starts ===============================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_030.py .                                                      [100%]

============================ 1 passed in 0.06 seconds =============================
'''
