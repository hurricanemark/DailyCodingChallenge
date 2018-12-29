'''
Date: 12/29/2018

Problem description:
===================
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. 
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.
'''

class linkedlistNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# add a node to end of linked list
def insertNode(head, val):
    currNode = head
    while currNode is not None:
        if currNode.next is None:
            currNode.next = linkedlistNode(val)
            return head
        currNode = currNode.next

# remove a node from linked list, needs work on head
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

# delete kth node in the linked list
def deleteKthNode(nodeA, k):
    while (nodeA is not None):
		if node.data == k:
			nodeA.next = nodeA.nex.next
			break
        nodeA = nodeA.next

