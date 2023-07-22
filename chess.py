import pygame,sys
from settings import Settings

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
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    chess_game = ChessGame()
    chess_game.run_game()