import pygame as py
py.init()
running = True
white = (255, 255, 255)
brown = (156, 70, 54)
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
                py.draw.rect(chess, brown,(x, y, 75, 75))
        else:
            if k%2==1:
                py.draw.rect(chess, brown,(x, y, 75, 75))
            else:
                py.draw.rect(chess, white,(x, y, 75, 75))
        x=x+75
    x=0
    y=y+75
py.display.update()
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running=False