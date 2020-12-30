
import numpy as np
from Board import Board
from View import View
import pygame
from random import randint,randrange

class Controler:


    def boardChoose(self,state): #Choose the player selection
        
        if state==0:
            randomSize=randrange(80, 120, 10)
            board = Board(randomSize,randomSize)
            status = np.zeros((board.rows,board.columns))
            for u in range(0,board.rows):
                for j in range(0,board.columns):
                    status[u,j]=randint(0,1) 
          
  
        else:
            if state == 3:
                with open("sample_patterns\glider.txt", "r") as file: 
                    for no, line in enumerate(file):
                        nX = len(line)
                    nY = no+1

                board = Board(nX,nY)
                status = np.zeros((board.rows,board.columns)) 
                with open("sample_patterns\glider.txt", "r") as file: 
                    for no, line in enumerate(file):
                        for i, l in enumerate(line):
                            if l=="X":
                                status[i,no]=1

            elif state == 1:
                with open("sample_patterns\pulsar.txt", "r") as file: 
                    for no, line in enumerate(file):
                        nX = len(line)
                    nY = no+1

                board = Board(nX,nY)
                status = np.zeros((board.rows,board.columns)) 
                with open("sample_patterns\pulsar.txt", "r") as file: 
                    for no, line in enumerate(file):
                        for i, l in enumerate(line):
                            if l=="X":
                                status[i,no]=1
            elif state == 2:
                with open("sample_patterns\gosper-glider-gun.txt", "r") as file: 
                    for no, line in enumerate(file):
                        nX = len(line)
                    nY = no+1

                board = Board(nX,nY)
                status = np.zeros((board.rows,board.columns)) 
                with open("sample_patterns\gosper-glider-gun.txt", "r") as file: 
                    for no, line in enumerate(file):
                        for i, l in enumerate(line):
                            if l=="X":
                                status[i,no]=1
            
            elif state==5:
                raise ValueError("You have no select an option")

     
        return board,status
        

