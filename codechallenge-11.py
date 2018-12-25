'''
Date: 12/22/2018

Problem description:
===================
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number
of steps required to reach the end coordinate from the start. If there is no possible path,
then return null. You can move up, left, down, and right. You cannot move through walls.
You cannot wrap around the edges of the board.

  Board = [[F,F,F,F], [T,T,F,F], [F,F,F,F], [F,F,F,F]]
    0   1   2   3
  +----------------
0 | F | F | F | F |
  +----------------
1 | T | T | F | F |
  +----------------
2 | F | F | F | F |
  +----------------
3 | F | F | F | F |
  +----------------

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps
required to reach the end is 7, since we would need to go through (1, 2) because there
is a wall everywhere else on the second row.



Forethoughts:
============
1.  Construct a dictionary {"up":"?", "down":"?", "right":"?", "left":"?"} to determine
    possible moves from current position.
2.  Ask, is end_row above or below current row?
    is end_column right or left of current collumn?

Pseudo code:
===========
1.  Make possible_moves() function to return a hash table containing elements up, down, left, right
2.  Check against end point coordinate in a while loop,  Inside, at current position, determine 
    up or down for virtical movement.  if blocked, determine left/right or up/down using the possible_move table. 

i.e. Priority move is alway toward the end coordinate, secondary move is when priority move is blocked.
i.e.  end(x0, y0) - start(x1,y1) ==>
    x1 - x0 == (3 - 0) = 3 means 3 moves in the virtical direction
    y1 - y0 == (0 - 0) = 0 means 0 moves in the horizontal direction necessary.
    We deduce the virtical movement takes priority in finding the end point.

3.  2 ways to move toward end point: virtical(row) or horizontal(column).
    Logically we seek virtical move first, if blocked, then try horizontal move, then back i
    to trying virtical move.

4.  Rule of movement: always seek to reduce distance from the end point.
'''

import pytest

F = 'Tile'   # you can pass
T = 'Wall'   # you shall not pass


#
# check if endpoint is not in the wall
#
def isEndpointApproachable(Board, endpos):
    return Board[endpos[0]][endpos[1]]

#
# check if specified row is not a complete wall    
#
def isPassableRow(Board, row):
    passingcnt=0
    for col in range(len(Board[-1])):
        if Board[row][col] == T:
            passingcnt+=1
    #print("PassingCnt:{} LenA:{}".format(passingcnt, len(Board[-1])))
    if passingcnt == len(Board[-1]):
        return False
    else:
        return True 
#
# is end_row above the current position?
#
def isAbove(Board, cur_row, end_row):
    if cur_row <= end_row:
        return False
    else:
        return True

#
# is end_column right of the current position?
#
def isRight(Board, cur_col, end_col):
    if cur_col >= end_col:
        return False
    else:
        return True 

# 
# return the next possible moves from current row,col
#
def possible_moves(Board, row, col):
    avail_moves = {"up":False, "down":False, "right":False, "left":False}

    # up 
    if row == 0:
		avail_moves['up'] = False
    elif row > 0:
        try:
			if (row-1) >= 0 and Board[row-1][col] is F:
				avail_moves['up'] = True
        except IndexError:
            avail_moves['up'] = False

    # down 
    if row == len(Board[:]):
        avail_moves['down'] = False
    elif row < len(Board[:]):
        try:
            if (row+1) <= len(Board[:]) and Board[row+1][col] == F:
                avail_moves['down'] = True
        except IndexError:
            avail_moves['down'] = False

    # right 
    if col == len(Board[-1]):
        avail_move['right'] = False
    elif col < len(Board[-1]):
        try:
            if (col+1) <= len(Board[-1]) and Board[row][col+1] == F:
                avail_moves['right'] = True
        except IndexError:
            avail_moves['right'] = False

    # left 
    if col == 0:
        avail_moves['left'] = False
    elif col > 0:
        try:
            if (col-1) >= 0 and Board[row][col-1] == F:
                avail_moves['left'] = True
        except IndexError:
            avail_moves['left'] = False

    return avail_moves

#
# Let's walk the talk.
#
def gotoEndPoint(Board, startpos, endpos):
    minSteps = 0
   
    # declare unit of increment which dictates prioritized direction toward target
    one=int(1)
    negone=-one
    row_unit_inclination = [one if startpos[0] < endpos[0] else negone][0]
    col_unit_inclination = [one if startpos[1] < endpos[1] else negone][0]
    inclincation = row_unit_inclination or col_unit_inclination

    rows = len(Board[:])
    cols = len(Board[-1])
    cur_row = startpos[0]
    cur_col = startpos[1]
    end_row = endpos[0]
    end_col = endpos[1]
    print("DBUG: endpos is {}".format(Board[endpos[0]][endpos[1]]))
    print("DBUG: row_inclination={} col_inclination:{}".format(row_unit_inclination, col_unit_inclination))
    print("DBUG: unit_inclination:{}".format(col_unit_inclination))

    # is there a blocking wall on the way?
    for row in range(cur_row-1, endpos[0]-1, -1):
        if isPassableRow(Board, row) == False:
            print("Found impenetrable wall blocking endpoint.")
            return None

    # is endpos passable. ie. F:yes, T:no
    if isEndpointApproachable(Board,endpos) is not F: 
        print("Endpoint is in the wall.  Impassable!")
        return None
    else:
        # good, we know we can get to the endpos
        # let's go
        while cur_row > end_row >= 0:
            if cur_row == end_row:
                break
            else:
                for row in range(cur_row, endpos[0]-1, -1):
                    possiblemoves = possible_moves(Board, row, cur_col)
                    print("DBUG-- From position({},{}) possible moves: {}".format(row, cur_col, possiblemoves))
                    if possiblemoves['up']:
                        print("DBUG--from({},{}) move up to ({},{})".format(cur_row, cur_col, cur_row-1, cur_col))
                        cur_row-=1
                        minSteps+=1
                    elif possiblemoves['right']:
                        print("DBUG--from({},{}) move right to ({},{})".format(cur_row, cur_col, cur_row, cur_col+1))
                        cur_row+=1
                        minSteps+=1
            if cur_col == end_col:
                break
            elif cur_col > end_col:
                for col in range(cur_col, end_col):
                    if possiblemoves['left']:
                        print("DBUG--from({},{}) move left to ({},{})".format(cur_row, cur_col, cur_row, cur_col-1))
                        cur_col-=1
                        minSteps+=1
                if possibleMoves['right']:
                    print("DBUG--from({},{}) move right to ({},{})".format(cur_row, cur_col, cur_row, cur_col+1))
                    cur_col-=1
                    minSteps+=1

            if cur_row == end_row and cur_col == end_col:
                return minSteps

    return minSteps


if __name__ == '__main__':

#    F = False  # you can pass
#    T = True   # you shall not pass
    Board = [[F,F,F,F], [T,T,F,F], [F,F,F,F], [F,F,F,F]]
    start = (3,0) #A[3][0]
    end = (0,0) #A[0][0]

    print("Start pos:{}".format(start))
    print("End pos:{}".format(end))
    print("Board layout:")
    rows = len(Board[:])
    cols = len(Board[-1])
    for i in range(rows):
        for j in range(cols):
            print("({}, {}):{}".format(i,j,Board[i][j]))

    minSteps = gotoEndPoint(Board, start, end)
    print("Minimum number of steps to reach the end position: {}".format(minSteps))
