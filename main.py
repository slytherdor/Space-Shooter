import pygame
import random
from warrior import Warrior
from rock import Rock

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

w = Warrior(40, 60)
warrior_lives = 3
rk = Rock(random.randint(0, 500), random.randint(10,340))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------
while run:
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

    # fox collision
    if w.rect.colliderect(r.rect):
        r.set_location(random.randint(0, 500), random.randint(10,340))
        warrior_lives -= 1

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((r, g, b))
    #red fox highscore
    screen.fill((r, g, b))
    screen.blit(display_message, (300, 350))
    screen.blit(display_message2, (200, 400))
    screen.blit(w.image, w.rect)
    pygame.display.update()
    ## END OF WHILE LOOP

    # Once we have exited the main program loop we can stop the game engine:
pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()



