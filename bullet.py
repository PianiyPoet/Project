import pygame as pg


class Bullet(pg.sprite.Sprite):
    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pg.Rect(0, 0, 2, 10)
        self.color = 237, 28, 35
        self.speed = 1
        self.rect.centerx = gun.rect.centerx
        self.rect.centery = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pg.draw.rect(self.screen, self.color, self.rect)




