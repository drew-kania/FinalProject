import tkinter as tk
import chess



move = [0,"",0,0, 0]

def Pawn(coordinate, i=0):
    move[0] = 0
    move[2] = coordinate
    move[4] = i
def Rook(coordinate, i=0):
    move[0] = "R"
    move[2] = coordinate
    move[4] = i
def Knight(coordinate, i=0):
    move[0] = "N"
    move[2] = coordinate
    move[4] = i
def Bishop(coordinate, i=0):
    move[0] = "B"
    move[2] = coordinate
    move[4] = i
def Queen(coordinate, i=0):
    move[0] = "Q"
    move[2] = coordinate
    move[4] = i
def King(coordinate, i=0):
    move[0] = "K"
    move[2] = coordinate
    move[4] = i

def Square(coordinate, old_coordinate):
    move[1] = coordinate
    y = old_coordinate[0]
    x = old_coordinate[1]
    move[3] = [y, x]
    print(move)
    game(move[0], move[1], move[2], move[3], move[4])




# Create a new window
root = tk.Tk()
root.geometry("800x800")

# Create a canvas to draw the board on
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()

# Define the colors for the light and dark squares
light_color = "white"
dark_color = "green"

# Create the squares on the board
for x in range(8):
    for y in range(8):
        x1 = x * 100
        y1 = y * 100
        x2 = x1 + 100
        y2 = y1 + 100
        if (x + y) % 2 == 0:
            canvas.create_rectangle(x1, y1, x2, y2, fill=dark_color)
        else:
            canvas.create_rectangle(x1, y1, x2, y2, fill=light_color)


image_file = "piece_images_small2/bishopblack.png"
image = tk.PhotoImage(file=image_file)

# Create the button and set its text to the image of the piece
wpawn = tk.PhotoImage(file="piece_images_small2/pawnwhite.png")
wPawn1 = tk.Button(root, image=wpawn, borderwidth=0, highlightthickness=0, command=lambda: Pawn([625,25], 0))
wPawn1.place(x=25, y=625)
wPawn2 = tk.Button(root, image=wpawn, borderwidth=0, highlightthickness=0, command=lambda: Pawn([625,125], 1))
wPawn2.place(x=125, y=625)
wPawn3 = tk.Button(root, image=wpawn, borderwidth=0, highlightthickness=0, command=lambda: Pawn([625,225], 2))
wPawn3.place(x=225, y=625)
wPawn4 = tk.Button(root, image=wpawn, borderwidth=0, highlightthickness=0, command=lambda: Pawn([625,325], 3))
wPawn4.place(x=325, y=625)
wPawn5 = tk.Button(root, image=wpawn, borderwidth=0, highlightthickness=0, command=lambda: Pawn([625,425], 4))
wPawn5.place(x=425, y=625)
wPawn6 = tk.Button(root, image=wpawn, borderwidth=0, highlightthickness=0, command=lambda: Pawn([625,525], 5))
wPawn6.place(x=525, y=625)
wPawn7 = tk.Button(root, image=wpawn, borderwidth=0, highlightthickness=0, command=lambda: Pawn([625,625], 6))
wPawn7.place(x=625, y=625)
wPawn8 = tk.Button(root, image=wpawn, borderwidth=0, highlightthickness=0, command=lambda: Pawn([625,725], 7))
wPawn8.place(x=725, y=625)


# White Rooks
wrook = tk.PhotoImage(file="piece_images_small2/rookwhite.png")
wRook1 = tk.Button(root, image=wrook, borderwidth=0, highlightthickness=0, command=lambda: Rook([725,25], 8))
wRook1.place(x=25, y=725)
wRook2 = tk.Button(root, image=wrook, borderwidth=0, highlightthickness=0, command=lambda: Rook([725,725], 9))
wRook2.place(x=725, y=725)


# White Bishops
wbishop = tk.PhotoImage(file="piece_images_small2/bishopwhite.png")
wBishop1 = tk.Button(root, image=wbishop, borderwidth=0, highlightthickness=0, command=lambda: Bishop([725,225], 10))
wBishop1.place(x=225, y=725)
wBishop2 = tk.Button(root, image=wbishop, borderwidth=0, highlightthickness=0, command=lambda: Bishop([725,525], 11))
wBishop2.place(x=525, y=725)


# White Knights
wknight = tk.PhotoImage(file="piece_images_small2/knightwhite.png")
wKnight1 = tk.Button(root, image=wknight, borderwidth=0, highlightthickness=0, command=lambda: Knight([725,125], 12))
wKnight1.place(x=125, y=725)
wKnight2 = tk.Button(root, image=wknight, borderwidth=0, highlightthickness=0, command=lambda: Knight([725,625], 13))
wKnight2.place(x=625, y=725)


