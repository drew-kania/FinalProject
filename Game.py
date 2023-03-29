# Import files
import Board
import Pieces

# ------------------------------
# Imported variables
game_board = Board.game_board
game_pieces = Pieces.pieces

# ------------------------------
# Returns the index of the starting position on the board
def get_start_position(piece_position, board):
    for rank in board:
        for position in rank:
            if piece_position == position:
                # Returns position by finding the rank of the piece(row) followed by the file(column)
                return board.index(rank), rank.index(position)
            
# ------------------------------
# places the pieces on the board
def place(board, pieces):
    for piece in pieces:
        start_position = get_start_position(piece.position, board)
        board[start_position[0]][start_position[1]] = piece.name

# ------------------------------
# Calls the functions and prints the board
place(game_board.board, game_pieces)
game_board.print_board()
