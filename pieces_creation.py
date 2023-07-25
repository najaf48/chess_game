from pieces import Piece

class pieces_set:
    def __init__(self,image,chessgame) -> None:
        self.image=image
        self.chessgame=chessgame
    def create_set(self):
        self.KING=Piece(1,self.image[0],self.chessgame, 'k')
        self.QUEEN=Piece(1,self.image[1],self.chessgame, 'q')
        self.BISHOP=Piece(1,self.image[2],self.chessgame, 'b')
        self.KNIGHT=Piece(1,self.image[3],self.chessgame, 'n')
        self.ROOK=Piece(1,self.image[4],self.chessgame, 'r')
        self.PAWN=Piece(1,self.image[5],self.chessgame, 'p')
        self.king=Piece(0,self.image[6],self.chessgame, 'k')
        self.queen=Piece(0,self.image[7],self.chessgame, 'q')
        self.bishop=Piece(0,self.image[8],self.chessgame, 'b')
        self.knight=Piece(0,self.image[9],self.chessgame, 'n')
        self.rook=Piece(0,self.image[10],self.chessgame, 'r')
        self.pawn=Piece(0,self.image[11],self.chessgame, 'p')
        self.list_pieces_objects=[self.KING,self.QUEEN,self.BISHOP,self.KNIGHT,self.ROOK,self.PAWN,self.king,self.queen,self.bishop,self.knight,self.rook,self.pawn]
