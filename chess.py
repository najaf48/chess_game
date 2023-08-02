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
        self.fen_notation = 'rnbkqbnr/pppppppp/////PPPPPPPP/RNBKQBNR'
        self.selected_piece = None
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.selected_piece!=None:
                        x=event.pos[0]
                        y=event.pos[1]
                        x=(int(x/75))*75
                        y=(int(y/75))*75
                        colliding_piece = self.pieces.check_collide([x,y])
                        colliding_piece.locations.remove([x,y])
                        self.selected_piece.locations.append([x,y])
                        self.selected_piece.locations.remove(self.cord)
                        print(self.selected_piece.locations)
                        self.selected_piece=None
                        break
                    elif self.selected_piece==None:
                        x=event.pos[0]
                        y=event.pos[1]
                        x=(int(x/75))*75
                        y=(int(y/75))*75
                        self.cord=[x,y]
                        self.selected_piece = self.pieces.check_collide(self.cord)
                        print(self.selected_piece)

    def draw_chess_board(self):
        self.chess_board = Board()
        self.chess_board.drawBoard(self.screen)
        self.images()
        self.pieces_set()
        self.update_location_of_pieces(self.fen_notation)
        self._update_screen()

    def _update_screen(self):
        self.chess_board.drawBoard(self.screen)
        self.pieces.drawPieces()
        pygame.display.flip()

    def images(self):
        sprite = SpriteSheet('Pieces.png')
        self.images_set = sprite.images_at()

    def pieces_set(self):
        self.pieces = pieces_set(self)
        self.pieces.create_set(self.images_set)

    def update_location_of_pieces(self,notation):
        self.chess_board.fen_notation(notation,self.pieces)

if __name__ == '__main__':
    chess_game = ChessGame()
    chess_game.run_game()