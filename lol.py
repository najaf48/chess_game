import pygame,sys

screen = pygame.display.set_mode((600,600))
r=True
while r:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            r=False
img=pygame.