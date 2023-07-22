import pygame,sys

screen = pygame.display.set_mode((600,600))
r=True
img=pygame.image.load('Pieces.png').convert_alpha()
screen.fill((156, 70, 54))
img = pygame.transform.scale(img,(600,200))
screen.blit(img,(0,0))
pygame.display.update()
while r:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            r=False