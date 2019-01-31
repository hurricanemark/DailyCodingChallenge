'''
Date: 01/31/2019

Task description:
=================
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns 
whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. 
Similarly, given the target word 'MASS', you should return true, since it's the last row.



Algorithm:
==========
Input: A 2D matrix of single characters, and a string
Output: A booean value

Psuedo code:

1.  Validate input
2.  Choose the shorter dimension to traverse.  
    If row is shorter than column, go up-to-down
    Else if column is shorter, go left-to-right
3.  Join each sub-list to upper-case string.  
    Use the `in list` syntax to match with target string 
4.  For better performance, perhaps wrap step#3 in a insertion list search.


'''


# 
# return True if joined characters by row or column matches the target string
#
def matchWordInMatrix(Matrix, target):
	rows = len(Matrix)
	cols = len(Matrix[0])

	if rows < cols:
		# go up-to-down
		for c in range(cols):
			word = ""
			for r in Matrix:
				word += r[c]
			#print("DBUG-- word:{} target:{}".format(word, target))
			if word.upper() == target.upper():
				print("Result: \'{}\' is found in colum {}".format(word, c))
				return True
	# go left-to-right
	words = ""	
	for i in range(rows):
		word = ''.join(Matrix[i])
		#print("DBUG-- word:{} target:{}".format(word, target))
		if word.upper() == target.upper():
			print("Result: \'{}\' is found in row {}".format(word, i))
			return True
	
	print("Result: \'{}\' is not found.".format(target))
	return False


#
# unittest
#
def test_matchWordInMatrix():
	Matrix = [['j','a','k','e'],['m','a','n','y'],['r','u','t','h']]
	target = "ruth"
	assert matchWordInMatrix(Matrix, target) == True
	target = "omma"
	assert matchWordInMatrix(Matrix, target) == False
	target = "aau"
	assert matchWordInMatrix(Matrix, target) == True

#
# client program
#
def main():
	Matrix = [['m','a','r','k'],['s','h','a','e'],['j','a','n','e']]
	target = "mark"
	print("\nTest1:\nGiven 2D matrix: {}\nTarget word: \'{}\'".format(Matrix, target))
	matchWordInMatrix(Matrix, target)

	target = "jane"
	print("\nTest2:\nGiven 2D matrix: {}\nTarget word: \'{}\'".format(Matrix, target))
	matchWordInMatrix(Matrix, target)

	target = "polk"
	print("\nTest3:\nGiven 2D matrix: {}\nTarget word: \'{}\'".format(Matrix, target))
	matchWordInMatrix(Matrix, target)
	target = "kee"
	print("\nTest4:\nGiven 2D matrix: {}\nTarget word: \'{}\'".format(Matrix, target))
	matchWordInMatrix(Matrix, target)
if __name__ == '__main__':
	main()


'''
Run-time output:
================

(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_040.py

Test1:
Given 2D matrix: [['m', 'a', 'r', 'k'], ['s', 'h', 'a', 'e'], ['j', 'a', 'n', 'e']]
Target word: 'mark'
Result: 'mark' is found in row 0

Test2:
Given 2D matrix: [['m', 'a', 'r', 'k'], ['s', 'h', 'a', 'e'], ['j', 'a', 'n', 'e']]
Target word: 'jane'
Result: 'jane' is found in row 2

Test3:
Given 2D matrix: [['m', 'a', 'r', 'k'], ['s', 'h', 'a', 'e'], ['j', 'a', 'n', 'e']]
Target word: 'polk'
Result: 'polk' is not found.

Test4:
Given 2D matrix: [['m', 'a', 'r', 'k'], ['s', 'h', 'a', 'e'], ['j', 'a', 'n', 'e']]
Target word: 'kee'
Result: 'kee' is found in colum 3
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_040.py
=================================== test session starts ===================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_040.py .                                                              [100%]

================================ 1 passed in 0.08 seconds =================================
'''

