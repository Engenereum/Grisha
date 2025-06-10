import pygame
from pygame import Surface


class Animation:
    def __init__(self):
        self.src_image = pygame.image.load('metelka-pipidastr.jpg').convert()
        self.src_image.set_colorkey((255,255,255))
        self.src_image = pygame.transform.scale(self.src_image,(900,600))
        self.rect = self.src_image.get_rect()
        self.image =  self.src_image
        self.angle = 0
    def update(self):
        self.image = pygame.transform.rotate(self.src_image,self.angle)
        self.angle += 1
    def draw(self,screen: Surface):
        self.rect = screen.get_rect(center=(300,450))
        screen.blit(self.image,(0,0))


class Application:
    def __init__(self):
        self.screen = pygame.display.set_mode((900,600))
        self.clock = pygame.time.Clock()
        self.anim = Animation()
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
            self.anim.update()
            self.screen.fill((0,0,0))
            self.anim.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(30)


if __name__ == '__main__':
    app = Application()
    app.run()