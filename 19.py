import pygame


FPS = 144
pygame.init()
screen = pygame.display.set_mode((500,300))
clock = pygame.time.Clock()
pygame.display.set_caption('manchkin')
x=0
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
    x += 0.5
    if x > 555:
        x=-50
    if (speed_y > 0 and y + speed_y >= 500) or (speed_y < 0 and y +speed_y <= 0):
        speed_y = -speed_y
    if (speed_y > 0 and y + speed_y >= 300) or (speed_y < 0 and y +speed_y <= 0):
        speed_y = -speed_y
    y += speed_y
    x += speed_x
    width = (width+1)%100
    screen.fill((50,50,50))
    pygame.draw.circle(screen,(0,0,0), (x,200), 50)
    pygame.draw.rect(screen,(0,0,0), (x,y,50,50), 50)
    pygame.display.flip()
    clock.tick(FPS)