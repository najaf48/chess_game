def GenerateMove(piece,board_representation,cord):
    if piece.name=='r' or piece.name=='R':
        return rook(cord,board_representation)
    elif piece.name=='p' or piece.name=='P':
        return pawn(cord,board_representation)
    elif piece.name == 'b' or piece.name == 'B':
        return bishop(cord,board_representation)
    elif piece.name == 'q' or piece.name == 'Q':
        return queen(cord,board_representation)
    elif piece.name == 'k' or piece.name == 'K':
        return king(cord,board_representation)
    

def pawn(cord,board_representation):
    x = cord[0]
    y = cord[1]
    x = int(x/75)
    y = int(y/75)
    ValidMoves = []
    opponents = []
    isWhite = board_representation[y][x].isupper()
    if isWhite:
        y1=y-1
        if y==6:
            if board_representation[y1][x] == 0:
                ValidMoves.append([x*75,y1*75])
                if board_representation[y1-1][x] == 0:
                    ValidMoves.append([x*75,(y1-1)*75])
        else:
            if board_representation[y1][x] == 0:
                ValidMoves.append([x*75,y1*75])
        if x+1<8 :
            if board_representation[y1][x+1] != 0:
                if board_representation[y1][x+1].isupper() !=  isWhite:
                    opponents.append([(x+1)*75,y1*75])
        if x-1>=0:
            if board_representation[y1][x-1] != 0:
                if board_representation[y1][x-1].isupper() != isWhite:
                    opponents.append([(x-1)*75,y1*75])
    else:
        y1=y+1
        if y==1:
            if board_representation[y1][x] == 0:
                ValidMoves.append([x*75,y1*75])
                if board_representation[y1+1][x] == 0:
                    ValidMoves.append([x*75,(y1+1)*75])
        else:
            if board_representation[y1][x] == 0:
                ValidMoves.append([x*75,y1*75])
        if x+1<8 :
            if board_representation[y1][x+1] != 0:
                if board_representation[y1][x+1].isupper() != isWhite:
                    opponents.append([(x+1)*75,y1*75])
        if x-1>=0:
            if board_representation[y1][x-1] != 0:
                if board_representation[y1][x-1].isupper() != isWhite:
                    opponents.append([(x-1)*75,y1*75])
        
    return ValidMoves,opponents

def rook(cord,board_representation):
    x = cord[0]
    y = cord[1]
    x = int(x/75)
    y = int(y/75)
    isWhite = board_representation[y][x].isupper()
    x1 = x+1
    ValidMoves = []
    opponents = []
    while x1<8:
        if board_representation[y][x1] == 0:
            ValidMoves.append([x1*75,y*75])
        elif board_representation[y][x1].isupper() !=  isWhite:
            opponents.append([x1*75,y*75])
            break
        else:
            break
        x1+=1
    
    x2=x-1
    while x2 >= 0:
        if board_representation[y][x2] == 0:
            ValidMoves.append([x2*75,y*75])
        elif board_representation[y][x2].isupper() != isWhite:
            opponents.append([x2*75,y*75])
            break
        else:
            break
        x2-=1

    y1=y+1
    while y1<8:
        if board_representation[y1][x] == 0:
            ValidMoves.append([x*75,y1*75])
        elif board_representation[y1][x].isupper() != isWhite:
            opponents.append([x*75,y1*75])
            break
        else:
            break
        y1+=1

    y2=y-1
    while y2>=0:
        if board_representation[y2][x] == 0:
            ValidMoves.append([x*75,y2*75])
        elif board_representation[y2][x].isupper() != isWhite:
            opponents.append([x*75,y2*75])
            break
        else:
            break
        y2-=1
    
    return ValidMoves,opponents

def bishop(cord,board_representation):
    x = cord[0]
    y = cord[1]
    x = int(x/75)
    y = int(y/75)
    ValidMoves = []
    opponents = []
    isWhite = board_representation[y][x].isupper()
    y1 = y - 1 
    y2 = y + 1
    x1 = x + 1
    x2 = x - 1

    while y1>=0 and x1 < 8:
        if board_representation[y1][x1] == 0:
            ValidMoves.append([x1*75,y1*75])
        elif board_representation[y1][x1].isupper() != isWhite:
            opponents.append([x1*75,y1*75])
            break
        else:
            break
        x1+=1
        y1-=1
    y1 = y - 1
    while y1 >= 0 and x2 >= 0:
        if board_representation[y1][x2] == 0:
            ValidMoves.append([x2*75,y1*75])
        elif board_representation[y1][x2].isupper() != isWhite:
            opponents.append([x2*75,y1*75])
            break
        else:
            break
        x2-=1
        y1-=1

    x1 = x + 1
    x2 = x - 1

    while y2 < 8 and x1 < 8:

        if board_representation[y2][x1] == 0:
            ValidMoves.append([x1*75,y2*75])
        elif board_representation[y2][x1].isupper() != isWhite:
            opponents.append([x1*75,y2*75])
            break
        else:
            break
        x1+=1
        y2+=1
    
    y2 = y + 1
    while y2 < 8 and x2 >= 0:
        if board_representation[y2][x2] == 0:
            ValidMoves.append([x2*75,y2*75])
        elif board_representation[y2][x2].isupper() != isWhite:
            opponents.append([x2*75,y2*75])
            break
        else:
            break
        x2-=1
        y2+=1

    return ValidMoves,opponents

