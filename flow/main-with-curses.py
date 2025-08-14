from boards import *
from cbs import *
from visualize import *

from curses import wrapper

g = graph(less_hard)
cbs = CBS_solver(g)
#cbs.solve_puzzle()

# TODO: Call solver with curses

def main(stdscr):

    dd = drawer(g, stdscr)

    stdscr.clear()

    dd.ww.win.addstr(0,0, 'HH')

    stdscr.addstr(1,0, '{}'.format(g.height))

    stdscr.addstr(2,0, '{}'.format(dd.ww.height))

    stdscr.refresh()
    dd.ww.win.refresh()
    stdscr.getkey()

wrapper(main)
