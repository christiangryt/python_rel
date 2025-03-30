from abstract_classes import abstract_drawer
from board import board
import curses
import time

class drawer(abstract_drawer):

    def __init__(self, stdscr):
        """
        Store stdscr in object
        """
        self.stdscr = stdscr
        curses.curs_set(0)
        self.stdscr.clear()


    def update(self, row, col, num):
        """"
        Draw num at location x, y
        """

        self.display(self.stdscr, row, col, num)
        time.sleep(0.05)

    """
    Curses Draw function
    """
    def display(self, stdscr, row, col, num):
        """
        Display character (num) at location x,y
        """
        # # Clear screen
        # stdscr.clear()
        
        # Set up colors
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

        #adjust starting position to terminal size
        #TODO adjust for varying sudoku size 
        screen_height, screen_width = stdscr.getmaxyx()

        #sudoku size
        #TODO make variable not static
        grid_height = 9 * 1 - 1
        grid_width = 9 * 2 - 1

        start_y = (screen_height - grid_height) // 2
        start_x = (screen_width - grid_width) // 2

        #x and y values to make grid
        x = col // 3 * 2 + col 
        y = row // 3 + row

        # x += col + 2 if col % 3 == 0 and col != 0 else 0
        # y += row + 2 if row % 3 == 0 and row != 0 else 0

        #num to be printed "." if 0 
        if num == 0:
            num = "."


        # Print colored text
        stdscr.addstr(start_y + y, start_x + x * 2, str(num), curses.color_pair(1))
        
        # Refresh the screen to show changes
        stdscr.refresh()

    def display_all(self,stdscr):
        """
        Display all characters from board
        """

        #Loop through self.state
        for i, y in enumerate(self.state):

            for j, x in enumerate(y):

                #TODO adjust x and y for pretty printing
                self.display(stdscr, i, j, x)
                # time.sleep(0.05)
