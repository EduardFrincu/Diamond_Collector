import pygame
import random


WIDTH = 1200
HEIGHT = 800

class Item(pygame.sprite.Sprite):
    def __init__(self, path, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = random.randrange(1,6)
        self.rect.center = (x,y)


    def update(self, *args, **kwargs) -> None:
        self.rect.y += self.speed

