import pygame


class Tank():
    def __init__(self, screen):
        self.screen = screen
        self.img = pygame.image.load("tank_images/tank_front.png")
        self.fr = pygame.image.load("tank_images/tank_front.png")
        self.ri = pygame.image.load("tank_images/tank_right.png")
        self.ba = pygame.image.load("tank_images/tank_back.png")
        self.le = pygame.image.load("tank_images/tank_left.png")
        self.rect = self.img.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.mright = False
        self.mleft = False
        self.mfront = False
        self.mback = False


    def appear(self):
        self.screen.blit(self.img, self.rect)


    def update_tank(self):
        if self.mright and self.rect.right < self.screen_rect.right:
            self.img = self.ri
            self.centerx += 0.15
        elif self.mleft and self.rect.left > self.screen_rect.left:
            self.img = self.le
            self.centerx -= 0.15
        elif self.mfront and self.rect.top > self.screen_rect.top:
            self.img = self.fr
            self.centery -= 0.15
        elif self.mback and self.rect.bottom < self.screen_rect.bottom:
            self.img = self.ba
            self.centery += 0.15
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery