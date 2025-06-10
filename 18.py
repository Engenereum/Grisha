import pygame


pygame.init()

screen = pygame.display.set_mode((500,300))

pygame.display.set_caption('пипидастр')


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    screen.fill((50,50,50))

    pygame.draw.rect(screen, (255,255,255), (250,150,250,150))
    pygame.draw.rect(screen, (255,255,255), (0,0,250,150))
    pygame.draw.circle(screen, (255, 55, 255), (250, 150), 100)
    pygame.draw.line(screen,(0,0,0),(500,0),(0,300), 5)
    pygame.draw.line(screen,(0,0,0),(0,0),(500,300), 5)
    pygame.draw.line(screen, (0, 0, 0), (250, 300), (250, 0), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 150), (500, 150), 5)
    pygame.display.flip()