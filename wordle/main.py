import curses
import time
from drawer import drawer
from server import server

def main(stdscr):

    # Setup
    draw = drawer(stdscr)
    ser = server("words.txt")
    status = ser.length * [0]
    ser.getWord()
    guess = 0

    while guess < 5:

        attempt = draw.takeGuess(guess)

        status = ser.checkWord(attempt)

        for i, letter in enumerate(attempt):

            draw.display(stdscr, guess, i, letter, status[i])
            time.sleep(0.4)

        if set(status) == {2}:
            break

        guess += 1

    stdscr.getch()

curses.wrapper(main)
