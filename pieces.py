import pygame

"""Module to represent a chess set, and individual pieces."""

class Piece:
    """Represents a chess piece."""

    def __init__(self, color, image, chess_game, name=None):
        """Initialize attributes to represent a chess piece."""
        self.image = image
        self.name = name
        self.color = color

        self.screen = chess_game.screen

        # Start each piece off at the top left corner.
        self.x, self.y = 0.0, 0.0
        self.locations = []
        # Each piece is alive at start
        self.isalive = True

    def blitme(self):
        """Draw the piece at its current location."""
        # self.rect = self.image.get_rect()
        # self.rect.topleft = self.x, self.y
        # self.rect=(self.x,self.y)
        for location in self.locations:
            self.screen.blit(self.image,tuple(location))
    def loacteme(self,location):
        self.x=location[0]
        self.y=location[1]