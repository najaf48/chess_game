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
        self.locations = []

    def blitme(self):
        """Draw the piece at its current location."""
        for location in self.locations:
            self.screen.blit(self.image,location)