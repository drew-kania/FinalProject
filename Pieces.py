from Board import ChessBoard

def get_position(piece):
    list_position = []
    for i in piece.position:
        list_position.append(i)
    return list_position


class Piece:
    # Pieces default to white pawns if not specified
    def __init__(self, color="White",  pos="A1", name="Pn", val=1):
        self.name = name
        self.value = val
        self.color = color
        self.position = pos

# ----------------------------------------
# Knight class
class Knight(Piece):
    def __init__(self, color="White", pos="A1", name="Kn", val=3):
        super().__init__(color, pos, name, val)
        self.rank = "1"
        self.file = "A"
        self.possible_moves = []
        self.actual_moves = []
    # --------------------
    def knight(self):
        self.name = "Kn"
        self.value = 3

    # --------------------
    # Finds all available moves
    def move_check(self):
        # Retrieves current position
        for i in self.position:
            if i in files:
                self.file = i
            elif i in ranks:
                self.rank = i
        self.find_move()
        

        
       
    # --------------------
    # Finds all possible moves and filters illegal moves
    def find_move(self):
        r = ranks.index(self.rank)
        f = files.index(self.file)
        all_moves = [(2, 1), (2, -1), (-2, 1),(-2, -1), (1, 2), (1, -2), (-1, 2),(-1, -2)]
        # checks if moves are within the list index for the ranks and files
        for v, h in all_moves:
            r, f = r+v, f+h
            if 0 <= r >= 7 and 0 <= f >= 7:
                self.possible_moves.append((r, f))
        # checks if the possible move has its own colored piece in that location
        for rank, file in self.possible_moves:
            for piece in pieces:
                if piece.color == self.color:
                    if piece.pos != ranks[rank] + files[file]:
                        self.actual_moves.append(ranks[rank] + files[file])


# bishop class
# ----------------------------------------
class Bishops(Piece):
    def __init__(self, sqColor="Dark", color="White", pos="A1", name="Pn", val=1):
        super().__init__(color, pos, name, val)
        self.name = name
        self.value = val
        self.color = color
        self.sColor = sqColor
        self.rank = "1"
        self.file = "A"
        self.possible_moves = []
        self.actual_moves = []

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
    
    def move_check(self):
        for i in self.position:
            if i in files:
                self.file = i
            elif i in ranks:
                self.rank = i

    def find_move(self):
        r = ranks.index(self.rank)
        f = files.index(self.file)
        all_moves = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        for i, j in all_moves:
            for b in range(1, 8):
                y = r + i * b
                x = f + j * b
                if 0 <= y >= 7 and 0 <= x >= 7:
                    self.possible_moves.append((y, x))
        for rank, file in self.possible_moves:
            for piece in pieces:
                if piece.pos == ranks[rank] + files[file]:
                    
                    if piece.color == self.color:
                        self.actual_moves.append(ranks[rank] + files[file])
        




# ----------------------------------------
# Queen class
class Queen(Piece):
    def __init__(self, color="White", pos="A1", name="Qu", val=9):
        super().__init__(color, pos, name, val)
    
    def queen(self):
        self.name = "Qu"
        self.value = 9

# ----------------------------------------
# Rook class
class Rook(Piece):
    def __init__(self, color="White", pos="A1", name="Rk", val=6):
        super().__init__(color, pos, name, val)

    def rook(self):
        self.name = "Rk"
        self.value = 6

# ----------------------------------------
# King class
class King(Piece):
    def __init__(self, color="White", pos="A1", name="Kg", val=1):
        super().__init__(color, pos, name, val)
    
    def king(self):
        self.name = "Kg"
        self.value = 10

# ----------------------------------------
pieces = []
files = ["A", "B", "C", "D", "E", "F", "G", "H"]
ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]

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
