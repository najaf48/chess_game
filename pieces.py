import pygame
from spritesheet import SpriteSheet

"""Module to represent a chess set, and individual pieces."""

class Piece:
    """Represents a chess piece."""

    def __init__(self, name:str, color:int, image, chess_game):
        """Initialize attributes to represent a chess piece."""
        self.image = image
        self.name = name
        self.color = color

        self.screen = chess_game.screen

        # Start each piece off at the top left corner.
        self.x, self.y = 0.0, 0.0

        # Each piece is alive at start
        self.isalive = True

    def blitme(self):
        """Draw the piece at its current location."""
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)