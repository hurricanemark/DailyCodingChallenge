'''
Date: 2020-07-14

Problem statement:
==================
This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal(Root -> Left -> Right):

[a, b, d, e, c, f, g]

And the following inorder traversal(Left -> Root -> Right):

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g

So, using both traversals, we can build the tree above.  Wow!
Let's break it down:
-  Preorder traversal is the root, then the left-most node, then the right-most node.
    i.e. Root -> Left -> Right
    [a, b, d, e, c, f, g] --> Root: a, Left(preorder)Tree: [b,d,e], Right(preorder)Tree: [c,f,g]
-  Inorder traversal is the left-most node first, then the root, then the right-most node.
    i.e. Left -> Root -> Right
    [d, b, e, a, f, c, g] --> Left(inorder)Tree: [d,b,e], Root: a, Right(inorder)Tree: [f,c,g]
    
1.  Locate root and subtrees
preorder = [a, b, d, e, c, f, g]
    Preorder[0] = Root = a
    Preorder_LeftSubTree = [d, b, e]
    Preorder_RightSubTree = [c, f, g]

Inorder = [d, b, e, a, f, c, g]
    Inorder_Root = a
    Inorder_LeftSubTree = [d, b, e]
    Inorder_RightSubTree = [c, f, g]
    
2. Construct subTrees    
    Preorder_LeftSubTree = [b, d, e]
         a
        /
       b
      / \
     d   e            
    Preorder_RightSubTree = [c, f, g]
        a
         \   
          c
         / \
        f   g
    Inorder_LeftSubTree = [b, d, e]
         a
        / \
        b
       / \
      d   e      
            
'''

import unittest

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    # Insert Node
    def insert(self, data):
        if type(data) is str:
            if self.data:  # if the node is not empty
                if ord(data) < ord(self.data):
                    if self.left is None:
                        self.left = Node(data)
                    else:
                        self.left.insert(data)
                elif ord(data) > ord(self.data):
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
            else: # root
                self.data = data

        elif type(data) is int:    
            if self.data:  # if the node is not empty
                if data < self.data:
                    if self.left is None:
                        self.left = Node(data)
                    else:
                        self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
            else: # root
                self.data = data
            
    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data), 
        if self.right:
            self.right.PrintTree()
            
    # Preorder traversal
    def preorderTraversal(self, root):
        if root:
            print(root.data),
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)

    # Inorder traversal
    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.data),
            self.inorderTraversal(root.right)            

# Inorder traversal
def inorderInsert(root):
    if root:
        inorderInsert(root.left)
        print(root.data, end = ' ')
        inorderInsert(root.right)

# Preorder traversal
def preorderInsert(root):
    if root:
        print(root.data, end = ' ')
        preorderInsert(root.left)
        preorderInsert(root.right)
    
# Build tree
def buildTree(preorder, start, end):
    # base case
    if start > end:
        return None
    node = Node(preorder[start])
    
    i = start
    while i <= end:
        if type(preorder[i]) is str:
            if ord(preorder[i]) > ord(node.data):
                break
        elif type(preorder[i]) is int:
            if preorder[i] > node.data:
                break
        i = i + 1            
    node.left = buildTree(preorder, start + 1, i - 1)
    node.right = buildTree(preorder, i, end)
    
    return node


class TestBuldTree(unittest.TestCase):
    def test_buildTree(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        
                              
if __name__ == '__main__':
    # test 1 
    preorderData = [15, 10, 8, 12, 20, 16, 25]
    root = buildTree(preorderData, 0, len(preorderData) - 1)
    print ('Test#1 Inorder traversal: ', end = '')
    inorderInsert(root)
    
    # test 2
    print()
    preorderData = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
    root = buildTree(preorderData, 0, len(preorderData) - 1)
    print ('Test#2 Inorder traversal: ', end = '')
    inorderInsert(root)
    
    # test 3
    print()
    inorderData = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
    root = buildTree(preorderData, 0, len(preorderData) - 1)
    print ('Test#3 Preorder traversal: ', end = '')
    preorderInsert(root)


'''
Run-time output:
===============
Test#1 Inorder traversal: 8 10 12 15 16 20 25 
Test#2 Inorder traversal: a b d c e f g 
Test#3 Preorder traversal: a b d e c f g 
'''

