#print pretty sudoku board
#returns a list of formatted lines
def pretty_print(board):

    ut = []

    #TODO adapt this for other sizes than 9
    for i, row in enumerate(board):

        if i % 3 == 0 and i != 0:
            #TODO make this adapt to board size
            ut.append("-" * 21)

        row_str = ""

        for j, num in enumerate(row):

            #TODO make this adapt to board size
            if j % 3 == 0 and j != 0:
                row_str += "| "

            #TODO make this adapt to default value other than 0
            row_str += str(num) if num != 0 else "."
            row_str += " "

        ut.append(row_str)

    return ut