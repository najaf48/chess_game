import pygame
pygame.mixer.init()
move_sound = pygame.mixer.Sound('audios/move-self.mp3')
capture_sound = pygame.mixer.Sound('audios/capture.mp3')
def playbg():
    pygame.mixer.music.load('audios/bg.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
def move():
    global move_sound
    move_sound.play()
def capture():
    global capture_sound 
    capture_sound.play()
