import pygame
import random
from Item import Item


WIDTH = 1200
HEIGHT = 800

class Gem(Item):
    def __init__(self, path,gemHeight, gemWidth):
        super().__init__()
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (gemWidth, gemHeight)).convert_alpha()
        self.rect = self.image.get_rect()
        x = random.randrange(0, WIDTH)
        y = random.randrange(-85, -35)
        self.rect.center = (x, y)
        self.gemWidth = gemWidth
        self.gemHeight = gemHeight
        self.speed = random.randrange(1, 6)


    def update(self, *args, **kwargs) -> None:
        super().update()
        if self.rect.y > HEIGHT-60:
            self.rect.y = random.randrange(-50,-8)
            self.rect.x = random.randrange(self.gemWidth, WIDTH-self.gemWidth)
            self.speed = random.randrange(1, 6)

