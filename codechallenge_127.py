'''
Date: 08/05/2022
Task description:
================

Asked by Airbnb.

You are given an array X of floating-point numbers x1, x2, ... xn. These can be rounded up or down to create a corresponding array Y of integers y1, y2, ... yn.

Write an algorithm that finds an appropriate Y array with the following properties:

The rounded sums of both arrays should be equal.
The absolute pairwise difference between elements is minimized. In other words, |x1- y1| + |x2- y2| + ... + |xn- yn| should be as small as possible.
For example, suppose your input is [1.3, 2.3, 4.4]. In this case you cannot do better than [1, 2, 5], which has an absolute difference of |1.3 - 1| + |2.3 - 2| + |4.4 - 5| = 1.

Pseudo Code:
============
The absolute pairwise difference should ideally equal 1.
1. Create a generator that yields the rounded values for array Y.
2. Create a generator that yields the absolute difference between elements in array X and array Y.
3. Create a generator that yields the sum of elements in array X and array Y. i.e. sum(X) == sum(Y)
'''

X = [1.3, 2.3, 4.4]
Y = [1, 2, 5]
Diff = abs(1.3 -1) + abs(2.3 - 2) + abs(4.4 - 5)
print(Diff)
[ print(True) if sum(X) != sum(Y) else print(False) ]

print(sum(X), 'is', sum(Y) if sum(X) != sum(Y) else 'equal')