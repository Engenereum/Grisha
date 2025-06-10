import copy

from pygame import Surface, Rect


def check_out_of_screen(obj: Rect, screen: Surface) -> bool:
    w, h = screen.get_size()
    if obj.left <= 55:
        return True
    elif obj.right >= w-65:
        return True
    elif obj.top <= 48:
        return True
    elif obj.bottom >= h-65:
        return True
    else:
        return False


def is_collide_spawn_enemies(enemy: Rect, enemies) -> bool:
    enemy_rects = []
    for en in enemies:
        enemy_rects.append(en.rect)
    res = enemy.collidelist(enemy_rects)
    print(res)
    if res > -1:
        return True
    else:
        return False


def is_collide_enemies(enemy: Rect, enemies) -> bool:
    enemy_rects = []
    for en in enemies:
        enemy_rects.append(en.rect)
    res = enemy.collidelist(enemy_rects)
    print(res)
    if res > 0:
        return True
    else:
        return False
