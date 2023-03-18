import pygame,sys,pygame_textinput
from time import sleep
from config import *
import math



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
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,3,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,3,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,3,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,3,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,3,3,3,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
                                self.rectlist[object] = (rect,'purple',pos)
                                self.startrect = self.rectlist[object]
                                self.choosestart = False
                            elif self.chooseend:
                                self.rectlist[object] = (rect,'pink',pos)
                                self.endrect = self.rectlist[object]
                                self.chooseend = False
                            else:
                                self.rectlist[object] = (rect,'blue',pos)
                
                if key[pygame.K_SPACE]:
                    for row in self.grid:
                        print(row)
                        self.astar()


    def createrectgrid(self):
        self.rectlist = []
        for row_index, row in enumerate(self.grid):
            for col_index, col in enumerate(row):
                if col == 0:
                    rect = pygame.Rect((col_index*tilesize+((widht-(len(self.grid[1])*tilesize))/2),row_index*tilesize,tilesize-1,tilesize-1))
                    color = 'white'
                    pos = row_index,col_index
                    self.rectlist.append((rect,color,pos))
                if col == 1:
                    rect = pygame.Rect((col_index*tilesize+((widht-(len(self.grid[1])*tilesize))/2),row_index*tilesize,tilesize-1,tilesize-1))
                    color = 'purple'
                    pos = row_index,col_index
                    self.rectlist.append((rect,color,pos))
                if col == 2:
                    rect = pygame.Rect((col_index*tilesize+((widht-(len(self.grid[1])*tilesize))/2),row_index*tilesize,tilesize-1,tilesize-1))
                    color = 'pink'
                    pos = row_index,col_index
                    self.rectlist.append((rect,color,pos))
                if col == 3:
                    rect = pygame.Rect((col_index*tilesize+((widht-(len(self.grid[1])*tilesize))/2),row_index*tilesize,tilesize-1,tilesize-1))
                    color = 'blue'
                    pos = row_index,col_index
                    self.rectlist.append((rect,color,pos))
                if col == 4:
                    rect = pygame.Rect((col_index*tilesize+((widht-(len(self.grid[1])*tilesize))/2),row_index*tilesize,tilesize-1,tilesize-1))
                    color = 'green'
                    pos = row_index,col_index
                    self.rectlist.append((rect,color,pos))
                if col == 5:
                    rect = pygame.Rect((col_index*tilesize+((widht-(len(self.grid[1])*tilesize))/2),row_index*tilesize,tilesize-1,tilesize-1))
                    color = 'red'
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
            if color == 'purple':
                self.grid[row_index][col_index] = 1
            if color == 'pink':
                self.grid[row_index][col_index] = 2
            if color == 'blue':
                self.grid[row_index][col_index] = 3

    def astar(self):
        try:
            search = True
            rect,color,posstart = self.startrect
            rect,color,posend = self.endrect

            endnode = posend
            startnode = posstart
            current =  None
            opennodes = []
            closenodes = []
            opennodes.append((startnode,math.dist(startnode,endnode)))
            while search:
                sleep(1) 
                self.createrectgrid()
                self.drawgrid()
                pygame.display.flip()
                current = min(opennodes, key= lambda t: t[1])
                closenodes.append(current)
                opennodes.remove(current)
                
                print(f'{current[0]}------{endnode}')
                
                if current[0] == endnode:
                    print('done')
                    return
                x,y = current[0]
                for i in range(-1,2,1):
                    for j in range(-1,2,1):
                        try:
                            if self.grid[x+i][y+j] != 0:
                                pass
                            else:
                                f_cost = math.dist((x+i,y+j),startnode)+math.dist((x+i,y+j),endnode)
                                opennodes.append(((x+i,y+j),f_cost))
                        except:
                            pass




                for nodes in opennodes:
                    pos,f_cost = nodes
                    x,y = pos
                    if pos == startnode or pos == endnode:
                        pass
                    else:
                        self.grid[x][y] = 4
                for nodes in closenodes:
                    pos,f_cost = nodes
                    x,y = pos
                    if pos == startnode or pos == endnode:
                        pass
                    else:
                        self.grid[x][y] = 5
        except:
            pass
        
        
            




if __name__ == "__main__":
    gui = GUI()
    gui.run()