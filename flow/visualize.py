import curses
import time

class drawer():

    def __init__(self, row_width):

        self.stdscr = curses.initscr()

        # Symbols per row in the graph
        self.row_width = row_width

        # Spaces between each character
        self.padding = 1

        self.screen_height, self.screen_width = stdscr.getmaxyx()
