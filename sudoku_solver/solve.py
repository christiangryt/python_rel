#IMPORT
from check import check
from pretty_print import pretty_print
from test import display
import curses
import time

#solves sudoku with backtracking algorithm
#looks at empty cells
#TODO add feature to override existing cells, to GENERATE new puzzle from random state
def solve(stdscr, board):

    """
    
    Recusrive backtracking algorithm that solves the soduko, and displays updates. Only looks at empty cells and does not overwrite existing data.
    
    """

    iter = len(board)

    for row in range(iter):

        for col in range(iter):

            if board[row][col] == 0:

                #test values 0-10
                #TODO find way to have more than 10 numbers
                for num in range(1,10):
                    
                    #check if given num is legal
                    if check(board, row, col, num):

                        #set cell to be num
                        board[row][col] = num

                        #update curses wrapper
                        pp = pretty_print(board)
                        display(stdscr, pp)
                        time.sleep(0.05)
                        #calls function to solve next empty cell
                        if solve(stdscr, board):
                            return True

                        #if next cell has no valid inputs backtrack
                        board[row][col] = 0

                        #update board after backtracking
                        pp = pretty_print(board)
                        display(stdscr, pp)
                        time.sleep(0.05)

                return False
    
    return True

