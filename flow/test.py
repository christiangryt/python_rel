from curses import wrapper
import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()

    stdscr.addstr(0,0, '{}'.format(curses.COLORS))

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        stdscr.addstr(i+1, 0, '10 divided by {} is {}'.format(v, 10/v))

        stdscr.refresh()
        stdscr.getkey()

wrapper(main)

