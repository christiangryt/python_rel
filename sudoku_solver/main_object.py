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
    bb.generate_board(4, 2)

    #make draw obj
    draw = drawer(stdscr, bb)

    #attach draw to board
    bb.attach(draw)

    #draw.state = boa
    #bb.state = boa

    #bb.cell_width = 3
    #bb.cell_height = 3
    #bb.side = bb.cell_width * bb.cell_height

    draw.display_all(stdscr, bb.state)
    bb.solve()

    stdscr.getch()

curses.wrapper(main)