# White Queen
wqueen = tk.PhotoImage(file="piece_images_small2/queenwhite.png")
wQueen = tk.Button(root, image=wqueen, borderwidth=0, highlightthickness=0, command=lambda: Queen([725,325], 14))
wQueen.place(x=325, y=725)


# White King
wking = tk.PhotoImage(file="piece_images_small2/kingwhite.png")
wKing = tk.Button(root, image=wking, borderwidth=0, highlightthickness=0, command=lambda: King([725,425], 15))
wKing.place(x=425, y=725)


# Black Bishops
bbishop = tk.PhotoImage(file="piece_images_small2/bishopblack.png")
bBishop1 = tk.Button(root, image=bbishop, borderwidth=0, highlightthickness=0, command=lambda: Bishop([25,225], 16))
bBishop1.place(x=225, y=25)
bBishop2 = tk.Button(root, image=bbishop, borderwidth=0, highlightthickness=0, command=lambda: Bishop([25,525], 17))
bBishop2.place(x=525, y=25)


# Black Knights
bknight = tk.PhotoImage(file="piece_images_small2/knightblack.png")
bKnight1 = tk.Button(root, image=bknight, borderwidth=0, highlightthickness=0, command=lambda: Knight([25,125], 18))
bKnight1.place(x=125, y=25)
bKnight2 = tk.Button(root, image=bknight, borderwidth=0, highlightthickness=0, command=lambda: Knight([25,625], 19))
bKnight2.place(x=625, y=25)


# Black Rooks
brook = tk.PhotoImage(file="piece_images_small2/rookblack.png")
bRook1 = tk.Button(root, image=brook, borderwidth=0, highlightthickness=0, command=lambda: Rook([25,25], 20))
bRook1.place(x=25, y=25)
bRook2 = tk.Button(root, image=brook, borderwidth=0, highlightthickness=0, command=lambda: Rook([25,725], 21))
bRook2.place(x=725, y=25)


# Black King
bking = tk.PhotoImage(file="piece_images_small2/kingblack.png")
bKing = tk.Button(root, image=bking, borderwidth=0, highlightthickness=0, command=lambda: King([25,425], 22))
bKing.place(x=425, y=25)


# Black Queen
bqueen = tk.PhotoImage(file="piece_images_small2/queenwhite.png")
bQueen = tk.Button(root, image=bqueen, borderwidth=0, highlightthickness=0, command=lambda: Queen([25,325], 23))
bQueen.place(x=325, y=25)


# Black Pawns
bpawn = tk.PhotoImage(file="piece_images_small2/pawnblack1.png")
bPawn1 = tk.Button(root, image=bpawn, borderwidth=0, highlightthickness=0, command=lambda: Pawn([125,25], 24))
bPawn1.place(x=25, y=125)
bPawn2 = tk.Button(root, image=bpawn, borderwidth=0, highlightthickness=0, command=lambda: Pawn([125,125], 25))
bPawn2.place(x=125, y=125)
bPawn3 = tk.Button(root, image=bpawn, borderwidth=0, highlightthickness=0, command=lambda: Pawn([125,225], 26))
bPawn3.place(x=225, y=125)
bPawn4 = tk.Button(root, image=bpawn, borderwidth=0, highlightthickness=0, command=lambda: Pawn([125,325], 27))
bPawn4.place(x=325, y=125)
bPawn5 = tk.Button(root, image=bpawn, borderwidth=0, highlightthickness=0, command=lambda: Pawn([125,425], 28))
bPawn5.place(x=425, y=125)
bPawn6 = tk.Button(root, image=bpawn, borderwidth=0, highlightthickness=0, command=lambda: Pawn([125,525], 29))
bPawn6.place(x=525, y=125)
bPawn7 = tk.Button(root, image=bpawn, borderwidth=0, highlightthickness=0, command=lambda: Pawn([125,625], 30))
bPawn7.place(x=625, y=125)
bPawn8 = tk.Button(root, image=bpawn, borderwidth=0, highlightthickness=0, command=lambda: Pawn([125,725], 31))
bPawn8.place(x=725, y=125)


