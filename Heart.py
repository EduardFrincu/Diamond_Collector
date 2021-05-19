import pygame
import random
from Item import Item

WIDTH = 1200
HEIGHT = 800

class Heart(Item):
    def __init__(self, path, x, y, heartHeight, heartWidth):
        super().__init__(path, x, y)
        self.image = pygame.transform.scale(self.image, (heartWidth, heartHeight)).convert_alpha()
        self.rect = self.image.get_rect()
        self.heartWidth = heartWidth
        self.heartHeight = heartHeight

    def update(self, *args, **kwargs) -> None:
        super().update()
        if self.rect.y > HEIGHT - 60:
            self.rect.y = random.randrange(-50, -8)
            self.rect.x = random.randrange(self.heartWidth, WIDTH - self.heartWidth)