'''
Date: 12/29/2018

Problem description:
===================
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. 
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.


Algorithm:
=========
Input: A linked list
Output: A modified linked list
Psuedo code:
1.  Check edge cases
2.  Travese the linked list until value k is found
3.  Continue by calling a sub-function to travese the rest of the list for more matching k
4.  If more found, delete that last found node, else delete the currently matching k node

'''
from __future__ import print_function
class linkedlistNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
#
# add a node to end of linked list
#
def insertNode(head, val):
    currNode = head
    while currNode is not None:
        if currNode.next is None:
            currNode.next = linkedlistNode(val)
            return head
        currNode = currNode.next


#
# print linked list
#
def printNode(head):
    retstr = []
    curr = head
    while curr:
        retstr.append(str(curr.val))
        #print(curr.val)
        curr = curr.next

    print(' -> '.join(retstr))

#
# search for node.val == k in
# sub-linked list
#
def isMoreKnode(head, k):
    currNode = head
    currNode = currNode.next
    while currNode is not None:
        if currNode.val == k:
            return True
        currNode = currNode.next
    return False
    
# 
# Traverse the singly linked list to find 
# the last item matching k.
# If found one, call a look-ahead function
# to determine if more match is found further
# up the linked list.
# 
def deleteLastKthNode(head, k):
    currNode = head
    prevNode = None
    moreKNode = False
    while currNode is not None:
        if currNode.val == k:
            # found a match, let's see if there is more
            moreKNode = isMoreKnode(currNode, k)
            if moreKNode == False:
                #print("isMoreKnode:{}".format(moreKNode))

                # let's delete the last kth node
                if prevNode is None:
                    newHead = currNode.next
                    return newHead
                else:
                    prevNode.next = currNode.next
                    return head

        # progressing toward end of list 
        prevNode = currNode
        currNode = currNode.next
    return head


if __name__ == '__main__':
    node = linkedlistNode(3)
    insertNode(node,4)
    insertNode(node,9)
    insertNode(node,8)
    insertNode(node,3)
    insertNode(node,4)
    insertNode(node,7)
    k=4
    print("Original linked list: ", end='') 
    printNode(node)
    print("Deleting the last node having value: {}".format(k))
    deleteLastKthNode(node,k)
    print("Resulting linked list: ", end='')
    printNode(node)

'''
Run-time output:
===============
markn@raspberrypi3:~/devel/py-src/DailyCodeChallenge $ python codechallenge_015.py
Original linked list: 3 -> 4 -> 9 -> 8 -> 3 -> 4 -> 7
Deleting the last node having value: 4
Resulting linked list: 3 -> 4 -> 9 -> 8 -> 3 -> 7
'''
