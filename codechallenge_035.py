'''
Date: 10/18/2019

Problem description:
===================
This problem was asked by Microsoft.
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.
Given the root to such a tree, write a function to evaluate it.
For example, given the following tree:
    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).

Algorithm:
==========
!!! WARNING:  This is a complex, time consuming interview question.

Assume the tree is not ballanced.  Hence, expect expressions such as 3*4+5 or 3-2+4+5 or 3*4+5*6. 
The root determines where to place the parenthesis.
Topdown tasks: 
	On whiteboard, make the assumption that the rooted tree exists (to save time)
	1. Retrieve
	2. Parse
	3. Evaluate
	Here, we have to construct the tree, fill it before we can get the answer out.
	1. Construct class Tree
	2. Fill
	3. Retrieve
	4. Parse
	5. Evaluate	

Input: a rooted tree containing a mathematical expression
Output: A numer
 
Pseudo code:
1.  Construct a root tree class including insert method
2.  Write a function to traverse and return a string representing the mathematical expression
3.  Import modules SymPy
4.  Write a function to evaluate the string expression

'''            

import sympy

def demo_eval_expr(my_expr=[]):

	# define a whitelist of symbols
	a, b, c, d = sympy.symbols('a b c d')

	# let say my_expr = "(2 + 5) * (3 + 9)"
	# construct d_expr = {a:2, b:5, c:3, d:9}
	
	return int(sympy.sympify("(a + b) * (c + d)").evalf(subs={a:2, b:5, c:3, d:9})) 

print(demo_eval_expr())

