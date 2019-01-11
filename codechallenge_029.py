'''
Date: 01/11/2019

Problem dscription:
==================
This problem was asked by Amazon.

Implement a stack that has the following methods:
-	push(val), which pushes an element onto the stack
-	pop(), which pops off and returns the topmost element of the stack. 
If there are no elements in the stack, then it should throw an error or return null.
-	max(), which returns the maximum value in the stack currently. 
If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.

Algorithm:
=========
Input:  Initialized stack, then add elements
Output:  Printout the content, size, top, and max element(s)

Psuedo code:
Implement stack methods using list.
1.  Create a class called Stack and initialize with empty "list"
2.  Implement push method to "prepend" element onto the stack
3.  Implement pop method to pop element from the "list"
4.  Implement method to return max value in the stack 
	-  Check if stack is not empty,
	-  For stack size, peek - pop - peek until max value is found
	-  Return max value
To achieve constant time, each method is implemented inside the class method.
'''

class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def push(self, item):
		self.items.append(item) # use the convention of end means top
	def pop(self):
		return self.items.pop()
	def size(self):
		return len(self.items)
	def peek(self):
		return self.items[len(self.items)-1]
	def print_stack(self):
		return ', '.join(str(val) for val in self.items)
 
	def max(self):
		# generate an iterable
		iteritems = iter(self.items)

		try:
			max_val = next(iteritems) # assign the first value as the max value
		except StopIteration:
			raise ValueError("max() called with no value")

		for val in iteritems:
			if val > max_val:
				max_val = val
		return max_val	

'''
Run-time output:
===============

'''
#
# unittest module
#
def test_stack():
	#init
	S = Stack()
	assert S.isEmpty() == True
	S.push(11)
	S.push(19)
	S.push(100)
	assert S.size() == 3
	S.pop()
	assert S.print_stack() == "11, 19"
	S.push(100)
	S.push(3)
	S.push(21)
	assert S.peek() == 21
	assert S.max() == 100

#
# direct client program
#
def main():
	print("The followings print the stack content with starting line as bottom and ending line as top of the stack.\n")
	s = Stack()
	s.push(9)
	s.push(10)
	s.push(23)
	s.push(5)
	print("Test1:\nContent of the stack is {}".format(s.print_stack()))
	s.pop()
	print("After poping once, the content of the stack is {}".format(s.print_stack()))
	print("The size of the stack is {}".format(s.size()))
	print("The top element in the stack is {}".format(s.peek()))
	print("Max value is {}".format(s.max()))
	s.pop()
	s.push(99)
	s.push(55)
	s.push(1)
	print("\n\nTest2:\nContent of the stack now is {}".format(s.print_stack()))
	s.pop()
	s.pop()
	s.push(1000)
	s.push(231)
	s.push(88)
	print("After poping twice, pushing thrice, the content of the stack is {}".format(s.print_stack()))
	print("The size of the stack now is {}".format(s.size()))
	print("The top element in the stack now is {}".format(s.peek()))
	print("Max value now is {}".format(s.max()))



if __name__ == '__main__':
	main()

'''
Run-time output:
===============
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_029.py
The followings print the stack content with starting line as bottom and ending line as top of the stack.

Test1:
Content of the stack is 9, 10, 23, 5
After poping once, the content of the stack is 9, 10, 23
The size of the stack is 3
The top element in the stack is 23
Max value is 23


Test2:
Content of the stack now is 9, 10, 99, 55, 1
After poping twice, pushing thrice, the content of the stack is 9, 10, 99, 1000, 231, 88
The size of the stack now is 6
The top element in the stack now is 88
Max value now is 1000


(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_029.py
==================================== test session starts =====================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_029.py .                                                                 [100%]

================================== 1 passed in 0.09 seconds ==================================

'''
