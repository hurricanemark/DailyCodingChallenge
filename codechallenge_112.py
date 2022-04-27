'''
Date: 04/28/2022

Problem statement:
==================
This problem was asked by PayPal.

Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

t     a     g
 h   s z   a
  i i   i z
   s     g

Observation 1:
=============
Number of columns = len(sentence)
Number of rows = k
X=[cols][rows]

X[0][0] = sentence[0]
X[0][1] = ' '
X[0][2] = ' '
X[0][3] = ' '
X[0][4] = ' '
X[0][5] = ' '
X[0][6] = sentence[6]
X[0][7] = ' '
X[0][8] = ' '
X[0][9] = ' '
X[0][10] = ' '
X[0][11] = ' '
X[0][12] = sentence[13]

X[1][0] = ' '
X[1][1] = sentence[1]
X[1][2] = ' '
X[1][3] = ' '
X[1][4] = ' '
X[1][5] = sentence[5]
X[1][6] = ' '
X[1][7] = sentence[7]
X[1][8] = ' '
X[1][9] = ' '
X[1][10] = ' '
X[1][11] = sentence[11]
X[1][12] = ' '

X[2][0] = ' '
X[2][1] = ' '
X[2][2] = sentence[2]
X[2][3] = ' '
X[2][4] = sentence[4]
X[2][5] = ' '
X[2][6] = ' '
X[2][7] = ' '
X[2][8] = sentence[8]
X[2][9] = ' '
X[2][10] = sentence[10]
X[2][11] = ' '
X[2][12] = ' '

X[3][0] = ' '
X[3][1] = ' '
X[3][2] = ' '
X[3][3] = sentence[3]
X[3][4] = ''
X[3][5] = ' '
X[3][6] = ' '
X[3][7] = ' '
X[3][8] = ' '
X[3][9] = sentence[9]
X[3][10] = ' '
X[3][11] = ' '
X[3][12] = ' '

for r in result:
   print(r)

# Output:
['t', ' ', ' ', ' ', ' ', ' ', 'a', ' ', ' ', ' ', ' ', ' ', 'g']
[' ', 'h', ' ', ' ', ' ', 's', ' ', 'z', ' ', ' ', ' ', 'a', ' ']
[' ', ' ', 'i', ' ', 'i', ' ', ' ', ' ', 'i', ' ', 'z', ' ', ' ']
[' ', ' ', ' ', 's', '', ' ', ' ', ' ', ' ', 'g', ' ', ' ', ' ']


Observation 2:
=============
Base on the output of observation 1, we can approach the sentence from both ends, defining the offset for blanks as {[0,5],[1,3],[2,1,2],[3,2]}.

Or we fold the matrix into four quadrants.  Then fill the quadrants in the order of mirroring diagonally.


Algorithm:
==========
1. Create a 2d array of size [k][len(sentence)], filling with whitespaces.
2. Fill the array with the sentence in accordance with the offsets calculated as:
    R_offset += 1 
    L_offset = len(sentence) - 1 
    
'''


def bruteforce(sentence, k):
    rows = k
    cols = len(sentence)
    
    # define a 2D array
    X = [[0 for x in range(cols)] for y in range(rows)] 
    
    X[0][0] = sentence[0]
    X[0][1] = ' '
    X[0][2] = ' '
    X[0][3] = ' '
    X[0][4] = ' '
    X[0][5] = ' '
    X[0][6] = sentence[6]
    X[0][7] = ' '
    X[0][8] = ' '
    X[0][9] = ' '
    X[0][10] = ' '
    X[0][11] = ' '
    X[0][12] = sentence[12]

    X[1][0] = ' '
    X[1][1] = sentence[1]
    X[1][2] = ' '
    X[1][3] = ' '
    X[1][4] = ' '
    X[1][5] = sentence[5]
    X[1][6] = ' '
    X[1][7] = sentence[7]
    X[1][8] = ' '
    X[1][9] = ' '
    X[1][10] = ' '
    X[1][11] = sentence[11]
    X[1][12] = ' '

    X[2][0] = ' '
    X[2][1] = ' '
    X[2][2] = sentence[2]
    X[2][3] = ' '
    X[2][4] = sentence[4]
    X[2][5] = ' '
    X[2][6] = ' '
    X[2][7] = ' '
    X[2][8] = sentence[8]
    X[2][9] = ' '
    X[2][10] = sentence[10]
    X[2][11] = ' '
    X[2][12] = ' '

    X[3][0] = ' '
    X[3][1] = ' '
    X[3][2] = ' '
    X[3][3] = sentence[3]
    X[3][4] = ''
    X[3][5] = ' '
    X[3][6] = ' '
    X[3][7] = ' '
    X[3][8] = ' '
    X[3][9] = sentence[9]
    X[3][10] = ' '
    X[3][11] = ' '
    X[3][12] = ' '

    # iterate through rows
    for r in X:
        print(r)
        
if __name__ == "__main__":
    k=4
    sentence='thisisazigzag'

    bruteforce(sentence, k)

    
'''
run-time output (bruteforce):
============================

PS D:\devel\GIT\DailyCodingChallenge> python .\codechallenge_112.py
['t', ' ', ' ', ' ', ' ', ' ', 'a', ' ', ' ', ' ', ' ', ' ', 'g']
[' ', 'h', ' ', ' ', ' ', 's', ' ', 'z', ' ', ' ', ' ', 'a', ' ']
[' ', ' ', 'i', ' ', 'i', ' ', ' ', ' ', 'i', ' ', 'z', ' ', ' ']
[' ', ' ', ' ', 's', '', ' ', ' ', ' ', ' ', 'g', ' ', ' ', ' ']
'''