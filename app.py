import pygame,sys,pygame_textinput
from config import *




class GUI():
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((widht,height))
        self.clock = pygame.time.Clock()
        self.rectlist = []
        self.startrect = None
        self.choosestart = False
        self.chooseend = False
        self.endrect = None
        pygame.display.set_caption('pathfinding')

        self.grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,3,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,3,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,3,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,3,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,3,3,3,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,2,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]
        
        self.createrectgrid()
    
    def run(self):
        while True:
            self.clock.tick(fps)
            pygame.display.flip()
            self.drawgrid()        
            self.updategrid()
            
            for event in pygame.event.get():
                key = pygame.key.get_pressed()

                if event.type == pygame.QUIT:
                    sys.exit()

                if key[pygame.K_r]:
                    self.choosestart = True

                if key[pygame.K_t]:
                    self.chooseend = True

                if key[pygame.K_q]:
                    self.startrect = None
                    self.choosestart = False
                    self.chooseend = False
                    self.endrect = None
                    for object, (rect,color,pos) in enumerate(self.rectlist):
                        self.rectlist[object] = (rect,'white',pos)
                
                if event.type == pygame.MOUSEBUTTONUP:

                    mouseposition = pygame.mouse.get_pos()
                    for object, (rect,color,pos) in enumerate(self.rectlist):
                        if rect.collidepoint(mouseposition):
                            if self.choosestart:
                                self.rectlist[object] = (rect,'green',pos)
                                self.startrect = self.rectlist[object]
                                self.choosestart = False
                            elif self.chooseend:
                                self.rectlist[object] = (rect,'red',pos)
                                self.endrect = self.rectlist[object]
                                self.chooseend = False
                            else:
                                self.rectlist[object] = (rect,'blue',pos)
                
                if key[pygame.K_SPACE]:
                    for row in self.grid:
                        print(row)


    def createrectgrid(self):
        for row_index, row in enumerate(self.grid):
            for col_index, col in enumerate(row):
                if col == 0:
                    rect = pygame.Rect((col_index*tilesize+((widht-(len(self.grid[1])*tilesize))/2),row_index*tilesize,tilesize-1,tilesize-1))
                    color = 'white'
                    pos = row_index,col_index
                    self.rectlist.append((rect,color,pos))
                if col == 1:
                    rect = pygame.Rect((col_index*tilesize+((widht-(len(self.grid[1])*tilesize))/2),row_index*tilesize,tilesize-1,tilesize-1))
                    color = 'green'
                    pos = row_index,col_index
                    self.rectlist.append((rect,color,pos))
                if col == 2:
                    rect = pygame.Rect((col_index*tilesize+((widht-(len(self.grid[1])*tilesize))/2),row_index*tilesize,tilesize-1,tilesize-1))
                    color = 'red'
                    pos = row_index,col_index
                    self.rectlist.append((rect,color,pos))
                if col == 3:
                    rect = pygame.Rect((col_index*tilesize+((widht-(len(self.grid[1])*tilesize))/2),row_index*tilesize,tilesize-1,tilesize-1))
                    color = 'blue'
                    pos = row_index,col_index
                    self.rectlist.append((rect,color,pos))


    def drawgrid(self):
        for rect,color,pos in self.rectlist:
            pygame.draw.rect(self.screen,color,rect)

    def updategrid(self):
        for rect,color,pos in self.rectlist:
            row_index,col_index = pos
            if color == 'white':
                self.grid[row_index][col_index] = 0
            if color == 'green':
                self.grid[row_index][col_index] = 1
            if color == 'red':
                self.grid[row_index][col_index] = 2
            if color == 'blue':
                self.grid[row_index][col_index] = 3

if __name__ is "__main__":
    gui = GUI()
    gui.run()