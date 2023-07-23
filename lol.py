import pygame,sys
from spritesheet import SpriteSheet
screen = pygame.display.set_mode((600,600))
screen.fill((156, 70, 54))
r=True
img=SpriteSheet('Pieces.png')
# i=img.images_at([(0,0,333.33,334),(333.33,0,333.33,334)],-1)
# i[0] = pygame.transform.scale(i[0],(75,75))
# i[1] = pygame.transform.scale(i[1],(75,75))
# screen.blit(i[0],(0,0))
# screen.blit(i[1],(75,0))
i=img.image_at([0,0,333.33,334])
i=pygame.transform.scale(i,(75,75))
screen.blit(i,(0,0))

pygame.display.flip()
while r:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            r=False