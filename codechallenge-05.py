'''
Date: 12/04/2018

Problem description:
===================

Given two non-empty linked lists representing two non-negative integers.  
The digits of the two numbers are stored in reversed order and each of their 
nodes contain a single digit.  i.e. (2 -> 4 -> 3) is number 342.  Add the 
two numbers and return it as a linked list.

You may assume the two numbers do not contain leading zero, except the 
number zero itself.  i.e. no 0342 but 304.

Approach:
-----------
Use addition technique taugh in elementary school.
Iterate through the linked lists and add the respective digits, 
Keep the carry over when the two digits adds up to more than 9.

'''

from collections import deque
import time
import unittest



class Node:

	def __init__(self,data,nextNode=None):
		self.data = data
		self.nextNode = nextNode

	def getData(self):
		return self.data

	def setData(self,val):
		self.data = val

	def getNextNode(self):
		return self.nextNode

	def setNextNode(self,val):
		self.nextNode = val

''' Singly linked list '''
class LinkedList:

	def __init__(self,head = None):
		self.head = head
		self.size = 0

	def getSize(self):
		return self.size

	def addNode(self,data):
		newNode = Node(data,self.head)
		self.head = newNode
		self.size+=1
		return True

	def popNode(self):
		curr = self.head
		if (self.head != None):
			self.head = curr.getNextNode()
			return curr.data
		else:
			return None


	def printNode(self):
		curr = self.head
		while curr:
			print(curr.data)
			curr = curr.getNextNode()

	def getNodes(self):
		ret = list()
		curr = self.head
		while curr:
			ret.append(curr.data)
			curr = curr.getNextNode()
		return ret


'''
Solution 1:
Implement using the class LinkedList above
Parameters: linkedlist l1, linkedlist l2
'''
def addDigitsInLinkedLists(l1, l2):
	result = LinkedList()
	carry = 0
	a = 0
	b = 0
	while a != None:
		a = l1.popNode()
		b = l2.popNode()
		if a != None:
			sum = a + b + carry
			carry = int(sum) % 10
			if (carry == 1 or sum == 10):
				result.addNode(0)
				carry = 1
			else:
				result.addNode(sum)
				carry = 0
	return result


			
	
'''
Solution 2:
Implement using module collections.deque
Parameters: deque l1, deque l2
'''
def addLinkedList(l1, l2):
	#assert len(l1) > 0
	#assert len(l2) > 0
	carry = 0
	a = b = 0
	resultLklst = deque()
	while len(l1) > 0:
		a = l1.pop()
		b = l2.pop()
		sum = a + b + carry
		carry = sum % 10
		if carry == 1 or sum == 10:
			resultLklst.append(0)
			carry = 1
		else:
			resultLklst.append(a+b)
			carry = 0
	return resultLklst


'''
Since unittest module is used here,
py.test would probably complain!
So, tests.py will fail here.
'''
def test_code(self):
	A = LinkedList()
	A.addNode(3)
	A.addNode(4)
	A.addNode(5)
	B = LinkedList()
	B.addNode(2)
	B.addNode(6)
	B.addNode(3)
	expret = LinkedList()
	expret.addNode(6)
	expret.addNode(0)
	expret.addNode(8)
	starttime = time.time()
	self.assertEqual(addDigitsInLinkedLists(A,B), expret)
	endtime = time.time()
	print("Elasped time = {}".format(endtime - starttime))

	#  ([3 -> 6 -> 5)] + ([2 -> 4 -> 3]) = ([6 -> 0 -> 8])
	lk1 = deque([3,6,5])
	lk2 = deque([2,4,3])
	retlklst = deque([6,0,8])

	starttime = time.time()
	self.assertEqual(addLinkedList(lk1, lk2), retlklst)
	endtime = time.time()
	print("Elasped time = {}".format(endtime - starttime))

	RET = addLinkedList(lk1, lk2)
	print(type(RET))
	for i in range(0, len(RET)):
		print(RET.pop())
		
if __name__ == "__main__":
	unittest.main()

	A = LinkedList()
	A.addNode(3)
	A.addNode(4)
	A.addNode(5)
	A.printNode()
	B = LinkedList()
	B.addNode(2)
	B.addNode(6)
	B.addNode(3)
	B.printNode()
	expret = LinkedList()
	expret.addNode(6)
	expret.addNode(0)
	expret.addNode(8)

	starttime = time.time()
	#assert addDigitsInLinkedLists(A,B) == expret 
	RET = addDigitsInLinkedLists(A,B) 
	endtime = time.time()
	print("Elasped time = {}".format(endtime - starttime))
	RET.printNode()

	#  ([3 -> 6 -> 5)] + ([2 -> 4 -> 3]) = ([6 -> 0 -> 8])
	lk1 = deque([3,6,5])
	lk2 = deque([2,4,3])
	retlklst = deque([6,0,8])

	starttime = time.time()
	RET = addLinkedList(lk1, lk2) 
	endtime = time.time()
	print("Elasped time = {}".format(endtime - starttime))

	RET = addLinkedList(lk1, lk2)
	print(type(RET))
	for i in range(0, len(RET)):
		print(RET.pop())
