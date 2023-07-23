import pygame,sys
from settings import Settings
from spritesheet import SpriteSheet
from pieces import Piece

class ChessGame:  #overall class to manage chess game behaviour
    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        self.settings=Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Chess')
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
    def _update_screen(self):
        self.drawBoard()
        pygame.display.flip()
    def drawBoard(self):
        white = (255, 255, 255)
        green = (50, 168, 82)
        x=0
        y=0
        for i in range(8):
            for j in range(8):
                g=((i+j)%2 != 0)
                squarecolor = white if g else green
                pygame.draw.rect(self.screen, squarecolor,(x, y, 75, 75))
                x+=75
            x=0
            y+=75
if __name__ == '__main__':
    chess_game = ChessGame()
    chess_game.run_game()