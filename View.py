
import pygame
import numpy as np

class View:
        def __init__(self ,rows , colums,width,height):

                self.xSize = width/rows
                self.ySize = height/colums  
        def updateBoard(self, x, y,status,screen): #Change the state of the board to the new one
                BG_COLOR = (10,10,10) 
                LIVE_COLOR = (255,255,255)
                DEAD_COLOR = (128,128,128)

                poly = [(x*self.xSize,y*self.ySize),
                        ((x+1)*self.xSize,y*self.ySize),
                        ((x+1)*self.xSize,(y+1)*self.ySize),
                        (x*self.xSize,(y+1)*self.ySize)]

                if status == 1:
                    pygame.draw.polygon(screen,LIVE_COLOR,poly,0)
                else:
                    pygame.draw.polygon(screen,DEAD_COLOR,poly,1)
        def cleanScreen(self,screen):
                BG_COLOR = (10,10,10) 
                screen.fill(BG_COLOR) 

