import pygame
import random
from Item import Item


WIDTH = 1200
HEIGHT = 800

class Bomb(Item):
    def __init__(self, path, x,y, bombHeight, bombWidth):
        super().__init__(path, x, y)
        self.image = pygame.transform.scale(self.image, (bombWidth, bombHeight)).convert_alpha()
        self.rect = self.image.get_rect()
        self.bombWidth = bombWidth
        self.bombHeight = bombHeight

    def update(self, *args, **kwargs) -> None:
        super().update()

        if self.rect.y > HEIGHT-60:
            self.rect.y = random.randrange(-50,-8)
            self.rect.x = random.randrange(self.bombWidth, WIDTH-self.bombWidth)
