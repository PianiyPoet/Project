import pygame
import tank_control
from tank import Tank
from pygame.sprite import Group


def start():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("aaa")
    bg_color = (0, 0, 0)
    tank = Tank(screen)
    tbullets = Group()

    while True:
        tank_control.events(screen, tank, tbullets)
        tank.update_tank()
        tank_control.update(bg_color, screen, tank, tbullets)
        tank_control.update_tbullets(tbullets, tank)



start()
