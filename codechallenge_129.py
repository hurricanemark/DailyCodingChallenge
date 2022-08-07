'''
Date: 08/07/2002
Task description:
-----------------
Asked by Dropbox.

Create a data structure that performs all the following operations in O(1) time:

  -  plus: Add a key with value 1. If the key already exists, increment its value by one.

  -  minus: Decrement the value of a key. If the key's value is currently 1, remove it.

  -  get_max: Return a key with the highest value.

  -  get_min: Return a key with the lowest value.

Pseudo Code:
------------
Complexity order O(1) can be achieved using dictionary.
* plus: O(1)
    Add a key of value 1 while checking key in dict
* minus: O(1)
    Delete/update a key if value exists in dict and value is 1
* Retrieval: O(1)
    Return a key with the highest value
    Return a key with the lowest value
    Return all keys in dict

Obervation:
* The key facts about python complexities for dictionary:
adict[key] = value  --> O(1)
adict[key]          --> O(1)
adict.get(key)      --> O(1)
key in adict        --> O(1)
for key in adict    --> O(N)

* Likewise for set:
aset.add(val)       --> O(1)
val in aset         --> O(1)
for val in aset     --> O(N)

However, set is not applicable to key,value pairs.
'''

import unittest
import os, time
from unittest.runner import TextTestResult

        
    
# Solution using dictionary
class Solution():    
    def __init__(self):
        self.d = {}
    # Add a key with value 1. If the key already exists, increment its value by one.
    def plus(self, key):
        if key in self.d:
            self.d[key] += 1
            # print(self.d[key])
        else:
            self.d[key] = 1

    # Decrement the value of a key. If the key's value is currently 1, remove it.
    def minus(self, key):
        if key in self.d:
            if self.d[key] == 1:
                del self.d[key]
            else:
                self.d[key] -= 1
                
    # return a key with the highest value
    def get_max(self):
        if (len(self.d) == 0):        
            return None
        return max(self.d, key=self.d.get)
    
    # return a key with the lowest value
    def get_min(self):
        if (len(self.d) == 0):
            return None
        return min(self.d, key=self.d.get)
    
    # return a list of keys
    def get_all(self):
        return self.d.values()


class Test(unittest.TestCase):
    testD = Solution();
  
    def test_plus(self):
        self.testD.plus(0)
        self.testD.plus(1)
        self.testD.plus(2)
        self.testD.plus(3)
        self.testD.plus(3)
        
    def test_get_max(self):
        self.testD.plus(0)
        self.testD.plus(1)
        self.testD.plus(2)
        self.testD.plus(3)
        self.testD.plus(3)  
        self.assertEqual(self.testD.get_max(), 3)
        
    def test_get_min(self):
        self.testD.plus(0)
        self.testD.plus(1)
        self.testD.plus(2)
        self.testD.plus(3)
        self.testD.plus(3)          
        self.assertEqual(self.testD.get_min(), 0)
        
    def test_minus(self):
        self.testD.minus(0)
        self.testD.minus(1)
        self.testD.minus(2)
        self.testD.minus(3)
        self.testD.minus(3)      
        self.testD.minus(0)
        self.testD.minus(1)
        self.testD.minus(2)
        self.testD.minus(3)
        self.testD.minus(3)        
        self.assertEqual(self.testD.get_min(), None)

    
def run_dev_tests():
    testD = Solution();
    testD.plus(0)
    testD.plus(1)
    testD.plus(2)
    testD.plus(3)
    testD.plus(3)    
    all = testD.get_all()
    for key,value in enumerate(all):
        print("Key: {} -- Value: {}".format(key,value))       

    print(testD.get_max())
    print(testD.get_min())
    
def main():
    # add some keys to the dictionary
    D = Solution()
    
    for i in range(10):
        D.plus(i)
    for i in range(4,9):
        D.plus(i)  
    for i in range(3,10):
        D.plus(i)   
    for i in range(8,10):
        D.plus(i)   
                   
    # check all
    all = D.get_all()
    for key,value in enumerate(all):
        print("Key: {} -- Value: {}".format(key,value))
        
  
    
    # get the highest and lowest value
    print("Key with max value: {}".format(D.get_max()))
    print("Key with min value: {}".format(D.get_min()))

    
    # minus a non-existing key
    D.minus(10)
    
    # check all
    all = D.get_all()
    for key,value in enumerate(all):
        print("Key: {} -- Value: {}".format(key,value))    
    
    # reverse the process.  expecting none to be returned
    print("Reversing the process...")
    for i in range(10):
        D.minus(i)
    for i in range(4,9):
        D.minus(i)  
    for i in range(3,10):
        D.minus(i)   
    for i in range(8,10):
        D.minus(i)

    # check all
    print("Now, expect None to be returned.:")
    all = D.get_all()
    for key,value in enumerate(all):
        print("Key: {} -- Value: {}".format(key,value))  
    print(D.get_max())  
        
if __name__ == '__main__':
    if os.environ.get('UNITTEST_ONLY') != False:
        main()
        # run_dev_tests()
    else:
        try:
            unittest.main()
        except Exception as e:
            print(e)    
            
'''
Runtime Output:
----------------
* Dev_tests:
PS D:\DEVEL\GIT\DailyCodingChallenge> pipenv run python .\codechallenge_129.py
Loading .env environment variables...
Key: 0 -- Value: 1
Key: 1 -- Value: 1
Key: 2 -- Value: 1
Key: 3 -- Value: 2
Key: 4 -- Value: 3
Key: 5 -- Value: 3
Key: 6 -- Value: 3
Key: 7 -- Value: 3
Key: 8 -- Value: 4
Key: 9 -- Value: 3
Key with max value: 8
Key with min value: 0
Key: 0 -- Value: 1
Key: 1 -- Value: 1
Key: 2 -- Value: 1
Key: 3 -- Value: 2
Key: 4 -- Value: 3
Key: 5 -- Value: 3
Key: 6 -- Value: 3
Key: 7 -- Value: 3
Key: 8 -- Value: 4
Key: 9 -- Value: 3
Reversing the process...
Now, expect None to be returned.:
None


* Unit tests:
PS D:\DEVEL\GIT\DailyCodingChallenge> pipenv run python .\codechallenge_129.py
Loading .env environment variables...
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
'''            