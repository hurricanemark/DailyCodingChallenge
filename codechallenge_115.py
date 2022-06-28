'''
Date: 05/04/2022

Problem description:
=====================
This problem was asked by Amazon.

Huffman coding is a method of encoding characters based on their frequency. 
Each letter is assigned a variable-length binary string, such as 0101 or 111110, 
where shorter lengths correspond to more common letters. To accomplish this, a 
binary tree is built such that the path from the root to any leaf uniquely maps 
to a character. When traversing the path, descending to a left child corresponds 
to a 0 in the prefix, while descending right corresponds to 1.

Here is an example tree (note that only the leaf nodes have letters):

        *
      /   \
    *       *
   / \     / \
  *   a   t   *
 /             \
c               s

With this encoding, cats would be represented as 0000110111.

i.e. Traversing starting from the root node
    c = left.left.left --> 000
    a = left.left.right --> 01
    t = right.left --> 10
    s = right.right.right --> 111

frequencies = {'c':'000','a':'01','t':'10','s':'111'}

Given a dictionary of character frequencies, build a Huffman tree, and use it to 
determine a mapping between characters and their encoded binary strings.

Algorithm:
===========
There are mainly two major parts in Huffman Coding

1. Build a Huffman Tree from input characters.
2. Traverse the Huffman Tree and assign codes to characters.

Steps to build Huffman Tree:
=============================
Input is an array of unique characters along with their frequency of occurrences 
and output is Huffman Tree. 

1. Create a leaf node for each unique character and build a min heap of all leaf 
nodes (Min Heap is used as a priority queue. The value of frequency field is used 
to compare two nodes in min heap. Initially, the least frequent character is at root)

2. Extract two nodes with the minimum frequency from the min heap.
 
3. Create a new internal node with a frequency equal to the sum of the two nodes 
frequencies. Make the first extracted node as its left child and the other extracted 
node as its right child. Add this node to the min heap.

4. Repeat steps#2 and #3 until the heap contains only one node. The remaining node is 
the root node and the tree is complete.

Notes:
======
Applications of Huffman Coding:
-  They are used for transmitting fax and text.
-  They are used by conventional compression formats like PKZIP, GZIP, etc.
-  Multimedia codecs like JPEG, PNG, and MP3 use Huffman encoding(to be more precise the prefix codes).
'''
    
from binarytree import Node
        
# A Huffman Tree Node
class node:
	def __init__(self, freq, symbol='', left=None, right=None):
		# frequency of symbol
		self.freq = freq

		# symbol name (character)
		self.symbol = symbol

		# node left of current node
		self.left = left

		# node right of current node
		self.right = right

		# tree direction (0/1)
		self.huff = ''
    
#
# build Huffman tree using binarytree library
#
def build_huffman_code(Hdict):
    root = Node('*')
    next = root
    #frequencies = {'c':'000','a':'01','t':'10','s':'111'}
    for value in Hdict.values():
        for x in value:
            if x == '0':
                next.left = Node('*')
                
            elif x == '1':
                next.right = Node('*')
                

def insert_huffman_tree(root, key, value):
    list(key)
    if root is None:
        root = Node(value)
    else:
        if key == '0':
            root.left = Node(value)
    

# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree


def printNodes(node, val=''):
	# huffman code for current node
	newVal = val + str(node.huff)

	# if node is not an edge node
	# then traverse inside it
	if(node.left):
		printNodes(node.left, newVal)
	if(node.right):
		printNodes(node.right, newVal)

    # if node is edge node then
    # display its huffman code
	if(not node.left and not node.right):
		print(f"{node.symbol} -> {newVal}")


def build_huffman_tree(Hdict):
    hNodes = []
    for key, value in Hdict.items():
        for x in list(value):
            if x == '0':
                hNodes.append(node(value, key, None, x))
            elif x == '1':
                hNodes.append(node(1, '*', None, node.right))
            
        
    while len(hNodes) > 1:
        # sort all the nodes in ascending order
        # based on their frequency
        hNodes = sorted(hNodes, key=lambda x: x.freq)

        # pick 2 smallest nodes
        left = hNodes[0]
        right = hNodes[1]

        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # combine the 2 smallest nodes to create
        # new node as their parent
        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
        print(newNode.freq)
        # remove the 2 nodes and add their
        # parent as new node among others
        hNodes.remove(left)
        hNodes.remove(right)
        hNodes.append(newNode)
    # Huffman Tree is ready!
    printNodes(hNodes[0])
    
def insert(root, val, key):
    if root is None:
        return Node(key)
    else:
        if root.val == '1':
            root.right = insert(root.right, key)
        elif root.val == '0':
            root.left = insert(root.left, key)
    return root

#
# build Huffman tree using binarytree library
#    
def test_cats():
    # chars = ['c','a','t','s']
    # freq = ['000','01','10','111']
    # frequencies = {'c':'000','a':'01','t':'10','s':'111'}
    
    # val = '*'
    # root = Node(val)
    # for key, value in frequencies.items():
        
    #     [insert(root, x, val) for x in value, if x == '0':  val = '*', else x == '1': val = '*']
    #     # replase last insertion with key
    #     insert(root, x, key)
        
    root = Node('*')
    root.left = Node('*')
    root.left.right = Node('a')
    root.left.left = Node('*')
    root.left.left.left = Node('c')
    
    root.right = Node('*')
    root.right.left = Node('t')
    root.right.right = Node('*')
    root.right.right.right = Node('s')
    
    print(root)    
    
def main():
    
    # characters for huffman tree
    chars = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # frequency of characters
    freq = [5,9,12,13,16,45,48,51,55,62,66,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190]

    # list containing unused nodes
    nodes = []

    # converting characters and frequencies
    # into huffman tree nodes
    for x in range(len(chars)):
        nodes.append(node(freq[x], chars[x]))

    while len(nodes) > 1:
        # sort all the nodes in ascending order
        # based on their frequency
        nodes = sorted(nodes, key=lambda x: x.freq)

        # pick 2 smallest nodes
        left = nodes[0]
        right = nodes[1]

        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # combine the 2 smallest nodes to create
        # new node as their parent
        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

        # remove the 2 nodes and add their
        # parent as new node among others
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    # Huffman Tree is ready!
    printNodes(nodes[0])
    print()


if __name__ == '__main__':
    print('Huffman Tree by (geeksforgeeks.org):\n')
    # main()
    test_cats()
    # frequencies = {'c':'000','a':'01','t':'10','s':'111'}
    # build_huffman_tree(frequencies)