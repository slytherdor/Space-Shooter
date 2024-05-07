import pygame
from red_heart import Red_Heart

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans', 13)
big_font = pygame.font.SysFont('Comic Sans', 16)
pygame.display.set_caption("Coin Collector!")

heart = pygame.image.load('red heart.png')

health = Red_Heart(40, 60)

screen.blit(f.image, f.rect)

keys = pygame.key.get_pressed()  # checking pressed keys
if keys[pygame.K_d]:
   f.move_direction("right")
   start = True
if keys[pygame.K_a]:
   f.move_direction("left")
   start = True
if keys[pygame.K_s]:
   f.move_direction("down")
   start = True
if keys[pygame.K_w]:
   f.move_direction("up")
   start = True


size = (800, 1000)
screen = pygame.display.set_mode(size)
