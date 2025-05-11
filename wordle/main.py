import curses
from drawer import drawer
from server import server

def main(stdscr):

    # Setup
    draw = drawer(stdscr)
    ser = server("words.txt")
    status = ser.length * [0]
    ser.getWord()
    tries = 0

    for i, letter in enumerate(ser.secretWord):

        draw.display(stdscr, 10, i, letter, 3)

    while tries <= 5:

        #bruker gjetter
        curses.echo()
        gjett = stdscr.getstr(0,17,20)
        curses.noecho()

        gjett = gjett.decode('utf-8')
        sjekk = ser.checkWord(gjett)

        for i, letter in enumerate(gjett):

            draw.display(stdscr, tries, i, letter, sjekk[i])

        stdscr.getch()

        if status == [2,2,2,2,2]:

            break

        tries += 1

curses.wrapper(main)
