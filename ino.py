import pygame as pg


class Ino(pg.sprite.Sprite):
    def __init__(self, screen):
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pg.image.load("images/ino.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def draw(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        self.y += 0.03
        self.rect.y = self.y