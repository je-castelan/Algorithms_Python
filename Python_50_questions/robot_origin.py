"""
There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.
Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.
"""

def robotCircle(steps):
    x = 0
    y = 0
    moves = {"U": [0,1] ,"D": [0,-1] ,"L": [1,0],"R": [-1,0]}
    for step in steps:
        move = moves[step]
        if move:
            x += move[0]
            y += move[1]
    return x == 0 and y == 0


def printResult(steps):
    print("*"*100)
    print("Traver on {} arrives to origin??? {}".format(steps,robotCircle(steps)))


if __name__ == "__main__":
    printResult("UD") #true
    printResult("LL") #false
    printResult("UDLR") #true
    printResult("RRDD") #false
    printResult("LDRRLRUULR") #false