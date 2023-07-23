# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

# Additional notes
# - Further adaptations from https://www.pygame.org/wiki/Spritesheet
# - Cleaned up overall formatting.
# - Updated from Python 2 -> Python 3.

import pygame

class SpriteSheet:

    def __init__(self, filename):
        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)


    def image_at(self, rectangle, colorkey = None):
        """Load a specific image from a specific rectangle."""
        # Loads image from x, y, x+offset, y+offset.
        # rect = pygame.Rect(rectangle)
        # image = pygame.Surface(rect.size)   
        # image.blit(self.sheet, (0, 0), rect)                          old method
        # if colorkey is not None:
        #     if colorkey == -1:
        #         colorkey = image.get_at((0,0))
        #     image.set_colorkey(colorkey, pygame.RLEACCEL)
        # return image
        cropped = self.sheet.subsurface(rectangle)
        return cropped


    def images_at(self,widthofsheet:int,heightofsheet:int,num_img_x:int,num_img_y:int):
        height_reduced=heightofsheet/num_img_y
        width_reduced=widthofsheet/num_img_x
        rects=[]
        x=0
        y=0
        for i in range(0,num_img_y):
            for k in range(0,num_img_x):
                rect=[x,y,width_reduced,height_reduced]
                rects.append(rect)
                x=x+width_reduced
            x=0
            y=y+height_reduced
        return [self.image_at(rect) for rect in rects]

    # def images_at(self, rects, colorkey = None):                          old method
        """Load a whole bunch of images and return them as a list."""
        # return [self.image_at(rect, colorkey) for rect in rects]


    def load_strip(self, rect, image_count, colorkey = None):
        """Load a whole strip of images, and return them as a list."""
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
    