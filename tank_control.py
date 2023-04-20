import pygame
import sys
from tank_bullet import Tbullet


def update(bg_color, screen, tank, tbullets):
    screen.fill(bg_color)
    for tbullet in tbullets.sprites():
        tbullet.draw_tbullet()
    tank.appear()
    pygame.display.flip()

def update_tbullets(tbullets, tank):
    tbullets.update(tank)


def events(screen, tank, tbullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                tank.mright = True
            elif event.key == pygame.K_a:
                tank.mleft = True
            elif event.key == pygame.K_w:
                tank.mfront = True
            elif event.key == pygame.K_s:
                tank.mback = True
            elif event.key == pygame.K_SPACE:
                new_tbullet = Tbullet(screen, tank)
                tbullets.add(new_tbullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                tank.mright = False
            elif event.key == pygame.K_a:
                tank.mleft = False
            elif event.key == pygame.K_w:
                tank.mfront = False
            elif event.key == pygame.K_s:
                tank.mback = False