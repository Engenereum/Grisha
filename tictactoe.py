import pygame
from pygame import Surface, Rect

RES = HEIGHT,WIDTH=1000,800
FPS = 60
BOARD_SIZE = 10


class Board:
    def __init__(self,s:Surface):
        self.screen = s
        self.size = min(self.screen.get_size())
        self.cell_size = self.size//BOARD_SIZE
        self.shift = (max(self.screen.get_size()) - self.size) // 2
        self.rects = []
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                c = self.cell_size
                s = self.shift
                self.rects.append({
                    'rect':Rect(s+j*c,i*c,c,c),
                    'type': 'empty'
                })
        self.turn = 'cross'
        self.board_logic = []
        for i in range(BOARD_SIZE):
            self.board_logic.append([])
            for j in range(BOARD_SIZE):
                self.board_logic[i].append(0)


    def check_win(self)->bool:
        t = 1 if not self.turn == 'cross' else 2
        b = self.board_logic
        for i in range(0,BOARD_SIZE -5):
            for j in range(0,BOARD_SIZE-5):
                if b[i][j] == b[i+1][j+1] == b[i+2][j+2] == b[i+3][j+3] == b[i+4][j+4]==t:
                    return True
                elif b[i][j] == b[i+1][j+3] == b[i+2][j+2] == b[i+3][j+1]==b[i+4][j]==t:
                    return True
                for k in range(5):
                        if b[i+k][j]==b[i+k][j+1]==b[i+k][j+2]==b[i+k][j+3]==b[i+k][j+4]==t:
                            return True

                        elif b[i][j+k] == b[i+1][j+k]==b[i+2][j+k]==b[i+3][j+k]==b[i+4][j+k]==t:
                            return True


    def update(self,mouse_pos):
        for index,rect in enumerate(self.rects):
            if rect['rect'].collidepoint(mouse_pos) and rect['type'] == 'empty':
                rect["type"] = self.turn
                i=index//BOARD_SIZE
                j=index%BOARD_SIZE
                if self.turn == 'cross':
                    self.turn = 'circle'
                    self.board_logic[i][j]=1
                else:
                    self.turn = 'cross'
                    self.board_logic[i][j] = 2
                break

    def draw(self):
        for rect in self.rects:
                pygame.draw.rect(self.screen,(0,0,0),rect['rect'],2)
                if rect['type'] == 'cross':
                    pygame.draw.line(self.screen,(125,0,0), rect['rect'].topleft,rect['rect'].bottomright, 3)
                    pygame.draw.line(self.screen, (125, 0, 0), rect['rect'].topright, rect['rect'].bottomleft,3)
                elif rect['type'] == 'circle':
                    pygame.draw.circle(self.screen,(0,125,0),rect['rect'].center,self.cell_size//2-5,3)


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode(RES)
        pygame.display.set_caption('tic tac toe')
        self.clock = pygame.time.Clock()
        self.board = Board(self.screen)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                if event.type == pygame.MOUSEBUTTONDOWN:
                        self.board.update(event.pos)
            self.screen.fill((255,255,255))
            if self.board.check_win():
                winner = 'cross' if self.board.turn == 'circle' else 'circle'
                font = pygame.font.SysFont(None,32)
                text = font.render(f'win {winner}', 1,(255,165,0))
                self.screen.blit(text,text.get_rect(center = (600,450)))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running=False
            self.board.draw()

            pygame.display.flip()
            self.clock.tick(FPS)


if __name__== "__main__":
    pygame.init()
    app = App()
    app.run()