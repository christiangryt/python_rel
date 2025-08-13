import curses
import time

class path_window():

    def __init__(self, width, height, begin_x, begin_y):
        """
        New window object. Width and height with respect to padding (TODO)
        """

        self.width = width
        self.height = height
        self.begin_x = begin_x
        self.begin_y = begin_y

        # IDK if this works
        self.win = curses.newwin(self.height, self.width, self.begin_x, self.begin_y)

    def draw_graph(self, graph=None):
        """
        Plan: Draw path. Graph reset from outside loop. (see if best option)
        """

        None

class drawer():

    def __init__(self, row_width):

        self.stdscr = curses.initscr()

        # Symbols per row in the graph
        self.row_width = row_width

        # Spaces between each character
        self.padding = 1

        self.screen_height, self.screen_width = stdscr.getmaxyx()

        # TODO: Customize
        self.start_x = int((self.screen_width -  self.row_width * self.padding) // 2)
        self.start_y = int(self.screen_height * 0.2)
