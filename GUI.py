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
            canvas.create_rectangle(x1, y1, x2, y2, fill=light_color)
        else:
            canvas.create_rectangle(x1, y1, x2, y2, fill=dark_color)


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


a1 = tk.Button(root, borderwidth=0, highlightthickness=0, width=8,
               height=6, fg=dark_color, bg=dark_color)
a1.place(x=200, y=500)



# Start the main event loop
root.mainloop()