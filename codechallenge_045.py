'''
Date: 02/08/2019

Tesk description:
================
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.


Algorithm:
==========
Task: Given an integer value n, find out the n-th positive integer whose sum is 10.
Input: An integer N
Output: An integer representing the n-th perfect number.

Psuedo code:

1.  Validate input
2.  Start the counter until all digits summed up to ten.  Up the perfect count by one until perfect count equals N

(*) Note, a number is perfect if the sum of its proper factors is equal to the number.
And, all multiples of 9 are present in arithmetic progression 19, 28, 37, 46, 55, 64, 73, 82, 91, 100, 109,...

'''
import itertools

def findNthFactor(N):  
    count = 0; 
    n_fact = 19; 
    while (True):  
  
        # Find sum of digits in 
        # n_fact no.  
        sum = 0; 
        x = n_fact; 
        while (x > 0): 
            sum = sum + x % 10; 
            x = int(x / 10); 
  
        # If sum is 10, we increment 
        # count  
        if (sum == 10):  
            count+=1;  
  
        # If count becomes N, we return  
        # n_fact number.  
        if (count == N):  
            return n_fact; 
          
        n_fact += 9; 
  
    return -1;


def main():
	print(findNthFactor(1))
	print(findNthFactor(2))
	print(findNthFactor(45))

if __name__ == '__main__':
	main()
