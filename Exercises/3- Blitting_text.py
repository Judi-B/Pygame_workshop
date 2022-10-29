import pygame

#Initialize pygame
pygame.init()

#Create display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting text")

#Define colors
GREEN = (0,255,0)
DARKGREEN = (10,50,10)
BLACK = (0,0,0)

#Set background
display_surface.fill((255,150,255))

#See all available fonts
fonts = pygame.font.get_fonts()


#Define fonts
System_font = pygame.font.SysFont("copperplategothic", 64)

#Define text
System_text = System_font.render("Hello world!", True, (255,150,255),(255,255,255))
System_text_rect = System_text.get_rect()
System_text_rect.center = (WINDOW_WIDTH//2,150)

#The main game loop 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Blit text surface to display surface
    display_surface.blit(System_text,System_text_rect)


    #Update the background
    pygame.display.update()

#End the game 
pygame.quit()