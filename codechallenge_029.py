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
 
	def max(self, key=None):
		# generate an iterable
		iteritems = iter(self.items)

		try:
			max_val = next(iteritems) # assign the first value as the max value
		except StopIteration:
			raise ValueError("max() called with no value")

		if key is None:               # use the pre-assign max value
			for val in iteritems:
				if val > max_val:
					max_val = val
		else:
			maxkey_val = key(max_val) # use the pass-in key value as key comparision
			for val in iteritems:
				keyval = key(val)
				if keyval > max_val:
					max_val = val
					maxkey_val = keyval
		return max_val	

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
	print("Test1:\nThe followings print the stack content with starting line as bottom and ending line as top of the stack.\n")
	s = Stack()
	s.push(9)
	s.push(10)
	s.push(23)
	s.push(5)
	print("Content of the stack is {}".format(s.print_stack()))
	s.pop()
	print("After poping once, the content of the stack is {}".format(s.print_stack()))
	print("The size of the stack is {}".format(s.size()))
	print("The top element in the stack is {}".format(s.peek()))
	print("Max value is {}".format(s.max()))
	s.pop()
	s.push(99)
	s.push(55)
	s.push(1)
	print("Content of the stack now is {}".format(s.print_stack()))
	s.pop()
	s.pop()
	s.push(1000)
	print("After poping twice, push once, the content of the stack is {}".format(s.print_stack()))
	print("The size of the stack now is {}".format(s.size()))
	print("The top element in the stack now is {}".format(s.peek()))
	print("Max value now is {}".format(s.max()))

main()
