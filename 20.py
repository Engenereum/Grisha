import pygame
from pygame import Rect
clock = pygame.time.Clock()
FPS = 60

class Triangle:
    def __init__(self, p1:tuple,p2:tuple,p3:tuple):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3
        self.bottom = max(p1[1], p2[1], p3[1])

    def draw(self,screen,color,width=1):
        pygame.draw.line(screen,color,self.point1,self.point2,width)
        pygame.draw.line(screen, color, self.point1, self.point3,width)
        pygame.draw.line(screen,color,self.point2,self.point3,width)
    def draw_filled(self,screen,color):
        pygame.draw.polygon(screen,color,[self.point3,self.point2,self.point3])


    def move_ip(self,x,y):
       self.point1 = self.point1[0] + x,self.point1[1] + y
       self.point2 = self.point2[0] + x, self.point2[1] + y
       self.point3 = self.point3[0] + x, self.point3[1] + y
       self.bottom = max(self.point1[1], self.point2[1], self.point3[1])

    def set_bottom(self,y):
        delta_y=self.bottom - y
        self.move_ip(0,delta_y)





if __name__ == '__main__':
    pygame.init()
    SIZE = 900,600
    screen = pygame.display.set_mode((500 ,300))
    trian = Triangle((50,50),(0,150),(100,150))

    running = True
    its_jump = True
    jump_force = 0
    gravity = 3
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False



        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            trian.move_ip(0,-10)
        if keys[pygame.K_d]:
            trian.move_ip(10,0)
        if keys[pygame.K_a]:
            trian.move_ip(-10, 0)
        #if keys[pygame.K_s]:
        #   trian.move_ip(0, 10)
        if keys[pygame.K_r]:
            Triangle((50,50),(0,150),(100,150))

        if keys[pygame.K_SPACE]:
            if its_jump:
                jump_force = 10

        if trian.bottom < 250:
            trian.move_ip(0,jump_force)
            jump_force=jump_force+gravity
            its_jump=False
        else:
            trian.set_bottom(250)

        screen.fill(pygame.color.Color('cyan2'))
        rect = Rect(0,250,500,50)
        pygame.draw.rect(screen,pygame.color.Color('green'),rect)
        trian.draw(screen,pygame.color.Color('white'),2)


        pygame.display.flip()

        clock.tick(FPS)