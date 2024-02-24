"""Implements a backtracking algorithm in order to more effciently solve a given board of sudoku. The following is a general step-by-step process of how the algorithm fucntions.
        1. Find an empty square
        2. Try numbers 1-9
        3. Find a number that works
        4. Repeat this process for the next empty square proceeding from left to right and downards
        5. When a conflict is found giving a unsolvable board given previous number choices, BACKTRACKS through other potential solutions of previous squares until a solution is found
        The following video gives a more in-depth explanation tailored to the problem: https://www.youtube.com/watch?v=eqUwSA0xI-s
"""

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0: 
            print("-----------------------") #checks if we are on third row of board, if so prints horizontal line spacer

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "") #checks if we are on the third column, if so prints a vertical line spacer

            if j == 8:
                print(board[i][j]) #checks if we are in the last position, if so goes to next line
            else:
                print(str(board[i][j]) + " ", end = "")


def find_empty_space(board):

    for i in range (len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # i denotes row, j denotes column
    return None


def check_if_valid(board, number, position):

     # Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False
        
    # Check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False

    return True


def solve(board):
    find = find_empty_space(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if check_if_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

print("\nOriginal:")
print_board(board)
solve(board)
print("\nSolved:")
print_board(board)
print()