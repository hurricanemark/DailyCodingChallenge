'''
Date: 01/08/2019

Problem description:
====================
This problem was asked by Dropbox.
Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:
	Any live cell with less than two live neighbours dies.
	Any live cell with two or three live neighbours remains living.
	Any live cell with more than three live neighbours dies.
	Any dead cell with exactly three live neighbours becomes a live cell.
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
1.  Check for valid input
2.  Initilize the board with '*'
3.  Create function count_life_sign()
    3.1  Check neighbors from cur_row-1 to cur_row+1 and cur_col-1 to cur_col+1
         return total number of alive cells      
4.  Create a generator that yields 
    - the initialized board,
    - the board after each tick (each loop)
5.  Create a function to print out the board
'''

from __future__ import print_function
#
# Initialize board with '*'
#
def init_board(rows, cols):
    return [ ['*'] * cols for _ in range(rows)]


#
# print board layout
#
def print_board(Board, tick_count):
    print("Board layout at tick count: {}.".format(tick_count))
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            print(" {} ".format(Board[i][j]), end='|') 
        print("\n")


#
# Return count of life_signs from adjacent cells
#
def count_life_signs(Board, row, col):
    life_cnt = 0

    start_row_idx = row-1
    end_row_idx = row+2
    start_col_idx = col-1
    end_col_idx = col+2

    for r in range(start_row_idx, end_row_idx, 1):
        for c in range(start_col_idx, end_col_idx, 1):
            try:
                if (r>=0 and r<=len(Board)) and(c>=0 and c<=len(Board)):
                    if Board[r][c] == '*':
                        #print("DBUG-- row,col:{},{}=={}".format(r,c, Board[r][c]))
                        life_cnt += 1
            except IndexError:
                continue
    return life_cnt

#
# generate board at initialization
# and update board after each tick
#
def board_gen(*args):
    ticks = args[2]
    tick_count = 0
    Board = init_board(args[0], args[1])
    yield Board
    def inner(*args):
        while tick_count < ticks:
            for i in range(len(Board)):
                for j in range(len(Board[i])):
                    life_count = count_life_sings(Board, i, j)
                    if Board[i][j] == '*' and (life_count < 2 or life_count > 3):
                        Board[i][j] = '.'
                    if Board[i][j] == '.' and (life_count == 3 or life_count >= 2):
                        Board[i][j] = '*'
            yield Board
            tick_count += 1
    return inner
    
#
# Altogether now!
#
def determine_mortality(Board, row, col):
    iterB = board_gen(5,5,5)
    for i,board in enumerate(iterB):
        print_board(board,i)





if __name__ == '__main__':
    Board = init_board(6,6)
    print_board(Board,0)
    print("neighbor's lifesign count at (0,0) is {}".format(count_life_signs(Board, 0,0)))
    print("neighbor's lifesign count at (5,5) is {}".format(count_life_signs(Board, 5,5)))
    print("neighbor's lifesign count at (0,5) is {}".format(count_life_signs(Board, 0,5)))
    print("neighbor's lifesign count at (5,0) is {}".format(count_life_signs(Board, 5,0)))
    print("neighbor's lifesign count at (2,2) is {}".format(count_life_signs(Board, 2,2)))

