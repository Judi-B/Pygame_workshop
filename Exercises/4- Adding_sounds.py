import pygame

#Initialize pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Adding sound!")

#load sound effects
sound_1 = pygame.mixer.Sound("explosion.wav")
sound_2 = pygame.mixer.Sound("pickupCoin.wav")

#play sound
sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)

#Change volume
sound_1.set_volume(0.1)
sound_1.play()

#Load background music
pygame.mixer.music.load("sound.wav")

#play background music
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(5000)
pygame.mixer.music.stop()

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


#End the game
pygame.quit()