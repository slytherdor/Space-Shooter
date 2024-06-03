import pygame
import random
import time
from warrior import Warrior
from rock import Rock
from ghost import Ghost
from target import Target

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Consolas', 15)
pygame.display.set_caption("NPC Battle!")

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1400
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

bg = pygame.image.load("Grass.jpg")
hrt1 = pygame.image.load("heart.png")
hrt2 = pygame.image.load("heart.png")
hrt3 = pygame.image.load("heart.png")

name = "Collect coins as fast as you can!"
how_to_move = "Use WASD or Arrow Keys to move."
message = "Welcome to NPC Battle!"
message2 = "To start, please click on the play button below:"
message3 = "Manual: 1) WASD to move 2) Press e to end game"

win_message1 = ""

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
trgt = Target(1,1)

rand_rk = Rock(random.randint(0, 500), random.randint(10,340))
start_time = time.time()

lives = 3

trgt.set_location(random.randint(10, 1200), random.randint(10, 550))

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

    if (win == False and lose_by_time == False) and start == True:
        current_time = time.time()
        current_time -= start_time
        current_time = round(current_time, 2)

    if start:
        lose_time = round(10 - current_time, 2)
        display_time = my_font.render("Time remaining: " + str(lose_time) + "s", True, (255, 255, 255))
        if lose_time == 0:
            lose_by_time = True

    if start == True:
        if w.rect.colliderect(rk.rect) or rk.rect.colliderect(trgt.rect):
            rk.set_location(random.randint(10, 1200), random.randint(10, 550))
            lives -= 1
        if w.rect.colliderect(ghost.rect) or ghost.rect.colliderect(trgt.rect):
            ghost.set_location(random.randint(10, 1200), random.randint(10, 550))
            lives -= 1
        if current_time % 1 == 0 and wait:
            rk.set_location(random.randint(10, 1300), random.randint(10, 575))
            ghost.set_location(random.randint(10, 1300), random.randint(10, 575))
            wait = False
        if (current_time * 100) % 100 == 99:
            wait = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_e] == pygame.QUIT:  #
            run = False

    screen.fill((r, g, b))

    if start:
        screen.blit(bg,(0,0))
        screen.blit(w.image, w.rect)
        screen.blit(rk.image, rk.rect)
        screen.blit(ghost.image, ghost.rect)
        screen.blit(trgt.image, trgt.rect)
        screen.blit(display_name, (5, 0))
        screen.blit(display_time, (5, 15))
        if lives == 3:
            screen.blit(hrt1, (5, 35))
            screen.blit(hrt2, (25, 35))
            screen.blit(hrt3, (45, 35))
        if lives == 2:
            screen.blit(hrt1, (5, 35))
            screen.blit(hrt2, (25, 35))
        if lives == 1:
            screen.blit(hrt1, (5, 35))
    else:
        screen.blit(display_message, (130, 170))
        screen.blit(display_message2, (155, 150))
        screen.blit(display_message3, (100, 250))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()