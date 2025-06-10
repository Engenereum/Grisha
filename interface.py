import pygame.font
from pygame import Surface


class Interface:
    def __init__(self):
        self.surf = Surface((200, 50))
        self.font = pygame.font.Font('alk-life-webfont.ttf', 50)
        self.level_font = pygame.font.Font('alk-life-webfont.ttf', 50)
        self.text = self.font.render('HP', 1, (155, 0, 0))
        self.level_text = self.font.render('HP', 1, (155, 0, 0))
        self.heart = pygame.image.load('textures/heart.png').convert_alpha()
        self.heart = pygame.transform.scale(self.heart, (50, 50))
        self.border = pygame.image.load("textures/border.png").convert_alpha()

    def draw(self, screen: Surface, count):
        screen.blit(self.text, (0, 0))
        rect = self.text.get_rect()
        size = screen.get_size()
        border = pygame.transform.scale(self.border, size)
        screen.blit(border, (0, 0))
        for i in range(count):
            screen.blit(self.heart, (rect.width + i * self.heart.get_width(), 0))
        if pygame.time.get_ticks() <= 3 * 1000:
            w, h = screen.get_size()
            rect = self.level_text.get_rect(center=(w // 2, h // 2))
            screen.blit(self.level_text, rect)

