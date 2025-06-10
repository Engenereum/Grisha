import random

from pygame.sprite import Sprite, Group

from animation2 import Animation
from colisions import check_out_of_screen, is_collide_enemies, is_collide_spawn_enemies
from player import Player

enemies_paths = ['enemies/enemy_1/']
enemies_sleep = ['enemies/enemy_1/sleep/']

def spawn(count,screen):
    enemies=Group()
    current_count = 0
    while current_count<count:
        enemy_x,y = random.randint(300,600),random.randint(300,400),
        path = random.choice(enemies_paths)
        enemy = Enemy(path,enemy_x,y,screen)
        if is_collide_spawn_enemies(enemy.rect,enemies):
            continue
        else:
            enemies.add(enemy)
            current_count +=1
    return enemies


class Enemy(Sprite):
    def __init__(self,path, enemy_x,y,screen):
        super().__init__()
        self.screen = screen
        self.anims = {
            #'down': Animation(path+'down/'),
            #'right': Animation(path+'right/'),  # -_-
            #'up': Animation(path+'up/'),
            'fly':Animation(path+'fly/'),
            'sleep':Animation(path+'sleep/'),
        }
        self.anim = self.anims["sleep"]
        self.image = self.anim.image
        self.rect =  self.image.get_rect(center=(enemy_x,y))
        self.is_sleep = True
        ...


    def update(self, player:Player, enemies=None):
        x,y = self.rect.center
        x1,y1 = player.rect.center
        if x1>= 150:
            self.anim = self.anims['fly']
            self.is_sleep = False
        if not self.is_sleep:
            dx, dy = 0, 0
            if x < x1:
                dx += 1
            else:
                dx -= 1
            if y < y1:
                dy += 1
            else:
                dy -= 1
            rect = self.rect.move(dx, 0)
            if not check_out_of_screen(rect, self.screen)and is_collide_enemies(rect, enemies):
                self.rect = rect
            rect = self.rect.move(0, dy)
            if not check_out_of_screen(rect, self.screen)and is_collide_enemies(rect, enemies):
                self.rect = rect

        self.anim.update()
        self.image = self.anim.image

    def draw(self,screen):
        screen.blit(self.image,self.rect)