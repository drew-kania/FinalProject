# Term color import to visually separate light and dark squares
from termcolor import colored

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
        rank = 0
        # iterates throught every square and colors the correct ones before printing
        for row in self.board:
            rank += 1
            file = 0
            print()
            # --------------------
            for square in row:
                file += 1
                if rank % 2 == 0:
                    if file % 2 == 0:
                        print(square, end=" ")
                    # --------------------
                    else:
                        print(colored(square, "green"), end=" ")
                # --------------------       
                elif rank % 2 != 0:
                    if file % 2 != 0:
                        print(square, end=" ")
                    # --------------------
                    else:
                        print(colored(square, "green"), end=" ")
        print()
                        

game_board = ChessBoard()
game_board.create_board()
