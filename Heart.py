import pygame
import random
from Item import Item

WIDTH = 1200
HEIGHT = 800

class Heart(Item):
    def __init__(self, path, heartHeight, heartWidth):
        super().__init__()
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (heartWidth, heartHeight)).convert_alpha()
        self.rect = self.image.get_rect()

        x = random.randrange(0, WIDTH)
        y = random.randrange(-85, -35)
        self.rect.center = (x, y)

        self.heartWidth = heartWidth
        self.heartHeight = heartHeight
        self.speed = random.randrange(1, 6)

    def update(self, *args, **kwargs) -> None:
        super().update()
        if self.rect.y > HEIGHT - 60:
            self.rect.y = random.randrange(-50, -8)
            self.rect.x = random.randrange(self.heartWidth, WIDTH - self.heartWidth)
            self.speed = random.randrange(1, 6)