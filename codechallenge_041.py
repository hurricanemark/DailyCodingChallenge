'''
Date: 01/28/2019

Task description:
=================
This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, 
since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it 
up into two subsets that add up to the same sum.



Algorithm:
==========
Input: A set of integers
Output: A boolean

Psuedo code:

1.  Validate input
2.  Let's convert set to list for easier manipulation
3.  Generate a function to yield every posible sublists of the given list
4.  For each subset, calculate sum and store in a list called sums.
5.  Determine if there are dupplicates in sums, if so return True, else False


'''

#
# generator that yields possible combinations of two sub-lists
# where elements of the combined two sublists should 
# be that of the original list
#
def gen_sublist(L=[]):
	start, end = 0, len(L)
	x_end = end
	sub_list = []
	while start < end -1:
		sub_listA = L[start:x_end]
		x_end -= 1
		sub_listB = L[x_end+1:end] + L[:start]

		yield sub_listA, sub_listB
	
		if x_end < start + 1:
			start += 1
			x_end = end


#
# return True if the multiset can be broken up into subsets
#
def isSubset_able(S={}):
	# conver set into list
	L = list(S)
	if len(L) == 0:
		return False

	lists_A_B = gen_sublist(L)
	for sublist in lists_A_B:
		print("DBUG-- L1:{} L1_SUM:{} -- L2:{} L2_SUM:{}".format(sublist[0], sum(sublist[0]), sublist[1], sum(sublist[1])))
		if sum(sublist[0]) == sum(sublist[1]):
			print("\nYES ==> L1:{} L1_SUM:{} -- L2:{} L2_SUM:{}".format(sublist[0], sum(sublist[0]), sublist[1], sum(sublist[1])))
			return True
	return False


#
# client program
#
def main():
	mySet = {15, 5, 20, 10, 35, 15, 10}
	print("\nTest1:")
	print("Can it be broken into subsets?: {}".format(isSubset_able(mySet)))
	mySet = {15, 5, 20, 10, 35}
	print("\nTest2:")
	print("Can it be broken into subsets?: {}".format(isSubset_able(mySet)))


if __name__ == '__main__':
	main()


'''
Run-time output:
================

(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_041.py

Test1:
DBUG-- L1:[35, 5, 10, 15, 20] L1_SUM:85 -- L2:[] L2_SUM:0
DBUG-- L1:[35, 5, 10, 15] L1_SUM:65 -- L2:[20] L2_SUM:20
DBUG-- L1:[35, 5, 10] L1_SUM:50 -- L2:[15, 20] L2_SUM:35
DBUG-- L1:[35, 5] L1_SUM:40 -- L2:[10, 15, 20] L2_SUM:45
DBUG-- L1:[35] L1_SUM:35 -- L2:[5, 10, 15, 20] L2_SUM:50
DBUG-- L1:[5, 10, 15, 20] L1_SUM:50 -- L2:[35] L2_SUM:35
DBUG-- L1:[5, 10, 15] L1_SUM:30 -- L2:[20, 35] L2_SUM:55
DBUG-- L1:[5, 10] L1_SUM:15 -- L2:[15, 20, 35] L2_SUM:70
DBUG-- L1:[5] L1_SUM:5 -- L2:[10, 15, 20, 35] L2_SUM:80
DBUG-- L1:[10, 15, 20] L1_SUM:45 -- L2:[35, 5] L2_SUM:40
DBUG-- L1:[10, 15] L1_SUM:25 -- L2:[20, 35, 5] L2_SUM:60
DBUG-- L1:[10] L1_SUM:10 -- L2:[15, 20, 35, 5] L2_SUM:75
DBUG-- L1:[15, 20] L1_SUM:35 -- L2:[35, 5, 10] L2_SUM:50
DBUG-- L1:[15] L1_SUM:15 -- L2:[20, 35, 5, 10] L2_SUM:70
Can it be broken into subsets?: False

Test2:
DBUG-- L1:[35, 5, 10, 15, 20] L1_SUM:85 -- L2:[] L2_SUM:0
DBUG-- L1:[35, 5, 10, 15] L1_SUM:65 -- L2:[20] L2_SUM:20
DBUG-- L1:[35, 5, 10] L1_SUM:50 -- L2:[15, 20] L2_SUM:35
DBUG-- L1:[35, 5] L1_SUM:40 -- L2:[10, 15, 20] L2_SUM:45
DBUG-- L1:[35] L1_SUM:35 -- L2:[5, 10, 15, 20] L2_SUM:50
DBUG-- L1:[5, 10, 15, 20] L1_SUM:50 -- L2:[35] L2_SUM:35
DBUG-- L1:[5, 10, 15] L1_SUM:30 -- L2:[20, 35] L2_SUM:55
DBUG-- L1:[5, 10] L1_SUM:15 -- L2:[15, 20, 35] L2_SUM:70
DBUG-- L1:[5] L1_SUM:5 -- L2:[10, 15, 20, 35] L2_SUM:80
DBUG-- L1:[10, 15, 20] L1_SUM:45 -- L2:[35, 5] L2_SUM:40
DBUG-- L1:[10, 15] L1_SUM:25 -- L2:[20, 35, 5] L2_SUM:60
DBUG-- L1:[10] L1_SUM:10 -- L2:[15, 20, 35, 5] L2_SUM:75
DBUG-- L1:[15, 20] L1_SUM:35 -- L2:[35, 5, 10] L2_SUM:50
DBUG-- L1:[15] L1_SUM:15 -- L2:[20, 35, 5, 10] L2_SUM:70
Can it be broken into subsets?: False


'''
