'''
Date:01/03/2019

Problem description:
===================
This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters 
as possible anywhere in the word. If there is more than one palindrome of minimum length that can 
be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters 
to it (which is the smallest amount to make a palindrome). There are seven other palindromes that 
can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.
As another example, given the string "google", you should return "elgoogle".


Algorithm:
==========
Input: A string
Output A palindrome string
Pseudo code:
1.  Check for valid input
2.  Write a decorator function that returns True if the string is a palindrome
	For index from the edge of the string toward the middle, iterate inward.
3.	For index from the middle, iterate outward imagining a paper folded in half
  	If not a palindrome, prepend a mirrored character to the beginning of the string and go check in step 2

'''

#
# use re.findall() method to find middle index+offset
# this allows us to deal with words such as 'oo' in 'google'
# return 3 parameters: 
#    True if there are repeated characters in the string
#    Starting index of the repeated character
#    Ending index of the repeated character
#    e.g. return False, None, None
#         return True, 1, 2
#
def idxOfRepeatedChars(str):
	# Find repeated chracters by converting string into an array of characters
	arrstr = [m[1] + m[0] for m in re.findall(r'(.)(\1*)', str)]

	# locate the consecutively repeated characters
	midstr = [i for i in arrstr if len(i) > 1][0]
	
	if len(midstr) == 0:
		# find index of this midstr above and its offset
		mididx = str.index(midstr)
		return True, mididx, mididx+len(midstr)
	else:
		return False, None, None

#
# decorator function
#
def palindrome(func):
	def inner(*args):
		ret = False
		repchars, startidx, endidx = idxOfRepeatedChars(args)
		if repchars:
			# found consecutively repeated characters such as 'oo' in 'google'
			# deal with the offset index
			
			# iterate from middle toward edge 
			for i in range(endidx+1, len(args), 1): 
				if args[startidx-i] == args[i]:
					ret = True
				else:
					ret = False
		else: 
			# remaining cases such as word 'race'
			halfidx = len(args)//2

			# iterate from edge toward middle
			for i in range(halfidx):
				ret = False
				if args[i] == args[-1 + i*-1]:
					ret = True
				else:
					ret = False
			print("str is:{}".format(ret))
			return ret
	return inner
		

@palindrome
def isValidPalindrome(str):
	if len(str) == 0:
		return False
	# remove any extra white space tat both ends
	str.strip()

	return palindrome(str)


def getPalindrome(str):
	if not str.isalpha():
		return "Invalid input.  Not an alphabetic string"
	while not isValidPalindrome(str):
		half_idx = len(str)//2
		for i in range(half_idx, -1, -1):
			# prepend mirrored character 
			str[:0] + A[-i] + str[0:]
			print("DBUG-- halfidx:{} idx:{} current string:{}".format(half_idx, i, str))

	print(str)

A='google'
getPalindrome(A)
