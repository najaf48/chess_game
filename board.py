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
    def fen_notation(self,notation,pieceSet):
        x=0
        y=0
        for n in notation:
            if n=='/':
                x=0
                y+=75
            for piece in pieceSet:
                if n==piece.name:
                    piece.x=x
                    piece.y=y
            x+=75