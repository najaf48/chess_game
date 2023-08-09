def GenerateMove(piece,board_representation,cord):
    if piece.name=='r' or piece.name=='R':
        rook(cord,board_representation)
def pawn(cord):
    ...
def rook(cord,board_representation):
    x = cord[0]
    y = cord[1]
    x = int(x/75)
    y = int(y/75)
    ValidMoves = []
    
