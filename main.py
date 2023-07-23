import pygame as py
from spritesheet import SpriteSheet
py.init()
running = True
white = (255, 255, 255)
green = (50, 168, 82)
chess = py.display.set_mode((600,600))
py.display.set_caption('Chess')
x=0
y=0
# py.draw.rect(chess, white,(0, 75, 75, 75))
for i in range(1,9):
    for k in range(1,9):
        if i%2==1:
            if k%2==1:
                py.draw.rect(chess, white,(x, y, 75, 75))
            else:
                py.draw.rect(chess,
                green,(x, y, 75, 75))
        else:
            if k%2==1:
                py.draw.rect(chess,
                green,(x, y, 75, 75))
            else:
                py.draw.rect(chess, white,(x, y, 75, 75))
        x=x+75
    x=0
    y=y+75
SpriteToImage=SpriteSheet('Pieces.png')
# i=img.image_at([0,0,333.33,334])
# i=py.transform.scale(i,(75,75))
images = SpriteToImage.images_at(2000,668,6,2)
for i in range(len(images)):
    images[i]=py.transform.scale(images[i],(75,75))
x=0
y=0
l=[]
for i in range(len(images)):
    t=(images[i],(x,y))
    x+=75
    if i==7:
        x=0
        y+=75
    l.append(t)
chess.blits(l)
py.display.update()
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running=False