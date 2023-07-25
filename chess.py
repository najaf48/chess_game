import pygame,sys
from settings import Settings
from spritesheet import SpriteSheet
from pieces_creation import pieces_set
from board import Board

class ChessGame:  #overall class to manage chess game behaviour
    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        self.settings=Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Chess')
    def run_game(self):
        """Start the main loop for the game."""
        self.draw_chess_board()
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
    def draw_chess_board(self):
        start_fen='kqpppppp/ppp/PP'
        self.chess_board = Board()
        self.chess_board.drawBoard(self.screen)
        self.pieces_set()
        self.chess_board.fen_notation(start_fen,self.pieces.list_set)
        print(self.pieces.list_set[6].y)

    def _update_screen(self):
        pygame.display.flip()
    def images(self):
        sprite = SpriteSheet('Pieces.png')
        self.images_set = sprite.images_at()
    def pieces_set(self):
        self.images()
        self.pieces = pieces_set(self.images_set,self)
        self.pieces.create_set()
if __name__ == '__main__':
    chess_game = ChessGame()
    chess_game.run_game()