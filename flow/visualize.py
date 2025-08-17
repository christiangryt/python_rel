from curses import wrapper
import curses
import time

from collections import defaultdict

class path_window():

    def __init__(self, height, width,  begin_y, begin_x, padding=0):
        """
        New window object. Width and height are graph dimensions
        """

        self.begin_x = begin_x
        self.begin_y = begin_y

        self.padding = padding
        self.width = width * padding + width - padding

        # TODO ??? Why Height isnt correct?
        self.height = height + 1

        self.win = curses.newwin(self.height, self.width, self.begin_x, self.begin_y)

    def draw_line(self, n, line):

        self.win.addstr(n,0, '{}'.format(line))

    def draw_graph(self, graph):
        """
        Graph object (i only use width and list of nodes)
        """

        for i in range (graph.height):
            self.draw_line(
                    i,
                    graph.display_one_line_graph(i, self.padding)
                )

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

        self.ww = path_window(self.graph.height, self.graph.width, 0, 0, 1)
        #self.windows["D"] = ww

    def draw(self):
        self.stdscr.addstr(0,0, "HHHEHE")
