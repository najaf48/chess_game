from ValidMoveGenerator import GenerateMove

def generate_moves_for_player(board_representation,isWhite):
    moves = []
    invalidmoves=[]
    x=0
    y=0
    for row in board_representation:
        for notation in row:
            if notation == 0:
                moves.append([[],[]])
                invalidmoves.append([[],[]])
            elif notation.isupper() == isWhite:
                move = GenerateMove(board_representation,[x,y])
                moves.append(move)
                invalidmoves.append([[],[]])
            else:
                moves.append([[],[]])
                invalidmoves.append([[],[]])
            x+=75
        x=0
        y+=75
    for i in range(len(moves)):
        for j in range(len(moves[i][0])):
            if will_it_kill_king(i,moves[i][0][j],board_representation):
                invalidmoves[i][0].append(moves[i][0][j])
        for j in range(len(moves[i][1])):
            if will_it_kill_king(i,moves[i][1][j],board_representation):
                invalidmoves[i][1].append(moves[i][1][j])
    for i in range(len(invalidmoves)):
        for j in range(len(invalidmoves[i][0])):
            if invalidmoves[i][0][j] in moves[i][0]:
                moves[i][0].remove(invalidmoves[i][0][j])
        for j in range(len(invalidmoves[i][1])):
            if invalidmoves[i][1][j] in moves[i][1]:
                moves[i][1].remove(invalidmoves[i][1][j])
    check_mate = True
    for i in moves:
        for j in i:
            for k in j:
                if k!=[]:
                    check_mate=False
    if check_mate:
        return None
    else:
        return moves

def will_it_kill_king(start,stop,board_repr):
    y = int(start/8)
    x = int(start%8)
    y1 =int((stop[1])/75)
    x1 =int((stop[0])/75)
    start_piece = board_repr[y][x]
    stop_piece = board_repr[y1][x1]
    iswhite = start_piece.isupper()
    kinglocation = whereisKing(iswhite,board_repr)
    board_repr[y][x] = 0
    board_repr[y1][x1] = start_piece
    if start_piece == 'K' or start_piece == 'k':
        kinglocation = whereisKing(iswhite,board_repr)
    oppoenent_moves = generate_moves_for_opponenet(board_repr,not iswhite)
    board_repr[y][x] = start_piece
    board_repr[y1][x1] = stop_piece
    for move in oppoenent_moves:
        if move!=[]:
            if kinglocation in move[0] or kinglocation in move[1]:
                return True
    return False

def whereisKing(iswhite,board_repr):
    x=0
    y=0
    for row in board_repr:
        for notation in row:
            if iswhite:
                if notation == 'K':
                    return [x,y]
            else:
                if notation == 'k':
                    return [x,y]
            x+=75
        y+=75
        x=0
        
def generate_moves_for_opponenet(board_representation,isWhite):
    x=0
    y=0
    mo=[]
    for row in board_representation:
        for notation in row:
            if notation == 0:
                mo.append([[],[]])
            elif notation.isupper() == isWhite:
                move = GenerateMove(board_representation,[x,y])
                mo.append(move)
            else:
                mo.append([[],[]])
            x+=75
        x=0
        y+=75
    return mo