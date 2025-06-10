import pygame
from pygame.examples.moveit import HEIGHT

FPS = 144
WIDTH = 500
HEIGHT = 300
pygame.init()
screen = pygame.display.set_mode((500,300))
clock = pygame.time.Clock()
rect = pygame.Rect(WIDTH//2,HEIGHT//2,50,50)

class Rect:
    def __init__(self,speed_x,speed_y, x , y):
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x,self.y,50,50)

    def move(self,another_rect : pygame.Rect):
       if(self.speed_x >= 0 and self.rect.right > WIDTH) or (self.speed_x < 0 and self.rect.left < 0):
           self.speed_x = -self.speed_x

       if (self.speed_y >= 0 and self.rect.bottom > HEIGHT) or(self.speed_y < 0 and self.rect.top < 0):
           self.speed_y = -self.speed_y

       if self.rect.colliderect(another_rect):
           self.speed_x = -self.speed_x
           self.speed_y = -self.speed_y
       self.rect.move_ip(self.speed_x,self.speed_y)




rect = Rect(5,10, 80, 90)
rect2 = Rect(5,10,180, 60)
pygame.display.set_caption('zhopa')
x=0
x2=0
x3=500
x4=0
y3 = 300
y4 = 0
y = 0
speed_y=2
speed_x = 3
width = 5
running = True
while running:
    print(clock.get_fps())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rect.move(rect2)
    rect2.move(rect)

    x+=3
    x2+=2
    x3+=-500//300
    y3+=-1
    x4+=2
    y4+=2
    if x >= 500:
        x = 0
    if x2 >= 300:
        x2 = 0
    if x3 <= 0:
        x3=500
    if y3 <= 0:
        y3=300
    if x4 >= 500:
         x4 = 0
    if y4 >= 300:
        y4 = 0
    screen.fill((50,50,50))
    pygame.draw.rect(screen, (255,0,255),rect.rect)
    pygame.draw.rect(screen, (255,0,255),rect2.rect)
   #pygame.draw.circle(screen,(0,0,0), (x,200), 25)
   #pygame.draw.circle(screen, (0, 0, 0), (250, x2), 25)
   #pygame.draw.circle(screen, (0, 0, 0), (x3, y3), 25)
   #print(x3, y3)
   #pygame.draw.circle(screen, (0, 0, 0), (x4, y4), 25)
    pygame.display.flip()
    clock.tick(FPS)