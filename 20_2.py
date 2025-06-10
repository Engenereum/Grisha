import pygame
from pygame.draw_py import draw_line

pygame.init()
SIZE=800
screen = pygame.display.set_mode((SIZE,SIZE))
clock = pygame.time.Clock()
drawing = False
last_pos = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                print('lmb')
                last_pos=event.pos
                drawing = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_RIGHT:
                print('rmb')
                drawing = False
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if last_pos:
                    pygame.draw.line(screen,(255,0,255),last_pos,event.pos,3)
                    last_pos=event.pos
                else:
                    last_pos=event.pos
    buttons = pygame.mouse.get_pressed()
   # if buttons[0]:
    #    print('lbm')
   # if buttons[2]:
    #    print('rbm')

    pygame.display.flip()