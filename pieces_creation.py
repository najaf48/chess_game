from pieces import Piece

class pieces_set:
    def __init__(self,chessgame) -> None:
        self.chessgame=chessgame
    def create_set(self,image):
        self.KING=Piece(1,image[0],self.chessgame, 'K')
        self.QUEEN=Piece(1,image[1],self.chessgame, 'Q')
        self.BISHOP=Piece(1,image[2],self.chessgame, 'B')
        self.KNIGHT=Piece(1,image[3],self.chessgame, 'N')
        self.ROOK=Piece(1,image[4],self.chessgame, 'R')
        self.PAWN=Piece(1,image[5],self.chessgame, 'P')
        self.king=Piece(0,image[6],self.chessgame, 'k')
        self.queen=Piece(0,image[7],self.chessgame, 'q')
        self.bishop=Piece(0,image[8],self.chessgame, 'b')
        self.knight=Piece(0,image[9],self.chessgame, 'n')
        self.rook=Piece(0,image[10],self.chessgame, 'r')
        self.pawn=Piece(0,image[11],self.chessgame, 'p')
        self.list_pieces_objects=[self.KING,self.QUEEN,self.BISHOP,self.KNIGHT,self.ROOK,self.PAWN,self.king,self.queen,self.bishop,self.knight,self.rook,self.pawn]
        self.list_white = [self.KING,self.QUEEN,self.BISHOP,self.KNIGHT,self.ROOK,self.PAWN]
        self.list_black = [self.king,self.queen,self.bishop,self.knight,self.rook,self.pawn]
    
    def drawPieces(self):
        for piece in self.list_pieces_objects:
            piece.blitme()
     
    def check_collide(self,cord,isWhite):
        if isWhite:
            for piece in self.list_white:
                for position in piece.locations:
                    if position == cord:
                        return piece,not isWhite
        else:
            for piece in self.list_black:
                for position in piece.locations:
                    if position == cord:
                        return piece,not isWhite
        return None
