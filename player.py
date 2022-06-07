import pygame

WIDTH = 1200
HEIGHT = 800


class Miner(pygame.sprite.Sprite):
    def __init__(self, path, x,y, minerHeight, minerWidth):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (minerWidth,minerHeight))

        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def update(self, *args, **kwargs) -> None:
         mouse_x, mouse_y = pygame.mouse.get_pos()
         pygame.mouse.set_visible(False)
         self.rect.x = mouse_x

        #boundaries
         if self.rect.x > WIDTH - 120:
            self.rect.x = WIDTH - 120
         if self.rect.x < 0:
            self.rect.x = 0

    def getX(self):
        return self.rect.x
