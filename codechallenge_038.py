'''
Date: 01/25/2019

Problem description:
====================
This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple texts such that 
each text has a length of k or less. You must break it up so that words don't break 
across lines. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is 
exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, 
you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. 
No string in the list has a length of more than 10.


Algorithm:
==========

1.  Validate input
2.  Split the string using white space as the delimiter
3.  join items at i and i+1 index such that the length of item and white spaces is less that or equal k
4.  Repeat step 3 until the end of string list
    e.g.  Given a string "the fox jumped over the fence into the pond"
    paired_text is ['the fox', 'fox jumped', 'jumped', 'over the', 'the fence', 'fence into', 'into the', 'the pond']
5.  Filter by removing overlap pairs
'''



def clipped_strs(instr, k):
	# validate input
	if len(instr) == 0 or type(k) is not int:
		return None
	elif k >= len(instr):
		return None

	# concatinate items having adjacent indices with length <= k 
	substr = instr.split(' ')
	paired_strs = [substr[i] + ' ' + substr[i+1] if (len(substr[i]) + len(substr[i+1]) + 1) <= k else substr[i] for i in range(len(substr)-1)]

	try:
		# remove wrapped over text
		for i in range(len(paired_strs)-1):
			if len(paired_strs[i].split(' ')) == 2:
				if paired_strs[i].split(' ')[1] in paired_strs[i+1]:
					paired_strs.pop(i+1)
	except IndexError:
		pass

	return paired_strs


#
# unittest
#
def test_clipped_strs():
	str = "Penny Lane is in my ears and in my eye"
	k = 11
	expected_str = ['Penny Lane', 'is in', 'my ears', 'and in', 'my eye']
	assert clipped_strs(str, k) == expected_str
	k = len(str)
	assert clipped_strs(str, k) == None


#
# client program
#
def main():
	str = "The not so smart fox jumped over the fence into the pond"
	k = 10
	print("Test1:\nGiven a string '{}' and k={}\nThe spliced string array with each element having length less than or equal to k is".format(str, k))
	print(clipped_strs(str, k))

	str = "Penny Lane is in my ears and in my eye"
	k = 11
	print("\nTest2:\nGiven a string '{}' and k={}\nThe spliced string array with each element having length less than or equal to k is".format(str, k))
	print(clipped_strs(str, k))

if __name__ == '__main__':
	main()


'''
Run-time output:
===============
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_038.py
Test1:
Given a string 'The not so smart fox jumped over the fence into the pond' and k=10
The spliced string array with each element having length less than or equal to k is
['The not', 'so smart', 'fox jumped', 'over the', 'fence into', 'the pond']

Test2:
Given a string 'Penny Lane is in my ears and in my eye' and k=11
The spliced string array with each element having length less than or equal to k is
['Penny Lane', 'is in', 'my ears', 'and in', 'my eye']
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_038.py
======================================= test session starts ========================================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_038.py .                                                                       [100%]

===================================== 1 passed in 0.06 seconds =====================================


'''
