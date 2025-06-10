import pygame.event
from pygame.sprite import Sprite

from animation2 import Animation
from colisions import check_out_of_screen


class Player(Sprite):
    def __init__(self,screen):                         #-_-
        super().__init__()
        self.screen = screen
        self.anims = {
            'down':Animation('anims/down/'),
            'right':Animation('anims/right/'),                  #-_-
            'up':Animation('anims/up/'),
            'left':Animation('anims/left/'),
            'idle_down':Animation('anims/idle_down/'),
            'idle_up': Animation('anims/idle_up/'),
            'idle_left': Animation('anims/idle_left/'),
            'idle_right': Animation('anims/idle_right/'),
        }
        self.image = self.anims['down'].image
        self.rect = self.image.get_rect(center=(350,350))
        self.current_anim = 'down'
        self.previous_anim = 'down'                    #-_-
        self.anim = self.anims[self.current_anim]
    def update(self,events,keys):
        w = keys[pygame.K_w]
        a = keys[pygame.K_a]
        s = keys[pygame.K_s]
        d = keys[pygame.K_d]
        if w:
            self.current_anim = 'up'
            self.previous_anim = 'up'
        elif s:
            self.current_anim = 'down'
            self.previous_anim = 'down'
        elif a:
            self.current_anim = 'left'
            self.previous_anim = 'left'
        elif d:
            self.current_anim = 'right'
            self.previous_anim = 'right'

        else:
            if self.previous_anim == 'up':
                self.current_anim = 'idle_up'
            elif self.previous_anim == 'down':
                self.current_anim = 'idle_down'
            elif self.previous_anim == 'left':
                self.current_anim = 'idle_left'
            elif self.previous_anim == 'right':
                self.current_anim = 'idle_right'

        self.anim = self.anims[self.current_anim]
        x, y = 0,0                                         #-_-
        self.anim.update()
        self.image = self.anim.image





#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

        if keys[pygame.K_a]:
            x-=2.5
        if keys[pygame.K_d]:
            x+=2
        if keys[pygame.K_w]:
            y -= 2.5
        if keys[pygame.K_s]:
            y += 2
        rect = self.rect.move(x, 0)
        if not check_out_of_screen(rect, self.screen):
            self.rect = rect
        rect = self.rect.move(0, y)
        if not check_out_of_screen(rect, self.screen):
            self.rect = rect

    def draw(self,screen):
        screen.blit(self.image,self.rect)

