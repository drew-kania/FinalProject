# Chess board class
class ChessBoard:
    
    def __init__(self, board=[]):
        self.board = board

    # ------------------------------
    # Creating the board
    def create_board(self):
        # Column Labels
        files = ["A", "B", "C", "D", "E", "F", "G", "H"]
        # Row Labels
        ranks = [1, 2, 3, 4, 5, 6, 7, 8]
        # --------------------
        # Creates a list for each row
        for rank in reversed(ranks):
            row = []
            # --------------------
            # Appends the row into the board object
            for file in files:
                row.append(file + str(rank))
            self.board.append(row)
    # ------------------------------
    # Prints board to the console by row
    def print_board(self):
        for row in self.board:
            print(row)

b = ChessBoard()
b.create_board()
b.print_board()