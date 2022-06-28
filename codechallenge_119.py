'''
Date: 06/27/2022

Two pointers problem:
======================
One pointer starts from the beginning of the string and another pointer starts from the end of the string.
They move towards each other until they meet.

Challenge description:
=======================
Reverse the characters in a string.

Test cases: even odd length of strings
'''
import unittest
import os, time
from unittest.runner import TextTestResult

def swap(s, i, j):
    # s is the list
    s[i], s[j] = s[j], s[i]
    return s

def reverse(str):
    # convert string to list
    s = list(str)
    i, j = 0, len(s) - 1
    while i < j:
        s = swap(s, i, j)
        i += 1
        j -= 1
    
    # return string from list    
    return ''.join(s)

def reverse_string(str):
    # convert string to list
    s = list(str)
    n = len(s)

    # list comprehension
    [swap(s, i, n - i - 1) for i in range(n // 2)]
    
    # return string from list
    return ''.join(s)

# unit tests
class TestReverseString(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_reverse_string(self):
        str1 = 'hurricanemark'
        str2 = 'kramenacirruh'
        time.sleep(1)
        try:
            assert reverse_string(str1) == str2
        except AssertionError:
            print('Test failed: reverse_string(str1) == str2')
            
        time.sleep(1)
        str1 = 'Emily'
        str2 = 'ylimE'
        assert reverse_string(str2) == str1
        time.sleep(1)
        assert reverse_string(reverse(str1)) == str1
        time.sleep(1)

def main():
    str1 = 'hurricanemark'
    str2 = 'kramenacirruh'
    print("Case 1: (Even number of characters in string)")
    print("\tGiven a string: '{}' its reverse: '{}'".format(str1, reverse_string(str1)))
    print("\tGiven a string: '{}', its reverse: '{}'".format(str2, reverse(str2)))

    str1 = 'Emily'
    str2 = 'ylimE'
    print("Case 2: (Odd number of characters in string)")
    print("\tGiven a string: '{}' its reverse: '{}'".format(str1, reverse_string(str1)))
    print("\tGiven a string: '{}', its reverse: '{}'".format(str2, reverse(str2)))
    
if __name__ == '__main__':
    if os.environ.get('UNITTEST_ONLY') == 'True':
        main()
    else:
        try:
            # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))    
            unittest.main()
        except Exception as e:
            print(e)
      
'''
Unit test:
==========
PS D:\DEVEL\GIT\DailyCodingChallenge> pipenv run python .\codechallenge_119.py
Loading .env environment variables...
__main__.TestReverseString.test_reverse_string: 4.048
.
----------------------------------------------------------------------
Ran 1 test in 4.048s

OK
----------------------------------------------------------------------
Ran 1 test in 4.054s

OK

Runtime output: (os.environ.get('UNITTEST_ONLY') != 'True')
===============
Loading .env environment variables...

Case 1: (Even number of characters in string)
        Given a string: 'hurricanemark' its reverse: 'kramenacirruh'
        Given a string: 'kramenacirruh', its reverse: 'hurricanemark'
        
Case 2: (Odd number of characters in string)
        Given a string: 'Emily' its reverse: 'ylimE'
        Given a string: 'ylimE', its reverse: 'Emily'
'''