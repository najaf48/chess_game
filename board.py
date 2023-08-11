import pygame

class Board:
    def __init__(self,screen):
        self.screen = screen
        self.board_representation = [['r','n','b','k','q','b','n','r'],
                                     ['p','p','p','p','p','p','p','p'],
                                     [0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0],
                                     ['P','P','P','P','P','P','P','P'],
                                     ['R','N','B','K','Q','B','N','R']]
        self.cordinates()

    def drawBoard(self):
        white = (255, 255, 255)
        green = (50, 168, 82)
        x = 0
        y = 0
        for i in range(8):
            for j in range(8):
                g = ((i+j)%2 == 0)
                squarecolor = white if g else green
                pygame.draw.rect(self.screen, squarecolor,(x, y, 75, 75))
                x += 75
            x = 0
            y += 75
    def cordinates(self):
        self.cord = {}
        x = 0
        y = 0
        for i in range(1,65):
            self.cord[i] = [x,y]
            x += 75
            if i%8 == 0:
                x = 0
                y += 75

    def fen_notation(self,notation,pieceSet):
        x = 0
        y = 0
        for n in notation:
            try:
                n = int(n)
                forward = (n-1)*75
                x += forward
            except:
                pass
            if n == 'k':
                pieceSet.king.locations.append([x,y])
            if n == 'q':
                pieceSet.queen.locations.append([x,y])
            if n == 'b':
                pieceSet.bishop.locations.append([x,y])
            if n == 'n':
                pieceSet.knight.locations.append([x,y])
            if n == 'r':
                pieceSet.rook.locations.append([x,y])
            if n == 'p':
                pieceSet.pawn.locations.append([x,y])
            if n == 'K':
                pieceSet.KING.locations.append([x,y])
            if n == 'Q':
                pieceSet.QUEEN.locations.append([x,y])
            if n == 'B':
                pieceSet.BISHOP.locations.append([x,y])
            if n == 'N':
                pieceSet.KNIGHT.locations.append([x,y])
            if n == 'R':
                pieceSet.ROOK.locations.append([x,y])
            if n == 'P':
                pieceSet.PAWN.locations.append([x,y])
            x += 75
            if n == '/':
                x = 0
                y += 75

    def selected_highlight(self,cords:list):
        s = pygame.Surface((75,75))
        s.set_alpha(180)
        s.fill((118, 118, 26))
        for cord in cords:
            self.screen.blit(s,(cord[0],cord[1]))
            # pygame.draw.rect(self.screen, (118, 118, 26),(cord[0], cord[1], 75, 75))
    def opponent_highlight(self,cords):
        s = pygame.Surface((75,75))
        # s.set_alpha(190)
        s.fill((248, 62, 62))
        for cord in cords:
            self.screen.blit(s,(cord[0],cord[1]))

    def update_board_representation(self,list_of_pieces_objects):
        for i in range(8):
            for j in range(8):
                self.board_representation[i][j]=0
        for piece in list_of_pieces_objects:
            for location in piece.locations:
                x = location[0]
                y = location[1]
                x = int(x/75)
                y = int(y/75)
                self.board_representation[y][x] = piece.name
        # print(self.board_representation)