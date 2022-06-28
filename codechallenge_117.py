'''
Date: 05/08/2022

Problem description:
====================
Build an inorder binary tree from a preorder and inorder traversal.

Algorithm:
===========
Inorder traversal
-----------------
1.  Traverse the left subtree
2.  Visit the root
3. Traverse the right subtree
Use cases: In the case of binary search trees (BST), Inorder traversal gives 
nodes in non-decreasing order. To get nodes of BST in non-increasing order, 
a variation of Inorder traversal where Inorder traversal s reversed can be used. 


Preorder traversal
----------------
1. Visit the root
2. Traverse the left subtree
3. Traverse the right subtree
Use cases: Preorder traversal is used to create a copy of the tree. Preorder 
traversal is also used to get prefix expression on an expression tree. 
Please see http://en.wikipedia.org/wiki/Polish_notation know why prefix expressions are useful. 

Postorder traversal
-----------------
1. Traverse the left subtree
2. Traverse the right subtree
3. Visit the root
Use cases: Postorder traversal is used to delete the tree. Please see the question 
for the deletion of a tree for details. Postorder traversal is also useful to get 
the postfix expression of an expression tree. 
Please see http://en.wikipedia.org/wiki/Reverse_Polish_notation for the usage of postfix expression.

'''
from binarytree import Node

# Python program to for tree traversals

# A class that represents an individual node in a
# Binary Tree


class binarytreeNode:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do inorder tree traversal
def printInorder(root):

	if root:

		# First recur on left child
		printInorder(root.left)

		# then print the data of node
		print(root.val),

		# now recur on right child
		printInorder(root.right)


# A function to do postorder tree traversal
def printPostorder(root):

	if root:

		# First recur on left child
		printPostorder(root.left)

		# the recur on right child
		printPostorder(root.right)

		# now print the data of node
		print(root.val),


# A function to do preorder tree traversal
def printPreorder(root):

	if root:

		# First print the data of node
		print(root.val),

		# Then recur on left child
		printPreorder(root.left)

		# Finally recur on right child
		printPreorder(root.right)


def buildBtreeWithNodeLib():
    hHeap = Node('*')
    hHeap.left = Node('*')
    hHeap.left.right = Node('a')
    hHeap.left.left = Node('*')
    hHeap.left.left.left = Node('c')
    hHeap
    hHeap.right = Node('*')
    hHeap.right.left = Node('t')
    hHeap.right.right = Node('*')
    hHeap.right.right.right = Node('s')
    print(hHeap)
    
              
#
# main driver
#
def main():

    root = binarytreeNode([1,5,2,9,4,9])
    print ("Preorder traversal of binary tree is")
    printPreorder(root)

    print ("\nInorder traversal of binary tree is")
    printInorder(root)

    print ("\nPostorder traversal of binary tree is")
    printPostorder(root)

    print("\nBuilding a binary tree with Node library")
    buildBtreeWithNodeLib()

if '__main__' == __name__:
    main()