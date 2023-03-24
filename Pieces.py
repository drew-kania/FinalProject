
class Piece:
    def __init__(self, color="White",  pos="A1", name="Pn", val=1):
        self.name = name
        self.value = val
        self.color = color
        self.position = [pos]
    
    def knight(self):
        self.name = "Kn"
        self.value = 3
 
    def rook(self):
        self.name = "Rk"
        self.value = 6
    
    def queen(self):
        self.name = "Qu"
        self.value = 9

    def king(self):
        self.name = "Kg"
        self.value = 10

class Bishops(Piece):
    def __init__(self, sqColor="Dark", color="White", pos="A1", name="Pn", val=1):
        super().__init__(color, pos, name, val)
        self.name = name
        self.value = val
        self.color = color
        self.sColor = sqColor

    def Bishop(self):
        if self.position == "C3" or "C8":
            self.name = "Bi"
            self.value = 3
            self.sColor = "Dark"
        else:
            self.name = "Bi"
            self.value = 3
            self.sColor = "Light"
 
pieces = []
files = ["A", "B", "C", "D", "E", "F", "G", "H"]
ranks = [1, 2, 3, 4, 5, 6, 7, 8]
# Creating white and black pawns
for file in files:
    wPawn = Piece("White", file + str(ranks[1]))
    bPawn = Piece("White", file + str(ranks[6]))
    pieces.append(wPawn)
    pieces.append(bPawn)

# Creating white and black knights
for file in files:
    if file == "B":
        wKnight = Piece("White", file + str(ranks[0]))
        bKnight = Piece("Black", file + str(ranks[7]))
        wKnight.knight()
        bKnight.knight()
        pieces.append(wKnight)
        pieces.append(bKnight)

    if file == "G":
        wKnight = Piece("White", file + str(ranks[0]))
        bKnight = Piece("Black", file + str(ranks[7]))
        wKnight.knight()
        bKnight.knight()
        pieces.append(wKnight)
        pieces.append(bKnight)

   
# Creating white and black rooks
for file in files:
    if file == "A":
        wRook = Piece("White", file + str(ranks[0]))
        bRook = Piece("Black", file + str(ranks[7]))
        wRook.rook()
        bRook.rook()
        pieces.append(wRook)
        pieces.append(bRook)
    if file == "H":
        wRook = Piece("White", file + str(ranks[0]))
        bRook = Piece("Black", file + str(ranks[7]))
        wRook.rook()
        bRook.rook()
        pieces.append(wRook)
        pieces.append(bRook)

# Creating white and black bishops
for file in files:
    if file == "C":
        wBishop =  Bishops("Dark", "White", file + str(ranks[0]))
        bBishop = Bishops("Light","Black", file + str(ranks[7]))
        wBishop.Bishop()
        bBishop.Bishop()
        pieces.append(wBishop)
        pieces.append(bBishop)
    if file == "F":
        wBishop = Bishops("Light", "White", file + str(ranks[0]))
        bBishop = Bishops("Dark","Black", file + str(ranks[7]))
        wBishop.Bishop()
        bBishop.Bishop()
        pieces.append(wBishop)
        pieces.append(bBishop)

# Creating white and black kings and queens
for file in files:
    if file == "D":
        wQueen = Piece("White", file + str(ranks[0]))
        bQueen = Piece("Black", file + str(ranks[7]))  
        wQueen.queen()
        bQueen.queen()
        pieces.append(wQueen)
        pieces.append(bQueen)
    elif file == "E":
        wKing = Piece("White", file + str(ranks[0]))
        bKing = Piece("Black", file + str(ranks[7]))
        wKing.king()
        bKing.king()
        pieces.append(wKing)
        pieces.append(bKing)

for i in pieces:
    print(i.name, i.color, i.position)


        