# Set up buttons for spaces
a1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color, command=lambda: Square(coordinate="a1", old_coordinate=[700, 0]))
a2 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color, command=lambda: Square(coordinate="a2", old_coordinate=[600, 0]))
a3 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color, command=lambda: Square(coordinate="a3", old_coordinate=[500, 0]))
a4 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color, command=lambda: Square(coordinate="a4", old_coordinate=[400, 0]))
b1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color, command=lambda: Square(coordinate="b1", old_coordinate=[700, 10]))
b2 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color, command=lambda: Square(coordinate="b2", old_coordinate=[600, 100]))
b3 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color, command=lambda: Square(coordinate="b3", old_coordinate=[500, 100]))
b4 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color, command=lambda: Square(coordinate="b4", old_coordinate=[400, 100]))
c1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color, command=lambda: Square(coordinate="c1", old_coordinate=[700, 200]))
c2 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color, command=lambda: Square(coordinate="c2", old_coordinate=[600, 200]))
c3 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color, command=lambda: Square(coordinate="c3", old_coordinate=[500, 200]))
c4 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color, command=lambda: Square(coordinate="c4", old_coordinate=[400, 200]))
d1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color, command=lambda: Square(coordinate="d1", old_coordinate=[700, 300]))
d2 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color, command=lambda: Square(coordinate="d2", old_coordinate=[600, 300]))
d3 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color, command=lambda: Square(coordinate="d3", old_coordinate=[500, 300]))
d4 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color, command=lambda: Square(coordinate="d4", old_coordinate=[400, 300]))
e1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color, command=lambda: Square(coordinate="e1", old_coordinate=[700, 400]))
e2 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color, command=lambda: Square(coordinate="e2", old_coordinate=[600, 400]))
e3 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color, command=lambda: Square(coordinate="e3", old_coordinate=[500, 400]))
e4 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color, command=lambda: Square(coordinate="e4", old_coordinate=[400, 400]))
f1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color, command=lambda: Square(coordinate="f1", old_coordinate=[700, 500]))
f2 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color, command=lambda: Square(coordinate="f2", old_coordinate=[600, 500]))
f3 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color, command=lambda: Square(coordinate="f3", old_coordinate=[500, 500]))
f4 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color, command=lambda: Square(coordinate="f4", old_coordinate=[400, 500]))
g1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color, command=lambda: Square(coordinate="g1", old_coordinate=[700, 600]))
g2 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color, command=lambda: Square(coordinate="g2", old_coordinate=[600, 600]))
g3 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color, command=lambda: Square(coordinate="g3", old_coordinate=[500, 600]))
g4 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color, command=lambda: Square(coordinate="g4", old_coordinate=[400, 600]))
h1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color, command=lambda: Square(coordinate="g1", old_coordinate=[700, 700]))
h2 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color, command=lambda: Square(coordinate="g1", old_coordinate=[600, 700]))
h3 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color, command=lambda: Square(coordinate="g1", old_coordinate=[500, 700]))
h4 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color, command=lambda: Square(coordinate="g1", old_coordinate=[400, 700]))
a3.place(x=0, y=500)
a4.place(x=0, y=400)
b3.place(x=100, y=500)
b4.place(x=100, y=400)
c3.place(x=200, y=500)
c4.place(x=200, y=400)
d3.place(x=300, y=500)
d4.place(x=300, y=400)
e3.place(x=400, y=500)
e4.place(x=400, y=400)
f3.place(x=500, y=500)
f4.place(x=500, y=400)
g3.place(x=600, y=500)
g4.place(x=600, y=400)
h3.place(x=700, y=500)
h4.place(x=700, y=400)


# Second Half
# The A's
a5 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color, command=lambda: Square(coordinate="a5", old_coordinate=[300, 0]))
a5.place(x=0, y=300)
a6 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color, command=lambda: Square(coordinate="a6", old_coordinate=[200, 0]))
a6.place(x=0, y=200)
a7 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color, command=lambda: Square(coordinate="a7", old_coordinate=[100, 0]))
#a7.place(x=, y=)
a8 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color, command=lambda: Square(coordinate="a8", old_coordinate=[0, 0]))
#a8.place(x=, y=)


# The B's
b5 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color, command=lambda: Square(coordinate="b5", old_coordinate=[300, 100]))
b5.place(x=100, y=300)
b6 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color, command=lambda: Square(coordinate="b6", old_coordinate=[200, 100]))
b6.place(x=100, y=200)
b7 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color, command=lambda: Square(coordinate="b7", old_coordinate=[100, 100]))
#b7.place(x=, y=)
b8 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color, command=lambda: Square(coordinate="b8", old_coordinate=[0, 100]))
#b8.place(x=, y=)


# The C's
c5 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color, command=lambda: Square(coordinate="c5", old_coordinate=[300, 200]))
c5.place(x=200, y=300)
c6 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color, command=lambda: Square(coordinate="c6", old_coordinate=[200, 200]))
c6.place(x=200, y=200)
c7 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color, command=lambda: Square(coordinate="c7", old_coordinate=[100, 200]))
#c7.place(x=, y=)
c8 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color, command=lambda: Square(coordinate="c8", old_coordinate=[0, 200]))
#c8.place(x=, y=)


