import curses
import time

class drawer():

    def __init__(self, stdscr):
        """
        Initialize with stdscr from main.py and clear screen
        """

        self.stdscr = stdscr
        curses.curs_set(0)
        self.stdscr.clear()

        # Amount of letters per row
        # TODO: Import this from main somehow
        self.row_width = 4
        self.padding = 2

        # Start near the top in the middle of the screen
        self.screen_height, self.screen_width = stdscr.getmaxyx()
        self.start_x = int((self.screen_width -  self.row_width * self.padding) // 2)
        self.start_y = int(self.screen_height * 0.2)

        # Display welcome message
        welcome_msg = "Welcome to WORDLE"
        for i, letter in enumerate(welcome_msg):
            self.display(self.stdscr, -2, i-6, letter, 3)

    def display(self, stdscr, guess, pos, letter, status):
        """
        Draw Letter at position (0-4) and Guess (row number 0-4)

        Depending on if the letter is grey (incorrect), yellow (wrong place) or green (right place).
        (subject to change) i will use different color pairs
        """

        # Colors
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

        color = 0
        match status:
            case 3:
                color = 3
            case 2:
                color = 2
            case 1:
                color = 1

        stdscr.addstr(self.start_y + guess, self.start_x + pos * self.padding, letter, curses.color_pair(color))

        stdscr.refresh()
