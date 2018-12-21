'''
Date: 12/20/2018

Problem description:
===================
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given 
A = 3 -> 7 -> 8 -> 10 and 
B = 99 -> 1 -> 8 -> 10, 
return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''



from __future__ import print_function
class linkedlistNode:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

def insertNode(head, val):
	currNode = head
	while currNode is not None:
		if currNode.next is None:
			currNode.next = linkedlistNode(val)
			return head
		currNode = currNode.next

def deleteNode(head, value):
	currNode = head
	prevNode = None
	while currNode is not None:
		if currNode.val == value:
			if prevNode is None:
				newHead = currNode.next
				return newHead
			prevNode.next = currNode.next
			return head
		prevNode = currNode
		currNode = currNode.next
	return head

def printNodes(nodeA):
	S=[]
	while (nodeA is not None):
		S.append(str(nodeA.val))
		nodeA = nodeA.next
	print(' -> '.join(S))

def findIntersectedNode(nodeA, nodeB):
	currNodeA = nodeA
	currNodeB = nodeB
	while currNodeA is not None or currNodeB is not None:
		if currNodeA.val == currNodeB.val:
			return currNodeA.val
		currNodeA = currNodeA.next
		currNodeB = currNodeB.next

def test_code():
	A = linkedlistNode(3)
	insertNode(A, 7)
	insertNode(A, 8)
	insertNode(A, 10)
	B = linkedlistNode(99)
	insertNode(B, 1)
	insertNode(B, 8)
	insertNode(B, 10)

	assert findIntersectedNode(A,B) == 8

if __name__ == "__main__":
	print("Given\nA singly linked list A: ", end='')
	# A = 3 -> 7 -> 8 -> 10 
	A = linkedlistNode(3)
	insertNode(A, 7)
	insertNode(A, 8)
	insertNode(A, 10)
	printNodes(A)


	# B = 99 -> 1 -> 8 -> 10
	print("And a singly linked list B: ", end='')
	B = linkedlistNode(99)
	insertNode(B, 1)
	insertNode(B, 8)
	insertNode(B, 10)
	printNodes(B)

	print("The intersected node in these linked lists A, B is {}".format(findIntersectedNode(A,B)))
