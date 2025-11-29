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

    def generate_board(self, n, m):
        """
        Set self._state to a n x m matrix with all 0s

        Here n and m represent cell width and height, meaning height and width become n*m. Sudoku must be square?
        """

        self.cell_width = n
        self.cell_height = m

        self.side = n*m

        board = []

        for i in range(self.side):

            #make nth column
            column = []

            for j in range(self.side):

                #add value k to nth colum
                column.append(0)

            #add nth column to board
            board.append(column)


        self.state = board

    def check(self, row, col, num):
        """
        Check if num at given location is valid. Does not check entire board, only relevant rows and columns.

        Works since i dont place the num before checking
        """

        #check if row and col legal
        for i in range(self.side):

            if self.state[row][i] == num or self.state[i][col] == num:

                return False

        #check if cell legal
        start_row = self.cell_height * (row // self.cell_height)
        start_col = self.cell_width * (col // self.cell_width)

        for i in range(self.cell_height):

            for j in range(self.cell_width):

                if self.state[start_row + i][start_col + j] == num:

                    return False


        return True

    def solve(self):
        """
        Recusrive backtracking algorithm that solves the soduko. Updates Observers on board change Only looks at empty cells and does not overwrite existing data.
        """


        for row in range(self.side):

            for col in range(self.side):

                if self.state[row][col] == 0:

                    #test values 0-10
                    for num in range(1, self.side + 1):

                        #check if given num is legal
                        if self.check(row, col, num):

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
