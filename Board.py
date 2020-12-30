import numpy as np

class Board:
    def __init__(self , rows , columns):
        self.rows = rows
        self.columns = columns   

    def checkNeighbors(self,posX,posY,status): #Return the number of cells alive 
        numberAlive = status[(posX-1)%self.rows,(posY-1)%self.columns] + status[(posX)%self.rows,(posY-1)%self.columns] + \
                            status[(posX+1)%self.rows,(posY-1)%self.columns] + status[(posX-1)%self.rows,(posY)%self.columns] + \
                            status[(posX+1)%self.rows,(posY)%self.columns] + status[(posX-1)%self.rows,(posY+1)%self.columns] + \
                            status[(posX)%self.rows,(posY+1)%self.columns] + status[(posX+1)%self.rows,(posY+1)%self.columns]
        return numberAlive
    def updateCell(self,state,numberAlive): #Check the rules and return the new cell state
        cellState=state
        # Rule 1: If there are 3 cells near alive, the cell revive
        if state == 0 and numberAlive==3:
            cellState = 1

        # Rule 2: If there are less than 2 or more than 4 cells alive near, it dies
        elif state == 1 and (numberAlive < 2 or numberAlive > 3):
            cellState = 0
        return cellState