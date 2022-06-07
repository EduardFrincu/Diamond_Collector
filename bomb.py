import pygame
import random
from Item import Item


WIDTH = 1200
HEIGHT = 800

class Bomb(Item):
    def __init__(self, path, bombHeight, bombWidth):
        super().__init__()
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (bombWidth, bombHeight)).convert_alpha()
        self.rect = self.image.get_rect()
        x = random.randrange(0, WIDTH)
        y = random.randrange(-85, -35)
        self.rect.center = (x, y)
        self.bombWidth = bombWidth
        self.bombHeight = bombHeight
        self.speed = random.randrange(1, 6)


    def update(self, *args, **kwargs) -> None:
        super().update()

        if self.rect.y > HEIGHT-60:
            self.rect.y = random.randrange(-50,-8)
            self.rect.x = random.randrange(self.bombWidth, WIDTH-self.bombWidth)
            self.speed = random.randrange(1, 6)
