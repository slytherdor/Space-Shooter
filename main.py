import pygame
import random
import time
from warrior import Warrior
from rock import Rock
from ghost import Ghost

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Consolas', 15)
pygame.display.set_caption("NPC Battle!")

# set up variables for the display
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1400
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

name = "Collect coins as fast as you can!"
how_to_move = "Use WASD or Arrow Keys to move."
message = "Welcome to NPC Battle!"
message2 = "To start, please click on the play button below:"
message3 = "Manual: 1) WASD to move 2) Press e to end game"

warrior_score = 0
r = 50
g = 0
b = 100
random_spawn = random.randint(3, 7)
# render the text for later
display_message = my_font.render(message, True, (255, 255, 255))
display_message2 = my_font.render(message2, True, (255, 255, 255))
display_message3 = my_font.render(message3, True, (255, 255, 255))
display_name = my_font.render(name, True, (255, 255, 255))

w = Warrior(40, 60)
rk = Rock(1,1)
ghost = Ghost(1,1)
rand_rk = Rock(random.randint(0, 500), random.randint(10,340))
start_time = time.time()

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
win = False
lose_by_time = False
start = False
check = True
wait = True

# -------- Main Program Loop -----------
while run:

    if start and check:
        start_time = time.time()
        check = False
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

    if (win == False and lose_by_time == False) and start == True:
        current_time = time.time()
        current_time -= start_time
        current_time = round(current_time, 2)

    if start:
        lose_time = round(10 - current_time, 2)
        display_time = my_font.render("Time remaining: " + str(lose_time) + "s", True, (255, 255, 255))
        if lose_time == 0:
            lose_by_time = True


    if w.rect.colliderect(rk.rect):
        rk.set_location(random.randint(10, 1200), random.randint(10, 800))
    if w.rect.colliderect(ghost.rect):
        ghost.set_location(random.randint(10, 1200), random.randint(10, 800))
    if start:
        if current_time % 2 == 0 and wait:
            rk.set_location(random.randint(10, 1200), random.randint(10, 800))
            ghost.set_location(random.randint(10, 1200), random.randint(10, 800))
            wait = False
        if (current_time * 100) % 100 == 99:
            wait = True


    # --- Main event loop
    for event in pygame.event.get():
        if current_time == 0:

        if event.type == pygame.QUIT:  #
            run = False

    screen.fill((r, g, b))

    if start:
        screen.blit(w.image, w.rect)
        screen.blit(rk.image, rk.rect)
        screen.blit(ghost.image, ghost.rect)
        screen.blit(display_name, (0, 0))
        screen.blit(display_time, (0, 15))
    else:
        screen.blit(display_message, (130, 170))
        screen.blit(display_message2, (155, 150))
        screen.blit(display_message3, (100, 250))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
