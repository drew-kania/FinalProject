
class Piece:
    # Pieces default to white pawns if not specified
    def __init__(self, color="White",  pos="A1", name="Pn", val=1):
        self.name = name
        self.value = val
        self.color = color
        self.position = pos


class Knight(Piece):
    def __init__(self, color="White", pos="A1", name="Kn", val=3):
        super().__init__(color, pos, name, val)

    def knight(self):
        self.name = "Kn"
        self.value = 3

# ----------------------------------------
class Bishops(Piece):
    def __init__(self, sqColor="Dark", color="White", pos="A1", name="Pn", val=1):
        super().__init__(color, pos, name, val)
        self.name = name
        self.value = val
        self.color = color
        self.sColor = sqColor

    # ------------------------------
    # Names and assigns values for bishops
    def Bishop(self):
        if self.position == "C3" or "C8":
            self.name = "Bi"
            self.value = 3
            self.sColor = "Dark"
        else:
            self.name = "Bi"
            self.value = 3
            self.sColor = "Light"

class Queen(Piece):
    def __init__(self, color="White", pos="A1", name="Qu", val=9):
        super().__init__(color, pos, name, val)
    
    def queen(self):
        self.name = "Qu"
        self.value = 9

class Rook(Piece):
    def __init__(self, color="White", pos="A1", name="Rk", val=6):
        super().__init__(color, pos, name, val)

    def rook(self):
        self.name = "Rk"
        self.value = 6

class King(Piece):
    def __init__(self, color="White", pos="A1", name="Kg", val=1):
        super().__init__(color, pos, name, val)
    
    def king(self):
        self.name = "Kg"
        self.value = 10

    

# ---------------------------------------- 
pieces = []
files = ["A", "B", "C", "D", "E", "F", "G", "H"]
ranks = [1, 2, 3, 4, 5, 6, 7, 8]

# Creating white and black pawns
for file in files:
    wPawn = Piece("White", file + str(ranks[1]))
    bPawn = Piece("White", file + str(ranks[6]))
    pieces.append(wPawn)
    pieces.append(bPawn)
# ------------------------------
# Creating white and black knights
for file in files:
    if file == "B":
        wKnight = Knight("White", file + str(ranks[0]))
        bKnight = Knight("Black", file + str(ranks[7]))
        wKnight.knight()
        bKnight.knight()
        pieces.append(wKnight)
        pieces.append(bKnight)

    if file == "G":
        wKnight = Knight("White", file + str(ranks[0]))
        bKnight = Knight("Black", file + str(ranks[7]))
        wKnight.knight()
        bKnight.knight()
        pieces.append(wKnight)
        pieces.append(bKnight)

# ------------------------------   
# Creating white and black rooks
for file in files:
    if file == "A":
        wRook = Rook("White", file + str(ranks[0]))
        bRook = Rook("Black", file + str(ranks[7]))
        wRook.rook()
        bRook.rook()
        pieces.append(wRook)
        pieces.append(bRook)
    if file == "H":
        wRook = Rook("White", file + str(ranks[0]))
        bRook = Rook("Black", file + str(ranks[7]))
        wRook.rook()
        bRook.rook()
        pieces.append(wRook)
        pieces.append(bRook)

# ------------------------------
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

# ------------------------------
# Creating white and black kings and queens
for file in files:
    if file == "D":
        wQueen = Queen("White", file + str(ranks[0]))
        bQueen = Queen("Black", file + str(ranks[7]))  
        wQueen.queen()
        bQueen.queen()
        pieces.append(wQueen)
        pieces.append(bQueen)
    elif file == "E":
        wKing = King("White", file + str(ranks[0]))
        bKing = King("Black", file + str(ranks[7]))
        wKing.king()
        bKing.king()
        pieces.append(wKing)
        pieces.append(bKing)
