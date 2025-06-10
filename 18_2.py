import pygame

pygame.init()

size = int(input())
count = int(input())
square = size // count
is_black = True
screen = pygame.display.set_mode((size, size))

pygame.display.set_caption('шахматы')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    is_black = True
    screen.fill((50, 50, 50))
    for n in range(count):
        for i in range(count):
            if is_black:
                color = (0, 0, 0)
            else:
                color = (255, 255, 255)
            is_black = not is_black
            pygame.draw.rect(screen, color, (n * square, i * square, square, square))

    pygame.display.flip()
