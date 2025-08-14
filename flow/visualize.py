from curses import wrapper
import curses
import time

from collections import defaultdict

class path_window():

    def __init__(self, height, width,  begin_y, begin_x, padding):
        """
        New window object. Width and height are graph dimensions
        """

        self.begin_x = begin_x
        self.begin_y = begin_y

        self.padding = padding
        self.width = width
        self.height = height

        # IDK if this works
        self.win = curses.newwin(self.height, self.width, self.begin_x, self.begin_y)

    def draw_graph(self, graph=None):
        """
        Plan: Draw path. Graph reset from outside loop. (see if best option)

        Expects line by line. Might restructure graph to be list of lists. This should be immune to any of those changes
        """

        None

class drawer():

    def __init__(self, graph, stdscr):

        # Graph
        self.graph = graph
        self.graph_width = self.graph.width
        self.graph_height = self.graph.height

        # Padding
        self.window_padding = 2
        self.character_padding = 1

        # Dimensions
        # TODO: Customize
        #self.start_x = int((self.screen_width -  self.row_width * self.padding) // 2)
        #self.start_y = int(self.screen_height * 0.2)

        self.stdscr = stdscr
        self.screen_height, self.screen_width = self.stdscr.getmaxyx()

        # Windows
        # TODO: Smart solution here.
        self.windows = defaultdict(path_window)

        self.ww = path_window(1, 5, 0, 0, 1)
        #self.windows["D"] = ww

    def draw(self):
        self.stdscr.addstr(0,0, "HHHEHE")
