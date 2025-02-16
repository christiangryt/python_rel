import curses
from board import board
from drawer import drawer

boa = [
[0, 0, 0, 0, 0, 0, 0, 0, 2],
[6, 0, 0, 1, 0, 5, 0, 0, 0],
[0, 0, 0, 3, 0, 2, 0, 0, 0],
[0, 0, 0, 7, 0, 1, 0, 0, 3],
[0, 2, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 3, 9, 2, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 8, 0],
[0, 0, 7, 0, 1, 0, 6, 0, 0],
[0, 4, 0, 0, 0, 0, 0, 0, 0]
]  


def main(stdscr):

    #make board object and init
    bb = board()
    bb.generate_board(9)

    #make draw obj
    draw = drawer(stdscr)

    #attach draw to board
    bb.attach(draw)

    draw.state = boa
    bb.state = boa

    draw.display_all(stdscr)
    bb.solve()

    stdscr.getch()

curses.wrapper(main)