import tkinter as tk


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

# Create the button and set its text to the image
button = tk.Button(root, image=image, borderwidth=0, highlightthickness=0)
button.place(x=325, y=25)

wpawn = tk.PhotoImage(file="piece_images_small2/pawnwhite.png")
wPawn1 = tk.Button(root, image=wpawn, borderwidth=0, highlightthickness=0)
wPawn1.place(x=25, y=625)
wPawn2 = tk.Button(root, image=wpawn, borderwidth=0, highlightthickness=0)
wPawn2.place(x=125, y=625)
wPawn3 = tk.Button(root, image=wpawn, borderwidth=0, highlightthickness=0)
wPawn3.place(x=225, y=625)
wPawn4 = tk.Button(root, image=wpawn, borderwidth=0, highlightthickness=0)
wPawn4.place(x=325, y=625)
wPawn5 = tk.Button(root, image=wpawn, borderwidth=0, highlightthickness=0)
wPawn5.place(x=425, y=625)
wPawn6 = tk.Button(root, image=wpawn, borderwidth=0, highlightthickness=0)
wPawn6.place(x=525, y=625)
wPawn7 = tk.Button(root, image=wpawn, borderwidth=0, highlightthickness=0)
wPawn7.place(x=625, y=625)
wPawn8 = tk.Button(root, image=wpawn, borderwidth=0, highlightthickness=0)
wPawn8.place(x=725, y=625)

wrook = tk.PhotoImage(file="piece_images_small2/rookwhite.png")
wRook1 = tk.Button(root, image=wrook, borderwidth=0, highlightthickness=0)
wRook1.place(x=25, y=725)
wRook2 = tk.Button(root, image=wrook, borderwidth=0, highlightthickness=0)
wRook2.place(x=725, y=725)

wbishop = tk.PhotoImage(file="piece_images_small2/bishopwhite.png")
wBishop1 = tk.Button(root, image=wbishop, borderwidth=0, highlightthickness=0)
wBishop1.place(x=225, y=725)
wBishop2 = tk.Button(root, image=wbishop, borderwidth=0, highlightthickness=0)
wBishop2.place(x=525, y=725)

wknight = tk.PhotoImage(file="piece_images_small2/knightwhite.png")
wKnight1 = tk.Button(root, image=wknight, borderwidth=0, highlightthickness=0)
wKnight1.place(x=125, y=725)
wKnight2 = tk.Button(root, image=wknight, borderwidth=0, highlightthickness=0)
wKnight2.place(x=625, y=725)

wqueen = tk.PhotoImage(file="piece_images_small2/queenwhite.png")
wQueen = tk.Button(root, image=wqueen, borderwidth=0, highlightthickness=0)
wQueen.place(x=325, y=725)

wking = tk.PhotoImage(file="piece_images_small2/kingwhite.png")
wKing = tk.Button(root, image=wking, borderwidth=0, highlightthickness=0)
wKing.place(x=425, y=725)

# Black Bishops
bbishop = tk.PhotoImage(file="piece_images_small2/bishopblack.png")
bBishop1 = tk.Button(root, image=bbishop, borderwidth=0, highlightthickness=0)
bBishop1.place(x=225, y=25)
bBishop2 = tk.Button(root, image=bbishop, borderwidth=0, highlightthickness=0)
bBishop2.place(x=525, y=25)

# Black Knights
bknight = tk.PhotoImage(file="piece_images_small2/knightblack.png")
bKnight1 = tk.Button(root, image=bknight, borderwidth=0, highlightthickness=0)
bKnight1.place(x=125, y=25)
bKnight2 = tk.Button(root, image=bknight, borderwidth=0, highlightthickness=0)
bKnight2.place(x=625, y=25)

# Black Rooks
brook = tk.PhotoImage(file="piece_images_small2/rookblack.png")
bRook1 = tk.Button(root, image=brook, borderwidth=0, highlightthickness=0)
bRook1.place(x=25, y=25)
bRook2 = tk.Button(root, image=brook, borderwidth=0, highlightthickness=0)
bRook2.place(x=725, y=25)

