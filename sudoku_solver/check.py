def check(board, row, col, num):
    """
    
    Check if num at given location is valid. Does not check entire board, only relevant rows and columns.
    
    """

    #check if row and col legal
    for i in range(len(board)):

        if board[row][i] == num or board[i][col] == num:

            return False
        
    #check if cell legal
    #TODO see how to make general form of sudoku other than 9x9
    #finner hvor man skal starte med indeks
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):

        for j in range(3):

            if board[start_row + i][start_col + j] == num:

                return False


    return True