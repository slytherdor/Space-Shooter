import pygame
from red_heart import Red_Heart
from play_button import Play_Button

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Consolas', 15)
pygame.display.set_caption("NPC Battle!")

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

r = 50
g = 0
b = 100

message = "Welcome to NPC Battle!"
display_message = my_font.render(message, True, (255, 255, 255))
message2 = "To start, please click on the play button below:"
display_message2 = my_font.render(message2, True, (255, 255, 255))

h = Red_Heart(1, 1)
pb = Play_Button(1, 1)

run = True
# -------- Main Program Loop -----------
while run:

    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if h.rect.collidepoint(event.pos):
                h.move(h.x + 3, h.y + 3)
    ##  ----- NO BLIT ZONE END  ----- ##

    ## FILL SCREEN, and BLIT here ##
    screen.fill((r, g, b))
    screen.blit(display_message, (0, 0))
    screen.blit(display_message2, (200, 400))
    screen.blit(h.image, h.rect)
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()





