
import pygame
import numpy as np
import time
from Board import Board
from View import View
from Controler import Controler
from Menu import Menu

class Game:
    def startGame(self): 

        menu = Menu()
        menu.startMenu()
        choice=menu.state

        controler = Controler()
        board,status=controler.boardChoose(choice)

        WIDTH, HEIGHT = 600, 600 
        view = View(board.rows,board.columns,WIDTH,HEIGHT)

        pygame.init() 

        screen = pygame.display.set_mode([WIDTH,HEIGHT]) 

        BG_COLOR = (10,10,10) 


        pauseRun = False

        running = True
        while running:

            newStatus = np.copy(status) # Copy status

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    pauseRun = not pauseRun

                mouseClick = pygame.mouse.get_pressed()
                if sum(mouseClick) > 0:
                    posX, posY = pygame.mouse.get_pos()
                    x, y = int(np.floor(posX/view.xSize)), int(np.floor(posY/view.ySize))
                    newStatus[x,y] = not mouseClick[2]

            view.cleanScreen(screen)

            for x in range(0,board.rows):
                for y in range(0,board.columns):


                    if not pauseRun:
                        nNeigh = board.checkNeighbors(x,y,status)
                        newStatus[x,y] = board.updateCell(status[x,y],nNeigh)

                    view.updateBoard(x,y,newStatus[x,y],screen)

            status = np.copy(newStatus)
            time.sleep(0.1)
            pygame.display.flip()



        pygame.quit()



