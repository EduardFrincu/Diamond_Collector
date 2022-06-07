import pygame
import random


WIDTH = 1200
HEIGHT = 800


class Item(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 0





    def update(self, *args, **kwargs) -> None:
        self.rect.y += self.speed


