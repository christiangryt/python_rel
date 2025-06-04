import curses
import time
from drawer import drawer
from server import server
from wordleBOT import wordleBOT

def main(stdscr):

    bot = wordleBOT(draw=True)

    # Setup
    draw = drawer(stdscr)
    ser = server("words.txt")
    status = ser.length * [0]
    ser.getWord()
    guess = 0

    while guess < 6:

        #attempt = draw.takeGuess(guess)
        attempt = bot.findGuess()
        status = ser.checkWord(attempt)
        bot.updateState(attempt, status)

        # Show attempt
        for i, letter in enumerate(attempt):

            draw.display(stdscr, guess, i, letter, status[i])
            time.sleep(0.3)

        # Remove wrong letters
        draw.removeLetters(attempt, status)

        if set(status) == {2}:
            break

        guess += 1

    # Print answer if failure
    if guess >= 6:
        for i, letter in enumerate(ser.secretWord):
            draw.display(stdscr, 6, i, letter, 3)
            time.sleep(0.4)
    else:
        for i, letter in enumerate("Congratulations"):
            draw.display(stdscr, 6, i-5, letter, 3)
            time.sleep(0.2)

    stdscr.getch()

curses.wrapper(main)
