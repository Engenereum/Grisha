import pygame
from pygame import Surface, Rect

level1_map = [
    '1111111_1111111',
    '122222222222221',
    '122322222222221',
    '122222222222221',
    '_2222222222322_',
    '_2222222222222_',
    '122223222222221',
    '122222222322221',
    '122222222222221',
    '1111111_1111111',
]


class Environment:
    def __init__(self,screen:Surface):
        self.grid = []
        w,h = screen.get_size()
        self.rows_count = 10
        self.column_count = 15
        self.cell_w = w//self.column_count
        self.cell_h = h//self.rows_count
        self.textures = {
            '_':pygame.Surface((self.cell_w,self.cell_h)),
            '1':pygame.transform.scale(pygame.image.load('textures/fence.png').convert(),(self.cell_w,self.cell_h)),
            '2': pygame.transform.scale(pygame.image.load('textures/grass dark2.jpg').convert(), (self.cell_w, self.cell_h)),
            '3': pygame.transform.scale(pygame.image.load('textures/stone.png').convert_alpha(), (self.cell_w, self.cell_h)),
            '4': pygame.transform.scale(pygame.image.load('textures/bigstone.png').convert(), (self.cell_w, self.cell_h)),
        }
        for i in range(self.rows_count):
            self.grid.append([])
            for j in range(self.column_count):
                index = level1_map[i][j]
                self.grid[i].append({
                    'rect': Rect(j*self.cell_w,i*self.cell_h,self.cell_w,self.cell_h),
                    'texture':self.textures[index],
                })

    def draw(self,screen):
      for i in range(self.rows_count):
          for j in range(self.column_count):
              screen.blit(self.textures['2'], self.grid[i][j]['rect'])
              screen.blit(self.grid[i][j]['texture'],self.grid[i][j]['rect'])