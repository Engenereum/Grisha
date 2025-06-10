import pygame

from enemy import spawn
from environment import Environment
from player import Player

def create_cursor():
    surface = pygame.Surface((50,50),pygame.SRCALPHA)
    hotspot = (25,25)
    pygame.draw.circle(surface,(255,255,255),(25,25),5)
    cursor = pygame.cursors.Cursor(hotspot,surface)
    return cursor



class App:                                                              #-_-
    def __init__(self):
        self.screen = pygame.display.set_mode((1000,700))
        self.clock = pygame.time.Clock()                                            #-_-
        self.player = Player(self.screen)
        self.map = Environment(self.screen)
        self.enemies = spawn(5,self.screen)
        pygame.mouse.set_cursor(create_cursor())
    def run(self):
        running=True
        while running:                                                              #-_-
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running=False
            keys = pygame.key.get_pressed()
            self.player.update(events, keys)
            self.enemies.update(self.player,self.enemies)
            self.screen.fill(pygame.color.Color('white')) #MediumVioletRed
            self.map.draw(self.screen)
            self.player.draw(self.screen)
            self.enemies.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    app = App()
    app.run()