'''
Date: 05/04/2022

Problem description:
====================
This problem was asked by Nest.

Create a basic sentence checker that takes in a stream of characters and determines 
whether they form valid sentences. If a sentence is valid, the program should print it out.

We can consider a sentence valid if it conforms to the following rules:

The sentence must start with a capital letter, followed by a lowercase letter or a space.
All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
There must be a single space between each word.
The sentence must end with a terminal mark immediately following a word.

Algorithm:
==========
1.  Validate input
2.  Check for single space between each word
3.  Check for terminal mark at the end of the stream
4.  Split the stream into array of characters.  Traverse the array checking for capitalized 1st letter, alphanumeric, separators.
5.  Return False if conditions not met, else print the sentence.
'''
import unittest
from msilib.schema import Error
import os, time, sys

def check_sentence(stream):
    # check for single space between each word
    if len(stream.split('  ')) > 1:
        return False
    # check if the sentence ends with a terminal mark
    if list(stream)[-1] not in ['.','!','?','‽']:
        return False
    if list(stream)[0].isupper() == False:
        return False
    # Traverse the stream and check for the followings:
    for i,c in enumerate(list(stream)):
        # is first c a capital letter?
        if i == 0:
            continue
        else: # i > 0
            if c.isspace():
                if (list(stream)[i+1].isspace()):
                    return False
            
            elif (c.isalnum() and c.islower()) or (c in [',',';',':','.']):
                continue
            else:
                return False
    print(stream)
    return True

class TestSentenceChecker(unittest.TestCase):
    def test_sentence(self):
        s = 'Hello world.'
        self.assertTrue(check_sentence(s), 'Valid sentence')
        s = 'Hello World.  This is two sentences.'
        self.assertFalse(check_sentence(s), 'Invalid sentence')
        s = 'this is not a sentence...ay caramba!'
        self.assertFalse(check_sentence(s), 'Invalid sentence')
        
#
# main driver
#
def main():
    sentence = 'The quick brown fox jumps over the lazy dog.'
    print(check_sentence(sentence))
    not_sentence = 'ohhh,  it  is not a sentence!'
    print(check_sentence(not_sentence))
    s = 'this is not a sentence...ay caramba!'
    print(check_sentence(s))
    
if __name__ == '__main__':
    if os.environ.get('UNITTEST_ONLY') != 'True':
        main()
    else:
        unittest.main()
        
'''
Run-time output:
===============

$ pipenv run python ./codechallenge_116.py
Loading .env environment variables...
The quick brown fox jumps over the lazy dog.
True
False

'''