import pygame
from red_heart import Red_Heart
from warrior import Warrior

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
message3 = "Manual: 1) WASD to move 2) Press K to attack 3) Press e to end game"
display_message3 = my_font.render(message3, True, (255, 255, 255))

h = Red_Heart(1, 1)
w = Warrior(5, 5)

run = True
start = False
# -------- Main Program Loop -----------
while run:
    if start:
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_d]:
            w.move_direction("right")
            start = True
        if keys[pygame.K_a]:
            w.move_direction("left")
            start = True
        if keys[pygame.K_s]:
            w.move_direction("down")
            start = True
        if keys[pygame.K_w]:
            w.move_direction("up")
            start = True

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((r, g, b))
    screen.blit(display_message, (300, 350))
    screen.blit(display_message2, (200, 400))
    screen.blit(h.image, h.rect)
    screen.blit(w.image, w.rect)
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
