import pygame,sys
from config import *




class GUI():
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((widht,height))
        self.clock = pygame.time.Clock()
        self.rectlist = []
        pygame.display.set_caption('Pathfinder')
        self.creategrid()

    def creategrid(self):
        for row_index in range(0,int(height/tilesize)-10,1):
            for col_index in range(0,int(widht/tilesize),1):
                color = 'white'
                rect = pygame.Rect(col_index*tilesize,row_index*tilesize,tilesize-1,tilesize-1)
                self.rectlist.append((rect,color))

    def drawgrid(self):
        for rect,color in self.rectlist:
            pygame.draw.rect(self.screen,color,rect)
    
    def run(self):
        while True:
            self.clock.tick(fps)
            pygame.display.update()
            
            self.drawgrid()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    mouseposition = pygame.mouse.get_pos()
                    for object, (rect,color) in enumerate(self.rectlist):
                        if rect.collidepoint(mouseposition):
                            self.rectlist[object] = (rect,'blue')
            

    

if __name__ is "__main__":
    gui = GUI()
    gui.run()