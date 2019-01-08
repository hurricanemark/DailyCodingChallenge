'''
Date: 01/08/2019

Problem description:
====================
This problem was asked by Dropbox.
Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:
•	Any live cell with less than two live neighbours dies.
•	Any live cell with two or three live neighbours remains living.
•	Any live cell with more than three live neighbours dies.
•	Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.
You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).


Forethoughts:
============
Any puzzle having to do with matrix (i.e. board games) will require manually tracing
at first hand.  This gives you a chance to visually approach and stratezige a more 
clever algorithm.  You will find that adjacency can be grouped by identifying the squares surrounding the current coordination.


Algorithm:
=========
Input: Rows, Columns, N-times
Output: Matrix at each sequence in N-times
Psuedo code:


'''
