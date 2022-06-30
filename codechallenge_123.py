'''
Date: 06/30/2022

Challenge description:
======================
Determine if two strings are anagrams of each other.

Two strings are anagrams of each other if they contain the same characters in the same quantity.

Use hash tables to store the characters of the first string and compare the second string to the first string.

Pseudo code:
============
Input: 'abcd' and 'dcba'
freq1 = {'a': 1, 'b': 1, 'c': 1, 'd': 1}
freq2 = {'d': 1, 'c': 1, 'b': 1, 'a': 1}
Note, hash tables can be compared using the == operator.
return True

Complexity: 
    (Number of Values to Store) * (SizeOf a Value) --> O(n)
    Space: O(n)

'''
import unittest
import os, time
from unittest.runner import TextTestResult

class solution:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2
        self.freq1 = {}
        self.freq2 = {}
        self.result = False
        self.compare()
    
    def compare(self):
        # base case
        if len(self.string1) != len(self.string2):
            self.result = False
            return
        if len(self.string1) == len(self.string2) == 0:
            self.result = False
            return
        
        # Get the frequency of each character in string1
        for char in self.string1:
            if char in self.freq1:
                self.freq1[char] += 1
            else:
                self.freq1[char] = 1
        print("freq1: {}".format(self.freq1))
        
        # Get the frequency of each character in string2        
        for char in self.string2:
            if char in self.freq2:
                self.freq2[char] += 1
            else:
                self.freq2[char] = 1
        print("freq2: {}".format(self.freq2))        
        
        # Compare the frequencies of each string        
        if self.freq1 == self.freq2:
            self.result = True
        else:
            self.result = False
            
        return self.result
    
    def get_result(self):
        return self.result

class TestSolution(unittest.TestCase):
    def testAnagram(self):
        ana = solution('abcd', 'dcba');
        self.assertTrue(ana.get_result())
        ana = solution('nameless', 'salesmen');
        self.assertTrue(ana.get_result())
        ana = solution('abcd', '12345');
        self.assertFalse(ana.get_result())
        ana = solution('', 'hey')
        self.assertFalse(ana.get_result())
        ana = solution('', '')
        self.assertFalse(ana.get_result())
        
        
def main(self):
    print("Running solution...\nTRUE CASES:")
    ana = solution('abcd', 'dcba');
    print("String1: '{}' and String2: '{}' are anagram? {}".format(ana.string1, ana.string2, ana.get_result()));
    ana = solution('nameless', 'salesmen');
    print("String1: '{}' and String2: '{}' are anagram? {}".format(ana.string1, ana.string2, ana.get_result()));
    
    print("\nFALSE CASES:")
    ana = solution('abcd', '12345');
    print("String1: '{}' and String2: '{}' are anagram? {}".format(ana.string1, ana.string2, ana.get_result()));
    ana = solution('', 'hey')
    print("String1: '{}' and String2: '{}' are anagram? {}".format(ana.string1, ana.string2, ana.get_result()));
    ana = solution('', '')
    print("String1: '{}' and String2: '{}' are anagram? {}".format(ana.string1, ana.string2, ana.get_result()));
    print('Done')
    
if __name__ == '__main__':
    if os.environ.get('UNITTEST_ONLY') == 'True':
        main()
    else:
        try:
            unittest.main()
        except Exception as e:
            print(e)        

'''
Runtime main() test:
=====================
TRUE CASES:
freq1: {'a': 1, 'b': 1, 'c': 1, 'd': 1}
freq2: {'d': 1, 'c': 1, 'b': 1, 'a': 1}
String1: 'abcd' and String2: 'dcba' are anagram? True
freq1: {'n': 1, 'a': 1, 'm': 1, 'e': 2, 'l': 1, 's': 2}
freq2: {'s': 2, 'a': 1, 'l': 1, 'e': 2, 'm': 1, 'n': 1}
String1: 'nameless' and String2: 'salesmen' are anagram? True

FALSE CASES:
String1: 'abcd' and String2: '12345' are anagram? False
String1: '' and String2: 'hey' are anagram? False
String1: '' and String2: '' are anagram? False
Done

Unit test:
==========
freq1: {'a': 1, 'b': 1, 'c': 1, 'd': 1}
freq2: {'d': 1, 'c': 1, 'b': 1, 'a': 1}
freq1: {'n': 1, 'a': 1, 'm': 1, 'e': 2, 'l': 1, 's': 2}
freq2: {'s': 2, 'a': 1, 'l': 1, 'e': 2, 'm': 1, 'n': 1}
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
'''