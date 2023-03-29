import chess

board = chess.Board()

while not board.is_game_over():
    print(board)
    move = input("Enter your move: ")
    try:
        board.push_san(move)
    except ValueError:
        print("Invalid move")
