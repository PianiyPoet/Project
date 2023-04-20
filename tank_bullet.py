import pygame


class Tbullet(pygame.sprite.Sprite):
    def __init__(self, screen, tank):
        super(Tbullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 10)
        self.color = 237, 28, 35
        self.speed = 1
        self.rect.centerx = tank.rect.centerx
        self.rect.centery = tank.rect.centery
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self, tank):
        if tank.img == tank.fr:
            self.y -= self.speed
            self.rect.y = self.y
        elif tank.img == tank.ba:
            self.y += self.speed
            self.rect.y = self.y
        elif tank.img == tank.ri:
            self.x += self.speed
            self.rect.x = self.x
        elif tank.img == tank.le:
            self.x -= self.speed
            self.rect.x = self.x

    def draw_tbullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
