'''
Date: 01/14/2019

Problem description:
===================
This problem was asked by Amazon.
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.
For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".


Algorithm:
---------
Input: A string
Output: A string representing the longest substring which is a palindrome

Pseudo code:

1.  Check for valid input
2.  change to lower case string
3.  Write a function to validate a palindrome
4.  Write a function to extract all possible substrings that could be a palindrom and feed it to the validating function above.

'''

#
# Check a string for palindrome
# this covers the case of single character.
#
def isPalindrome(instr):
    #instr = instr.casefold()  #casefold is not supported in python2.7
    rev_str = reversed(instr)  # the same as (slice/step) instr[::-1]
    if list(instr) == list(rev_str):
        return True
    else:
        return False

#
# return all possible palindrome strings
#
def all_palindromes(instr):
    start,end=0,len(instr)
    j=end
    results=[]

    while start < end-1:
        temp = instr[start:j] #Time complexity O(k)
        #print("DBUG-- {}".format(temp))
        j-=1

        if isPalindrome(temp):
            results.append(temp)

        if j<start+2:
            start+=1
            j=end

    return list(set(results))


#
# Choose the longest palindrome
#
def longest_palindrome(plist=[]):
	if len(plist) == 0:
		return None
	else:
		return max(plist, key = len)



#
# unittest
#
def test_longest_palindrome():
	STRINGS = ["aabcdcb", "bananas", "google", "maddashcat"]
	EXPECTED = ["bcdcb", "anana", "goog", "adda"] 
	PLINDS = []
	for word in STRINGS:
		PLINDS.append(longest_palindrome(all_palindromes(word)))
	assert PLINDS == EXPECTED



#
# client program
#
def main():
	STRINGS = ["aabcdcb", "bananas", "google", "maddashcat"]
	for str in STRINGS:
		print("Given '{}', the longest palindrome is '{}'".format(str, longest_palindrome(all_palindromes(str))))


if __name__ == '__main__':
	main()

'''
Run-time output:
===============
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ python codechallenge_032.py
Given 'aabcdcb', the longest palindrome is 'bcdcb'
Given 'bananas', the longest palindrome is 'anana'
Given 'google', the longest palindrome is 'goog'
Given 'maddashcat', the longest palindrome is 'adda'
(DailyCodingChallenge-wC3ocw3s) markn@raspberrypi3:~/devel/py-src/DailyCodingChallenge $ pytest codechallenge_032.py
=============================== test session starts ===============================
platform linux2 -- Python 2.7.13, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: /home/markn/devel/py-src/DailyCodingChallenge, inifile:
collected 1 item

codechallenge_032.py .                                                      [100%]

============================ 1 passed in 0.11 seconds =============================
'''