# Black King
bking = tk.PhotoImage(file="piece_images_small2/kingblack.png")
bKing = tk.Button(root, image=bking, borderwidth=0, highlightthickness=0)
bKing.place(x=425, y=25)

# Black Queen
bqueen = tk.PhotoImage(file="piece_images_small2/queenwhite.png")
bQueen = tk.Button(root, image=bqueen, borderwidth=0, highlightthickness=0)
bQueen.place(x=325, y=25)

# Black Pawns
bpawn = tk.PhotoImage(file="piece_images_small2/pawnblack1.png")
bPawn1 = tk.Button(root, image=bpawn, borderwidth=0, highlightthickness=0)
bPawn1.place(x=25, y=125)
bPawn2 = tk.Button(root, image=bpawn, borderwidth=0, highlightthickness=0)
bPawn2.place(x=125, y=125)
bPawn3 = tk.Button(root, image=bpawn, borderwidth=0, highlightthickness=0)
bPawn3.place(x=225, y=125)
bPawn4 = tk.Button(root, image=bpawn, borderwidth=0, highlightthickness=0)
bPawn4.place(x=325, y=125)
bPawn5 = tk.Button(root, image=bpawn, borderwidth=0, highlightthickness=0)
bPawn5.place(x=425, y=125)
bPawn6 = tk.Button(root, image=bpawn, borderwidth=0, highlightthickness=0)
bPawn6.place(x=525, y=125)
bPawn7 = tk.Button(root, image=bpawn, borderwidth=0, highlightthickness=0)
bPawn7.place(x=625, y=125)
bPawn8 = tk.Button(root, image=bpawn, borderwidth=0, highlightthickness=0)
bPawn8.place(x=725, y=125)


a1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color)
a2 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color)
a3 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color)
a4 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color)
b1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color)
b2 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color)
b3 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color)
b4 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color)
c1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color)
c2 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color)
c3 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color)
c4 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color)
d1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color)
d2 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color)
d3 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color)
d4 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color)
e1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color)
e2 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color)
e3 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color)
e4 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color)
f1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color)
f2 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color)
f3 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color)
f4 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color)
g1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color)
g2 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color)
g3 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color)
g4 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color)
h1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color)
h2 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color)
h3 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=dark_color)
h4 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8, height=6, bg=light_color)
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
a5 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
a5.place(x=0, y=300)

a6 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color)
a6.place(x=0, y=200)

a7 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
#a7.place(x=, y=)

a8 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color)
#a8.place(x=, y=)

# The B's
b5 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color)
b5.place(x=100, y=300)

b6 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
b6.place(x=100, y=200)

b7 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color)
#b7.place(x=, y=)

b8 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
#b8.place(x=, y=)

# The C's
c5 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
c5.place(x=200, y=300)

c6 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color)
c6.place(x=200, y=200)

c7 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
#c7.place(x=, y=)

c8 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color)
#c8.place(x=, y=)

# The D's
d5 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color)
d5.place(x=300, y=300)

d6 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
d6.place(x=300, y=200)

d7 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color)
#d7.place(x=, y=)

d8 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
#d8.place(x=, y=)

# The E's
e5 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
e5.place(x=400, y=300)

e6 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color)
e6.place(x=400, y=200)

e7 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
#e7.place(x=, y=)

e8 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color)
#e8.place(x=, y=)

# The F's
f5 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color)
f5.place(x=500, y=300)

f6 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
f6.place(x=500, y=200)

f7 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color)
#f7.place(x=, y=)

f8 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
#f8.place(x=, y=)

# The G's
g5 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
g5.place(x=600, y=300)

g6 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color)
g6.place(x=600, y=200)

g7 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
#g7.place(x=, y=)

g8 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color)
#g8.place(x=, y=)

# The H's
h5 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color)
h5.place(x=700, y=300)

h6 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
h6.place(x=700, y=200)

h7 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=light_color, bg=light_color)
#h7.place(x=, y=)

h8 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
#h8.place(x=, y=)



# Start the main event loop
root.mainloop()
