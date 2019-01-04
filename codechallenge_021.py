'''
Date: 01/05/2019

Problem description:
===================
This problem was asked by Dropbox.
Given the root to a binary search tree, find the second largest node in the tree.


       [6]      [6]      [6] 
       / \        \      / \
     [5] [7]      [9]  [5] [8]
                  / \        \
                [8] [10]    [10]

Algorithm:
=========
Input: Root of a binary search tree
Output: Node of second to right most.
Psuedo code:
	Binary Search Tree inherently contains sorted data.
1.	Write the BST constructor, add function, print function
2.	We will search for two cases 
	2.1  If root is None return None
	2.2  If root->right->right is None, return root->data


After thoughts:
==============
Try to assign and return an array of values in a recursive function
and you will be surprised what will come out.  For example, if you initialized
a list in the print_tree(self) function and append data to it.  The index of
your list may be recursively retro to zero each time the function called itself.
Haha!
'''

class BSTNode:
	def __init__(self, data, right=None, left=None):
		self.data = data
		self.right = right
		self.left = left

	def add(self, data):
		if self.data:
			if data < self.data:
				# left branches
				if self.left is None:
					self.left = BSTNode(data)
				else:
					self.left.add(data)
			elif data > self.data:
				# right branches
				if self.right is None:
					self.right = BSTNode(data)
				else:
					self.right.add(data)
		else:
			# root
			self.data = data

	def print_tree(self):
		# in-order traversal: left-root-right
		if self.left:
			self.left.print_tree()
		print ("{} ".format(self.data)),
		if self.right:
			self.right.print_tree()

	def get_second_last_right(self):
		if self.data is None:
			print(None)
			return None
		# traverse only the right sub tree
		if self.right:
			if self.right.right is None:
				print(self.data)
				return self.data
			self.right.get_second_last_right()


def run_test(root):
	print("Given a binaray search tree having data:")
	root.print_tree()	
	print("\nSecond largest value in the BST is:")
	root.get_second_last_right()
	
if __name__ == '__main__':
	node = BSTNode(8)
	node.add(5)
	node.add(7)
	node.add(9)
	node.add(10)
	node.add(17)
	node.add(19)
	run_test(node)
	xNode = BSTNode(None)
	run_test(xNode)




'''
Run-time output:
===============
Given a binaray search tree having data:
5  7  8  9  10  17  19  
Second largest value in the BST is:
17
Given a binaray search tree having data:
None  
Second largest value in the BST is:
None
'''

