from time import sleep as a
from generate_board import generate_board
from pretty_print import pretty_print
# from solve import solve
from check import check

import curses

#Display board state to curses wrapper
def display(stdscr, board_lines):
    """
    Dsiplay board to curses wrapper
    """
    # Clear screen
    stdscr.clear()
    
    # Set up colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    #adjust starting position to terminal size
    #TODO adjust for varying sudoku size 
    screen_height, screen_width = stdscr.getmaxyx()

    #sudoku size
    #TODO make variable not static
    grid_height = 9 * 1 - 1
    grid_width = 9 * 2 -1

    start_y = (screen_height - grid_height) // 2
    start_x = (screen_width - grid_width) // 2
    
    for i, line in enumerate(board_lines):

        #vertical offset
        y = start_y + i * 1
        x = start_x

        # Print colored text
        stdscr.addstr(y, start_x, line, curses.color_pair(1))
        
        # Refresh the screen to show changes
        stdscr.refresh()