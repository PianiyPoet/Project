import pygame as pg
import sys
from bullet import Bullet
from ino import Ino


def events(screen, gun, bullets):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                gun.mright = True
            elif event.key == pg.K_a:
                gun.mleft = True
            elif event.key == pg.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pg.KEYUP:
            if event.key == pg.K_d:
                gun.mright = False
            elif event.key == pg.K_a:
                gun.mleft = False


def update(bg_color, screen, gun, inos, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.appear()
    inos.draw(screen)
    pg.display.flip()


def update_bullets(inos, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pg.sprite.groupcollide(bullets, inos, True, True)


def create_army(screen, inos):
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((854 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((480 - 2 * ino_height - 100) / ino_height)

    for row in range(number_ino_y - 1):
        for ino_num in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_num
            ino.y = ino_height + ino_height * row
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row
            inos.add(ino)

def update_inos(gun, inos):
    inos.update()
    if pg.sprite.spritecollideany(gun, inos):
        print("!!!!!!!!!!!!!!!!!")