def queen(cord,board_representation):
    moves_like_rook = rook(cord,board_representation)
    moves_like_bishop = bishop(cord,board_representation)
    ValidMoves = moves_like_rook[0]+moves_like_bishop[0]
    opponents = moves_like_rook[1]+moves_like_bishop[1]
    return ValidMoves,opponents

def king(cord,board_representation):
    x = cord[0]
    y = cord[1]
    x = int(x/75)
    y = int(y/75)
    ValidMoves = []
    opponents = []
    isWhite = board_representation[y][x].isupper()
    if x+1<8:
        if board_representation[y][x+1] == 0:
            ValidMoves.append([(x+1)*75,y*75])
        elif board_representation[y][x+1].isupper() != isWhite:
            opponents.append([(x+1)*75,y*75])
    if x-1>=0:
        if board_representation[y][x-1] == 0:
            ValidMoves.append([(x-1)*75,y*75])
        elif board_representation[y][x-1].isupper() != isWhite:
            opponents.append([(x-1)*75,y*75])
    if y+1<8:
        if board_representation[y+1][x] == 0:
            ValidMoves.append([x*75,(y+1)*75])
        elif board_representation[y+1][x].isupper() != isWhite:
            opponents.append([x*75,(y+1)*75])
    if y-1>=0:
        if board_representation[y-1][x] == 0:
            ValidMoves.append([x*75,(y-1)*75])
        elif board_representation[y-1][x].isupper() != isWhite:
            opponents.append([x*75,(y-1)*75])

    if y+1<8 and x+1<8:
        if board_representation[y+1][x+1] == 0:
            ValidMoves.append([(x+1)*75,(y+1)*75])
        elif board_representation[y+1][x+1].isupper() != isWhite:
            opponents.append([(x+1)*75,(y+1)*75])

    if y+1<8 and x-1>0:
        if board_representation[y+1][x-1] == 0:
            ValidMoves.append([(x-1)*75,(y+1)*75])
        elif board_representation[y+1][x-1].isupper() != isWhite:
            opponents.append([(x-1)*75,(y+1)*75])

    if y-1<8 and x+1<8:
        if board_representation[y-1][x+1] == 0:
            ValidMoves.append([(x+1)*75,(y-1)*75])
        elif board_representation[y-1][x+1].isupper() != isWhite:
            opponents.append([(x+1)*75,(y-1)*75])

    if y-1<8 and x-1>0:
        if board_representation[y-1][x-1] == 0:
            ValidMoves.append([(x-1)*75,(y-1)*75])
        elif board_representation[y-1][x-1].isupper() != isWhite:
            opponents.append([(x-1)*75,(y-1)*75])

    return ValidMoves,opponents

def knight(cord,board_representation):
    x = cord[0]
    y = cord[1]
    x = int(x/75)
    y = int(y/75)
    ValidMoves = []
    opponents = []
    isWhite = board_representation[y][x].isupper()

    if y+1<8 and x+2<8:
        if board_representation[y+1][x+2] == 0:
                ValidMoves.append([(x+2)*75,(y+1)*75])
        elif board_representation[y+1][x+2].isupper() != isWhite:
            opponents.append([(x+2)*75,(y+1)*75])
    if y+1<8 and x-2>=0:
        if board_representation[y+1][x-2] == 0:
                ValidMoves.append([(x-2)*75,(y+1)*75])
        elif board_representation[y+1][x-2].isupper() != isWhite:
            opponents.append([(x-2)*75,(y+1)*75])

    if y-1>=0 and x+2<8:
        if board_representation[y-1][x+2] == 0:
                ValidMoves.append([(x+2)*75,(y-1)*75])
        elif board_representation[y-1][x+2].isupper() != isWhite:
            opponents.append([(x+2)*75,(y-1)*75])
    if y-1>=0 and x-2>=0:
        if board_representation[y-1][x-2] == 0:
                ValidMoves.append([(x-2)*75,(y-1)*75])
        elif board_representation[y-1][x-2].isupper() != isWhite:
            opponents.append([(x-2)*75,(y-1)*75])

    if y+2<8 and x+1<8:
        if board_representation[y+2][x+1] == 0:
                ValidMoves.append([(x+1)*75,(y+2)*75])
        elif board_representation[y+2][x+1].isupper() != isWhite:
            opponents.append([(x+1)*75,(y+2)*75])
    if y+2<8 and x-1>=0:
        if board_representation[y+2][x-1] == 0:
                ValidMoves.append([(x-1)*75,(y+2)*75])
        elif board_representation[y+2][x-1].isupper() != isWhite:
            opponents.append([(x-1)*75,(y+2)*75])

    if y-2>=0 and x+1<8:
        if board_representation[y-2][x+1] == 0:
                ValidMoves.append([(x+1)*75,(y-2)*75])
        elif board_representation[y-2][x+1].isupper() != isWhite:
            opponents.append([(x+1)*75,(y-2)*75])
    if y-2>=0 and x-1>=0:
        if board_representation[y-2][x-1] == 0:
                ValidMoves.append([(x-1)*75,(y-2)*75])
        elif board_representation[y-2][x-1].isupper() != isWhite:
            opponents.append([(x-1)*75,(y-2)*75])
    
    return ValidMoves,opponents
