import os

import pygame
from pygame import Surface


class Animation:
    def __init__(self, path):
        self.path = path
        files = os.listdir(path)
        self.images = []
        for file in files:
            image = self.src_image = pygame.image.load(f'{self.path}{file}').convert_alpha()
            image = pygame.transform.scale(image, (65, 65))
            self.images.append(image)
        self.index = 0
        self.image = self.images[self.index]
        self.counter = 0
        self.slower = 10

    def update(self):
        self.counter +=1
        if self.counter >= self.slower:
            self.index += 1
            self.index %= len(self.images)
            self.image = self.images[self.index]
            self.counter = 0

    def draw(self, screen: Surface):
        screen.blit(self.image, (0, 0))


class Application:
    def __init__(self):
        self.screen = pygame.display.set_mode((900, 600))
        self.clock = pygame.time.Clock()
        self.anim = Animation('anims/2/')

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.anim.update()
            self.screen.fill((0, 0, 0))
            self.anim.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(30)


if __name__ == '__main__':
    app = Application()
    app.run()
