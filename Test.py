import chess
import GUI

board = chess.Board()

def game(piece="", move_to=""):
    if piece == 0:
        move = move_to
    else:
        move = piece+move_to
    try:
        board.push_san(move)
    except ValueError:
        print("Invalid move")

while not board.is_game_over():
    GUI.loop()
