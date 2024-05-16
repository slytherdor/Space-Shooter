import pygame
class Warrior:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("warrior.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 2
        self.right = True


    def move_direction(self, direction):
        if direction == "right":
            self.x = self.x + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "left":
            self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "down":
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "up":
            self.y = self.y - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "left" and self.right == True:
            self.image = pygame.transform.flip(self.image, True, False)
            self.right = False
        if direction == "right" and self.right == False:
            self.image = pygame.transform.flip(self.image, True, False)
            self.right = True





