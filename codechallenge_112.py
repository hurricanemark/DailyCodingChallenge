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
X=[rows][cols]

Let's bruteforce it by filling out the 2d array to print the desired zigzag form.
['t', ' ', ' ', ' ', ' ', ' ', 'a', ' ', ' ', ' ', ' ', ' ', 'g']
[' ', 'h', ' ', ' ', ' ', 's', ' ', 'z', ' ', ' ', ' ', 'a', ' ']
[' ', ' ', 'i', ' ', 'i', ' ', ' ', ' ', 'i', ' ', 'z', ' ', ' ']
[' ', ' ', ' ', 's', '', ' ', ' ', ' ', ' ', 'g', ' ', ' ', ' ']


Observation 2:
=============
The main idea is to observe the layout of the output above and draw paterns from it.

Algorithm:
==========
1. Create a 2d array of size [rows, cols] == [k, len(sentence)], filling with whitespaces.
2. Fill out one row at a time with 
- Insert necessary number of spaces in the beginning of the line
- Identify next character that belongs to this line and append to it
- Append necessary number of spaces
3. Concatinate each row to the end of the 2D array and delete the top empty row.

'''
import unittest
import string
from textwrap import wrap
import numpy as np

def bruteforce(sentence, k):
    rows = k
    sentence = 'thisisazigzag' 
    cols = len(sentence)
    
    # define a 2D array
    X = [['' for x in range(cols)] for y in range(rows)] 
    
    X[0][0] = sentence[0]
    X[0][6] = sentence[6]
    X[0][12] = sentence[12]

    X[1][1] = sentence[1]
    X[1][5] = sentence[5]
    X[1][7] = sentence[7]
    X[1][11] = sentence[11]

    X[2][2] = sentence[2]
    X[2][4] = sentence[4]
    X[2][8] = sentence[8]
    X[2][10] = sentence[10]

    X[3][3] = sentence[3]
    X[3][9] = sentence[9]

    # iterate through rows
    for r in X:
        print(r)
      
      
# Use numpy.fill_diagonal         
def smarterAlgo(sentence, k):
    rows = k
    cols = len(sentence)
    chars = list(sentence)
    X = np.zeros((rows, cols), dtype='U1')
    np.fill_diagonal(X, chars[0:k], wrap=False)
    X[1,5] = 's'
    X[2,4] = 'i'
    col = np.arange(k)
    X[col, col+k+2] = ['a','z','i','g']  #chars[-(2*k):k]
    np.fill_diagonal(np.fliplr(X), chars[cols-k:cols], wrap=True)
    print(X)

# Function to print given string in the zigzag form in `k` rows
def zigZagNp(sentence, k):
    # base case
    if k == 0:
        return
 
    # base case
    if k == 1:
        print(sentence, end='')
        return sentence
 
    # define 2D array
    Result = np.zeros((k,len(sentence)), dtype='U1')
 
    # print first row
    row=[]
    last_i=1
    for i in range(0, len(sentence), (k - 1) * 2):
        [row.append(' ') for x in range(last_i, i)]
        row.append(sentence[i])
        last_i = i + 1

    row_n = Result.shape[0] ##last row
    Result = np.insert(Result,row_n,[row],axis= 0)
    n_Result = np.delete(Result, 1, 0)
    Result = n_Result
    # print(Result)
    
    # print middle rows
    last_i=0
    row = []
    for j in range(1, k - 1):
        down = True
        i = j

        while i < len(sentence):
            [row.append(' ') for x in range(last_i, i)]
            row.append(sentence[i])
            # print('i is: ',i)
            last_i=i+1
            
            if down:            # going down
                i += (k - j - 1) * 2
            else:               # going up
                i += (k - 1) * 2 - (k - j - 1) * 2
        
            down = not down     # switch direction

        [row.append(' ') for x in range(last_i, len(sentence))]
        # print(row)
        row_n = Result.shape[0] ##last row
        Result = np.insert(Result,row_n,[row],axis= 0)
        n_Result = np.delete(Result, 1, 0)
        Result = n_Result
        # print(Result)
            
        last_i = 0
        row = []
        
    # print last row
    for i in range(k - 1, len(sentence), (k - 1) * 2):
        [row.append(' ') for x in range(last_i, i)]
        row.append(sentence[i])
        last_i=i+1
    [row.append(' ') for x in range(last_i, len(sentence))]        
 
 
    row_n = Result.shape[0] ##last row
    Result = np.insert(Result,row_n,[row],axis= 0)
    n_Result = np.delete(Result, 0, 0)
    Result = n_Result
    print(Result)
    return Result
        
        
def test_zigzag():
    assert zigZagNp('THISISAZIGZAG', 4) 
            
        
def main():
    k=4
    sentence='thisisazigzag'

    print('run-time bruteforce output:')
    bruteforce(sentence, k)

    print('\nrun-time smarterAlgo output:')
    smarterAlgo(sentence, k)

    print('\nrun-time zigZagNp output:')
    sentence='THISISAZIGZAGTHATSLITHERS'
    k = 5
    zigZagNp(sentence, k) != None
    
if __name__ == '__main__':
    	main()

'''
PS D:\devel\GIT\DailyCodingChallenge> python .\codechallenge_112.py
run-time bruteforce output:
['t', '', '', '', '', '', 'a', '', '', '', '', '', 'g']
['', 'h', '', '', '', 's', '', 'z', '', '', '', 'a', '']
['', '', 'i', '', 'i', '', '', '', 'i', '', 'z', '', '']
['', '', '', 's', '', '', '', '', '', 'g', '', '', '']

run-time smarterAlgo output:
[['t' '' '' '' '' '' 'a' '' '' '' '' '' 'g']
 ['' 'h' '' '' '' 's' '' 'z' '' '' '' 'z' '']
 ['' '' 'i' '' 'i' '' '' '' 'i' '' 'a' '' '']
 ['' '' '' 's' '' '' '' '' '' 'g' '' '' '']]

run-time zigZagNp output:
[['T' ' ' ' ' ' ' ' ' ' ' 'A' ' ' ' ' ' ' ' ' ' ' 'G']
 [' ' 'H' ' ' ' ' ' ' 'S' ' ' 'Z' ' ' ' ' ' ' 'A' ' ']
 [' ' ' ' 'I' ' ' 'I' ' ' ' ' ' ' 'I' ' ' 'Z' ' ' ' ']
 [' ' ' ' ' ' 'S' ' ' ' ' ' ' ' ' ' ' 'G' ' ' ' ' ' ']]
 
run-time zigZagNp output: 
[['T' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'I' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'T' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'S']
 [' ' 'H' ' ' ' ' ' ' ' ' ' ' 'Z' ' ' 'G' ' ' ' ' ' ' ' ' ' ' 'A' ' ' 'S' ' ' ' ' ' ' ' ' ' ' 'R' ' ']
 [' ' ' ' 'I' ' ' ' ' ' ' 'A' ' ' ' ' ' ' 'Z' ' ' ' ' ' ' 'H' ' ' ' ' ' ' 'L' ' ' ' ' ' ' 'E' ' ' ' ']
 [' ' ' ' ' ' 'S' ' ' 'S' ' ' ' ' ' ' ' ' ' ' 'A' ' ' 'T' ' ' ' ' ' ' ' ' ' ' 'I' ' ' 'H' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'I' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'G' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'T' ' ' ' ' ' ' ' ']] 
'''