# The D's
d5 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color, command=lambda: Square(coordinate="d5", old_coordinate=[300, 300]))
d5.place(x=300, y=300)
d6 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color, command=lambda: Square(coordinate="d6", old_coordinate=[200, 300]))
d6.place(x=300, y=200)
d7 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color, command=lambda: Square(coordinate="d7", old_coordinate=[100, 300]))
#d7.place(x=, y=)
d8 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color, command=lambda: Square(coordinate="d8", old_coordinate=[0, 300]))
#d8.place(x=, y=)


# The E's
e5 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color, command=lambda: Square(coordinate="e5", old_coordinate=[300, 400]))
e5.place(x=400, y=300)
e6 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color, command=lambda: Square(coordinate="e6", old_coordinate=[200, 400]))
e6.place(x=400, y=200)
e7 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color, command=lambda: Square(coordinate="e7", old_coordinate=[100, 40]))
#e7.place(x=, y=)
e8 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color, command=lambda: Square(coordinate="e8", old_coordinate=[0, 400]))
#e8.place(x=, y=)


# The F's
f5 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color, command=lambda: Square(coordinate="f5", old_coordinate=[300, 500]))
f5.place(x=500, y=300)
f6 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color, command=lambda: Square(coordinate="f6", old_coordinate=[200, 500]))
f6.place(x=500, y=200)
f7 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color, command=lambda: Square(coordinate="f7", old_coordinate=[100, 500]))
#f7.place(x=, y=)
f8 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color, command=lambda: Square(coordinate="f8", old_coordinate=[0, 500]))
#f8.place(x=, y=)


# The G's
g5 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color, command=lambda: Square(coordinate="g5", old_coordinate=[300, 600]))
g5.place(x=600, y=300)
g6 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color, command=lambda: Square(coordinate="g6", old_coordinate=[200, 600]))
g6.place(x=600, y=200)
g7 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color, command=lambda: Square(coordinate="g7", old_coordinate=[100, 600]))
#g7.place(x=, y=)
g8 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color, command=lambda: Square(coordinate="g8", old_coordinate=[0, 600]))
#g8.place(x=, y=)


# The H's
h5 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color, command=lambda: Square(coordinate="h5", old_coordinate=[300, 700]))
h5.place(x=700, y=300)
h6 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color, command=lambda: Square(coordinate="h6", old_coordinate=[200, 700]))
h6.place(x=700, y=200)
h7 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color, command=lambda: Square(coordinate="h7", old_coordinate=[100, 700]))
#h7.place(x=, y=)
h8 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color, command=lambda: Square(coordinate="h8", old_coordinate=[0, 700]))
#h8.place(x=, y=)


buttons = [[a8,b8,c8,d8,e8,f8,g8,h8],
           [a7,b7,c7,d7,e7,f7,g7,h7],
           [a6,b6,c6,d6,e6,f6,g6,h6],
           [a5,b5,c5,d5,e5,f5,g5,h5],
           [a4,b4,c4,d4,e4,f4,g4,h4],
           [a3,b3,c3,d3,e3,f3,g3,h3],
           [a2,b2,c2,d2,e2,f2,g2,h2],
           [a1,b1,c1,d1,e1,f1,g1,h1]]

pieces = [wPawn1,wPawn2,wPawn3,wPawn4,wPawn5,wPawn6,wPawn7,wPawn8,wRook1,wRook2,wBishop1,wBishop2,wKnight1,wKnight2,wQueen,wKing,bBishop1,bBishop2,bKnight1,bKnight2,bRook1,bRook2,bKing,bQueen,bPawn1,bPawn2,bPawn3,bPawn4,bPawn5,bPawn6,bPawn7,bPawn8]


# Start the main event loop
def loop():
    root.mainloop()

board = chess.Board()

def game(piece="", move_to="", new_coordinate=[0,0], old_coordinate=[0,0], piece_index=0):
    valid = True
    if piece == 0:
        move = move_to
    else:
        move = piece+move_to
    try:
        board.push_san(move)
    except ValueError:
        valid = False
    if valid == True:
        new_coordinate[0] = new_coordinate[0]//25
        new_x = new_coordinate[0]//4
        new_coordinate[1] = new_coordinate[1]//25
        new_y = new_coordinate[1]//4
        buttons[new_y][new_x].destroy()
        old_coordinate[0] = old_coordinate[0]//25
        row = old_coordinate[0]//4
        old_coordinate[1] = old_coordinate[1]//25
        col = old_coordinate[1]//4
        pieces[piece_index].destroy()
        buttons[row][col].place(x=col, y=row)
        pieces[piece_index].place(x=new_x, y=new_y)
        move = []
        




while not board.is_game_over():
    loop()
