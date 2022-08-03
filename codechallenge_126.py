'''
Date: 08/02/2022
Description:
===========
Asked by Square.

You are given a histogram consisting of rectangles of different heights. These heights are represented in an input list, such that [1, 3, 2, 5] corresponds to the following diagram:

      x
      x  
  x   x
  x x x
x x x x

Determine the area of the largest rectangle that can be formed only from the bars of the histogram. For the diagram above, for example, this would be six, representing the (height * width): 2 x 3 area at the bottom right.

Understanding the problem:
=========================
When mapped to a 1D array, the width == the index of the elemnt.  The height is the value of the selected element (previous value + 1).

The above histogram contains three retangles of different heights. 
First one: 1x1
 x
xx    
Second one: 3x2
  x
  xx
  xxx
Third one: 2x3
    x
   xx
  xxx

Possible triangle shapes:
========================
case 1: right triangles
    /|         |\  
   / |         | \        
c /  |         |  \ c 
 /   | b     b |   \ 
/    |         |    \ 
------         -------  
   a              a  
Area of right triangle is:
Area = (a * b) / 2

case 2: isoceles triangle

     /|\         
  a / | \ a
   /  |h \   
  /   |   \
 -----------
      b 
Area = (b * h) / 2      

Isoceles requirements:
- Length of list must be odd
- Each half is the mirror image of the other. 
==> Area is ( length(histogram) * max(histogram) ) // 2


Psuedo code:
============
1. Check edge cases:
    - empty list
    - list with one element
    - list is an isoceles triangle
2. Create a generator that yields the next element in the list for comparison.
    - Keep track of incremental height by one each time.
    - if current element is less than the previous element, check for the possible triangle from elements travered so far.
    - Compare the area of the progressing triangle with the current area.
'''
import unittest
import os, time
from unittest.runner import TextTestResult
class Solution():
    
    # Check if the list describe an isoceles triangle 
    def isIsoceles(self, histogram: list[int]):
        if type(histogram) is not list:
            return False
        if len(histogram) < 2:
            return False
        # find max value in list and make it the height.  split array in half using this marker.
        max_value = max(histogram)
        print('Maximum value: {} Index: {}'.format(max_value, histogram.index(max_value)))
        
        # split the list into two halves
        h1 = histogram[:(histogram.index(max_value))]
        h2 = histogram[histogram.index(max_value) + 1:]
        # reverse the second half of the list
        h2 = h2[::-1]

        # make the two halves having equal length
        if len(h1) > len(h2):
            h1 = h1[1:len(h1)]
        if len(h2) > len(h1):
            h2 = h2[1:len(h2)]

        # print("h1:", h1)
        # print("h2:", h2[::-1])

        # compare the two halves        
        if h1 == h2:
            return [True, ((len(h1) + len(h2)) * max(histogram)) // 2]
        else:
            return [False, 0]


    def generate_next_element(self, histogram: list[int]) -> int:
        for i in histogram:
            yield i

                
    def largestTriagle(self, histogram: list[int]) -> int:
        # Edge cases:
        if (len(histogram) <= 1):
            return 0
        if (len(histogram) == 2):
            return 1
        
        # Area is ( length(histogram) * max(histogram) ) // 2
        getIsoceles = self.isIsoceles(histogram)
        if getIsoceles[0] is not False:
            return getIsoceles[1]
        
        # right triangle:
        prev_width = 0
        prev_height = 0
        # gen_element = self.generate_next_element(histogram)
        for i in histogram:
            if prev_height < i:
                prev_width += 1 
                prev_height += 1
            else:
                prev_width = 0
                
        return (prev_height * prev_width +1) // 2
    

class Test(unittest.TestCase):
    def testTriangles(self):
        histogram = [0, 1, 2, 3, 4, 3, 2, 1]         
        expected = 12
        self.assertEqual(Solution().largestTriagle(histogram), expected)            


def main():    
    histogram = [0, 1, 2, 3, 4, 3, 2, 1]         
    
    print("Is it an isoceles triangle? ", Solution().isIsoceles(histogram))
                  
    print("Area of the isoceles triangle from this histogram is: ",Solution().largestTriagle(histogram))
    
    histogram = [1, 3, 2, 5]
    print("Area of the right triangle from this histogram is: ",Solution().largestTriagle(histogram))

main()


'''
Output:
=======
PS D:\DEVEL\GIT\DailyCodingChallenge> python ./codechallenge_126.py
Maximum value: 4 Index: 4
Is it an isoceles triangle?  [True, 12]
Maximum value: 4 Index: 4
Area of the isoceles triangle from this histogram is:  12
Maximum value: 5 Index: 3
Area of the right triangle from this histogram is:  2
'''