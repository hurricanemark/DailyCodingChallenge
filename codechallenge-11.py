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

For example, given the following board:
[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps
required to reach the end is 7, since we would need to go through (1, 2) because there
is a wall everywhere else on the second row.



Pseudo code:
===========
1.  Determine the general direction of priority move, decondary move.
Priority move is alway toward the end coordinate, secondary move is when priority move is blocked.
i.e.  end(x0, y0) - start(x1,y1) ==>
    x1 - x0 == (3 - 0) = 3 means 3 moves in the virtical direction
    y1 - y0 == (0 - 0) = 0 means 0 moves in the horizontal direction necessary.
    We deduce the virtical movement takes priority in finding the end point.

2.  Ways to move: virtical(row) or horizontal(column).
    Logically we seek virtical move first, if blocked, then try horizontal move, then back i
    to trying virtical move.

3.  Rule of movement: always seek to reduce distance from the end point.
'''

import pytest

F = 'Tile'   # you can pass
T = 'Wall'   # you shall not pass
class positions:

    def __init__(self, startx, starty, endx, endy, next_x=None, next_y=None):
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
        self.next_x = next_x
        self.next_y = next_y

'''right, left, up, down'''
def whichway(curpos, endpos):
    pass

'''determine primary direction of movement'''
def priorityaxis(startpos, endpos):
    pass

def isEndpointApproachable(Board, endpos):
    return Board[endpos[0]][endpos[1]]
    
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


def canGoUp(Board, row, col):
    # can move up?
    try:
        if Board[row-1][col] == F:
            return True
        return False
    except IndexError:
        return False

def canGoDown(Board, row, col):
    try:
        if Board[row+1][col] is F:
            return True
        return False
    except IndexError:
        return False

def canGoRight(Board, row, col):
    try:
        if Board[row][col+1] is F:
            return True
        return False
    except IndexError:
        return False

def canGoLeft(Board, row, col):
    try:
        if Board[row][col-1] is F:
            return True
        return False
    except IndexError:
        return False
def forwardLooking(Board, row, col, first_inclination, second_inclination):
    # return tuple (virtical:(up, down), horizontal:(right,left)}
    right = False
    left = False
    up = False
    down = False
    forward = {}
    virt, hoz = 0
    if first_inclination == one:
        # downward 
        try:
            down = [True if Board[row-1][col] is F else False][:]
        except IndexError:
            down = False
    else:
        # upward
        try:
            up = [True if Board[row+1][col] is F else False][:]
        except IndexError:
            up = False
   
   if second_inclination == one:
        try:
            right = [True if Board[row][col-1] is F else False]
        exception IndexError:
            right = False

        elif Board[row][col+1] is not T:
            left = True
    else: 
        # upward
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
            print("Founf impenetrable wall blocking endpoint.")
            return None

    # is endpos passable. ie. F:yes, T:no
    if isEndpointApproachable(Board,endpos) is not F: 
        print("Endpoint is in the wall.  Impassable!")
        return None
    else:
        # good, we know we can get to the endpos
        # let's go
        if inclincation == negone:
            # go upward as many step as possible
            while cur_row > end_row >= 0:
                if canGoUp(Board, cur_row, cur_col) is True:
                    cur_row-=1
                    minSteps+=1
                    print("DBUG-- row upward  move: cur pos: {},{}".format(cur_row,cur_col))

            if cur_col == 0 and cur_row > end_row:
                # go right until you can go up again
                while canGoUp(Board, cur_row, cur_col) is False and canGoRight(Board, cur_row, cur_col) == True:
                        cur_col+=1
                        minSteps+=1
                # go up
                cur_row+=1
                minSteps+=1
                while cur_row > end_row and canGoLeft(Board, cur_row, cur_col) is True:
                    cur_row-=1
                    minSteps+=1
                    if cur_row == end_row and cur_col == end_col:
                        return minSteps

            elif cur_col < end_col and canGoLeft(Board, cur_row, cur_col) is True:
                print("Left:", canGoLeft(Board, cur_row, cur_col))
                cur_col-=1
                minSteps+=1
                print("DBUG:-- col leftmove  cur pos: {},{}".format(cur_row,cur_col))

            if cur_row == end_row and cur_col == end_col:
                return MinSteps  # we whould be at the end point

        elif inclination == one:
            # go downward
            while cur_row < endpos[0]:
                while canGoDown(Board, cur_row, cur_col) is True:
                    cur_row+=1
                    minSteps+=1
                    print("DBUG-- row downward  move: cur pos: {},{}".format(cur_row,cur_col))
                if cur_col > endpos[1] and canGoLeft(Board, cur_row, cur_col) is True:
                    cur_col-=1
                    minSteps+=1
                    print("DBUG:-- col leftmove  cur pos: {},{}".format(cur_row,cur_col))
                if cur_col < endpos[1] and canGoRight(Board, cur_row, cur_col) is True:
                    cur_col+=1
                    minSteps+=1
                    print("DBUG:-- col rightmove  cur pos: {},{}".format(cur_row,cur_col))
                if cur_col == endpos[1]:
                    break  # we whould be at the end point


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
