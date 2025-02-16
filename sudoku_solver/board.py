from abstract_classes import abstract_board, abstract_drawer
from pretty_print import pretty_print

class board(abstract_board):
    """
    Board object with logic to solve sudoku
    """

    state = []
    """
    State of board is a list
    """

    observers =  []
    """
    List of subscribers to this board
    """

    def attach(self, observer):
        return self.observers.append(observer)

    def detach(self, observer):
        return self.observers.remove(observer)
    
    """
    Subscription management methods
    """

    def notify(self, y, x, num):
        """
        Notify each subscriber with new state
        """

        for observer in self.observers:
            
            #Send board state to all observers
            observer.update(y, x, num)
    
    """
    Solve Sudoku Methods
    """

    def generate_board(self, n):
        """
        
        Set self._state to a n x n matrix with all 0s
        
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


        self.state = board



    def check(self, board, row, col, num):
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
    
    def solve(self):
        """
        
        Recusrive backtracking algorithm that solves the soduko. Updates Observers on board change Only looks at empty cells and does not overwrite existing data.
        
        """

        iter = len(self.state)

        for row in range(iter):

            for col in range(iter):

                if self.state[row][col] == 0:

                    #test values 0-10
                    #TODO find way to have more than 10 numbers
                    for num in range(1,10):
                        
                        #check if given num is legal
                        if self.check(self.state, row, col, num):

                            #set cell to be num
                            self.state[row][col] = num

                            #UPDATE OBSERVERS
                            self.notify(row, col, num)

                            #calls function to solve next empty cell
                            if self.solve():
                                return True

                            #if next cell has no valid inputs backtrack
                            self.state[row][col] = 0

                            #UPDATE OBSERVERS
                            self.notify(row, col, 0)

                    return False
        
        return True