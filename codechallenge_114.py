'''
Date: 05/03/2022

Problem description:
===================
This problem was asked by Pinterest.

The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for its order 
is an array representing whether each number is larger or smaller than the last. 
Given this information, reconstruct an array that is consistent with it. 
For example, given guide == [None, +, +, -, +], and jumbled_list = [1,4,2,3,0] ]you could return [1, 2, 3, 0, 4]

Algorithm:
==========
1.  Validate input.  And check for len(guide) == len(jumbled_array)
2.  It helps if we pre-sort the jumbled list (not needed. as it turns out)
3.  Traverse the guide and construct the list making sure the current element is logically valid with the previous element.

'''

from msilib.schema import Error
import unittest
import HtmlTestRunner
import os, time
from unittest.runner import TextTestResult



def getSmallerElement(elem, lst):
    # get the first element in the lst that is smaller tham elem.
    # list.pop(index) will delete the element from lst too.  
    # pop() effects the passed-in param lst as well.  How convinience!
    for i,x in enumerate(lst):
        if x < elem: return lst.pop(i)

def getLargerElement(elem, lst):
    # get the first element in the lst that is bigger than elem.  
    # list.pop(index) will delete the element from lst too.  
    # pop() effects the passed-in param lst as well.  How convinience!
    for i,x in enumerate(lst):
        if x > elem: return lst.pop(i)
        
#
# Solution for Algorithm #1
# return the reconstructed list
#
def reconstructList(guide, lst):
    if len(guide) > len(lst):
        raise ValueError("Reconstruction guide and jumbled list have different length.")
    
    # pre-sort the jumbled list
    #worklst = sorted(lst, reverse=False)
    worklst = lst
    
    # define the return list
    newlst = []
    
    # let's reassemble the list
    for x in guide:
        if x == 'None':  # any object
            newlst.append(worklst.pop(0))
        elif x == '+':
            # insert element with value greater than newlst[-1] into newlst
            print(len(worklst))
            largerElem = getLargerElement(newlst[-1], worklst)
            print(len(worklst))
            print('newlst[-1]: ', newlst[-1], ' largerElem: ', largerElem)
            newlst.append(largerElem)
            
        elif x == '-':
            # insert element with value lesser than newlst[-1] into newlst
            smallerElem  = getSmallerElement(newlst[-1], worklst)
            print('newlst[-1]: ', newlst[-1], ' smallerElem: ', smallerElem)
            newlst.append(smallerElem)

            
        else:  #this should not happen
            raise ValueError('Unknown guiding instruction!')

    return newlst

#
# Unittest
#
class TestReconstructMessedupList(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))
    
    def test_ReconstructList(self):
        # guide = ['None', '+', '+', '-', '+']
        # jlst = [1,4,2,3,0,5]
        guide = ['None', '+', '+', '+', '-']
        jlst = [1,2,4,3,0,9,5]
        self.assertEqual(reconstructList(guide, jlst),  [1, 2, 4, 9, 3])
        jlst = [1,2,4]
        self.assertRaises(ValueError, lambda: reconstructList(guide, jlst))

def main():
    guide = ['None', '+', '+', '+', '-']
    jlst = [1,2,4,3,0,9,5]
    newList = reconstructList(guide, jlst)
    print(newList)


if __name__ == '__main__':
    if os.environ.get('UNITTEST_ONLY') != 'True':
        main()
    else:
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))    
    

'''
Run-time Output:
===============
PS D:\devel\GIT\DailyCodingChallenge> pipenv run python .\codechallenge_114.py
Loading .env environment variables...

Running tests... 
----------------------------------------------------------------------
 test_ReconstructList (__main__.TestReconstructMessedupList) ... OK (0.000000)s

----------------------------------------------------------------------
Ran 1 test in 0:00:00

OK


Generating HTML reports...
test_reports\TestResults___main__.TestReconstructMessedupList_2022-05-03_17-37-24.html
'''