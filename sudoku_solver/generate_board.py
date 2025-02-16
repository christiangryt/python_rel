def generate_board(n):
    """
    
    Return an n x n matrix filled with 0 
    
    """

    board = []

    for i in range(n):
        
        #make nth column
        column = []

        for j in range(n):
            
            #add value k to nth colum
            column.append(0)

        #add nth column to board
        board.append(column)


    return board

# print (generate_board(9))