import chess
import LCDdisplay
import chess.engine
import time
import RPi.GPIO as GPIO
import stockfish
import random
def start():
    LCDdisplay.setup("This is a game", "of chess using", "a Pi and", "stockfish, goodluck")
    time.sleep(2.5)
    LCDdisplay.destroy()
    
def choose_color():
    color = ["white", "black"]
    LCDdisplay.setup("Choosing color.")
    LCDdisplay.setup("Choosing color..")
    LCDdisplay.setup("Choosing color...")
    LCDdisplay.setup("Choosing color....")
    c = random.choice(color)
    LCDdisplay.setup("", "You are {}".format(c))

    return c


               
def set_engine():
    LCDdisplay.setup("Set Engine Elo", "1st Button: 750", "2nd Button: 1500", "3rd Button: 2000")
    while True:
        if (GPIO.input(b1) == GPIO.HIGH):
            LCDdisplay.destroy()
            return 750
        elif (GPIO.input(b2) == GPIO.HIGH):
            LCDdisplay.destroy()
            return 1500
        elif (GPIO.input(b3) == GPIO.HIGH):
            LCDdisplay.destroy()
            return 2250
            
def Pmove():
    player_move = ""
    player_move += get_file(True)
    player_move += get_rank(True)
    player_move += get_file(False)
    player_move += get_rank(False)
    LCDdisplay.destroy()
    print(player_move)
    return player_move
    
def get_file(starting_move):
    if starting_move:
        LCDdisplay.setup("Choose the starting", "file of the piece", "1st Button: A", "8th Button: H")
    else:
        LCDdisplay.setup("Choose the new", "file of the piece", "1st Button: A", "8th Button: H")
    while True:
        if (GPIO.input(b1) == GPIO.HIGH):
            return "a"
        elif (GPIO.input(b2) == GPIO.HIGH):
            return "b"
        elif (GPIO.input(b3) == GPIO.HIGH):
            return "c"
        elif (GPIO.input(b4) == GPIO.HIGH):
            return "d"
        elif (GPIO.input(b5) == GPIO.HIGH):
            return "e"
        elif (GPIO.input(b6) == GPIO.HIGH):
            return "f"
        elif (GPIO.input(b7) == GPIO.HIGH):
            return "g"
        elif (GPIO.input(b8) == GPIO.HIGH):
            return "h"
    
def get_rank(starting_move):
    if starting_move:
        LCDdisplay.setup("Choose the starting", "rank of the piece", "1st Button: 1", "8th Button: 8")
    else:
        LCDdisplay.setup("Choose the new", "rank of the piece", "1st Button: 1", "8th Button: 8")
    while True:
        if (GPIO.input(b1) == GPIO.HIGH):
            return "1"
        elif (GPIO.input(b2) == GPIO.HIGH):
            return "2"
        elif (GPIO.input(b3) == GPIO.HIGH):
            return "3"
        elif (GPIO.input(b4) == GPIO.HIGH):
            return "4"
        elif (GPIO.input(b5) == GPIO.HIGH):
            return "5"
        elif (GPIO.input(b6) == GPIO.HIGH):
            return "6"
        elif (GPIO.input(b7) == GPIO.HIGH):
            return "7"
        elif (GPIO.input(b8) == GPIO.HIGH):
            return "8"

   
    
board = chess.Board()
game_engine = stockfish.Stockfish("stockfish")
GPIO.setmode(GPIO.BCM)
b1 = 18
b2 = 20
b3 = 22
b4 = 13
b5 = 12
b6 = 6
b7 = 5
b8 = 4
GPIO.setup(b1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

start()
set_engine()
game_engine.set_depth(10)
player_color = choose_color()

if player_color == "white":
    while not board.is_game_over():
        move = Pmove()
        board.push_uci(move)
        game_engine.set_fen_position(board.fen())
        engine_move = game_engine.get_best_move_time(10)
        LCDdisplay.setup("Stockfish moved:", engine_move, "Button 1 to continue")
        board.push_uci(engine_move)
        while True:
            if (GPIO.input(b1) == GPIO.HIGH):
                break
        
else:
    while not board.is_game_over():
        engine_move = game_engine.get_best_move_time(10)
        LCDdisplay.setup("Stockfish moved:", engine_move, "Button 1 to continue")
        board.push_uci(engine_move)
        while True:
            if (GPIO.input(b1) == GPIO.HIGH):
                break
        
        move = Pmove()
        board.push_uci(move)
        game_engine.set_fen_position(board.fen())

    
