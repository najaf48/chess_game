import pygame
from settings import Settings
class Board:
    def __init__(self):
        setting=Settings()
        width = setting.screen_width
        height = setting.screen_width
        self.cordinates()
    def drawBoard(self,screen):
        white = (255, 255, 255)
        green = (50, 168, 82)
        x=0
        y=0
        for i in range(8):
            for j in range(8):
                g=((i+j)%2 == 0)
                squarecolor = white if g else green
                pygame.draw.rect(screen, squarecolor,(x, y, 75, 75))
                x+=75
            x=0
            y+=75
    def cordinates(self):
        self.cord = {1:[0,0]}
        x=0
        y=0
        for i in range(1,65):
            self.cord[i]=[x,y]
            x+=75
            if i%8==0:
                x=0
                y+=75
    # def fen_notation(self,notation,pieceSet):
    #     x=0
    #     y=0
    #     for n in notation:
    #         if n=='k':
    #             pieceSet.king.locations.append([x,y])
    #         if n=='q':
    #             pieceSet.queen.locations.append([x,y])
    #         if n=='b':
    #             pieceSet.bishop.locations.append([x,y])
    #         if n=='n':
    #             pieceSet.knight.locations.append([x,y])
    #         if n=='r':
    #             pieceSet.rook.locations.append([x,y])
    #         if n=='p':
    #             pieceSet.pawn.locations.append([x,y])
    #         if n=='K':
    #             pieceSet.KING.locations.append([x,y])
    #         if n=='Q':
    #             pieceSet.QUEEN.locations.append([x,y])
    #         if n=='B':
    #             pieceSet.BISHOP.locations.append([x,y])
    #         if n=='N':
    #             pieceSet.KNIGHT.locations.append([x,y])
    #         if n=='R':
    #             pieceSet.ROOK.locations.append([x,y])
    #         if n=='P':
    #             pieceSet.PAWN.locations.append([x,y])
    #         x+=75
    #         if n=='/':
    #             x=0
    #             y+=75
    def fen_notation(self,notation,pieceSet):
        x=0
        y=0
        for n in notation:
            try:
                n=int(n)
                forward = (n-1)*75
                x+=forward
            except:
                pass
            if n=='k':
                pieceSet.king.locations.append([x,y])
            if n=='q':
                pieceSet.queen.locations.append([x,y])
            if n=='b':
                pieceSet.bishop.locations.append([x,y])
            if n=='n':
                pieceSet.knight.locations.append([x,y])
            if n=='r':
                pieceSet.rook.locations.append([x,y])
            if n=='p':
                pieceSet.pawn.locations.append([x,y])
            if n=='K':
                pieceSet.KING.locations.append([x,y])
            if n=='Q':
                pieceSet.QUEEN.locations.append([x,y])
            if n=='B':
                pieceSet.BISHOP.locations.append([x,y])
            if n=='N':
                pieceSet.KNIGHT.locations.append([x,y])
            if n=='R':
                pieceSet.ROOK.locations.append([x,y])
            if n=='P':
                pieceSet.PAWN.locations.append([x,y])
            x+=75
            if n=='/':
                x=0
                y+=75