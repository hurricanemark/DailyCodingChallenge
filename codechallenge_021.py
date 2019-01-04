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
	Since the left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
	We will search for two cases 
1.  If root is None return None
2.  If node->next is None, return previous node
'''

class BSTNode:
	def __init__(self, data, right=None, left=None):
		self.data = data
		self.right = right
		self.left = left

	def add(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = BSTNode(data)
				else:
					self.left.add(data)
			elif data > self.data:
				if self.right is None:
					self.right = BSTNode(data)
				else:
					self.right.add(data)
		else:
			self.data = data

	def print_tree(self):
		# in-order traversal
		if self.left:
			self.left.print_tree()
		print ("{} ".format(self.data)),
		if self.right:
			self.right.print_tree()

	def get_second_last_right(self):
		# traverse only the right sub tree
		if self.right:
			if self.right.right is None:
				print(self.data)
				return self.data
			self.right.get_second_last_right()




node = BSTNode(8)
node.add(5)
node.add(7)
node.add(9)
node.add(10)
node.add(17)
node.add(19)

print("Given a binaray search tree having data:")
node.print_tree()	
print("\nSecond largest value in the BST is:")
node.get_second_last_right()
