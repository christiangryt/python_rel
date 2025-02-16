#IMPORT
from generate_board import generate_board
from solve import solve
import curses

#main
def main(stdscr):

    #generate board
    # board = generate_board(9)

    board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 2],
    [6, 0, 0, 1, 0, 5, 0, 0, 0],
    [0, 0, 0, 3, 0, 2, 0, 0, 0],
    [0, 0, 0, 7, 0, 1, 0, 0, 3],
    [0, 2, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 3, 9, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 7, 0, 1, 0, 6, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0]
    ]  

    #solve the board with curses
    solve(stdscr, board)

    stdscr.getch()

curses.wrapper(main)