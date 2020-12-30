from tkinter import *

from tkinter.ttk import * 
from tkinter import messagebox


class Menu:

    def __init(self):
        self.state=5

    def startMenu(self): #Start the menu and have the logic of player selection
        window = Tk()

        window.title("Ivan Arjona Life's Game")

        window.geometry('400x400')

    
        messagebox.showinfo('Welcome to the Life Game','To start the game, select one option and then press play! \n\nYou can stop the game pressing any key \nThen you can paint new cells clicking on your mouse')

        def clicked():

            self.state=0
        def clicked1():

            self.state=1

        def clicked2():

            self.state=2

        def clicked3():

            self.state=3
            

        btn1 = Button(window, text="Random", command=clicked)
        btn2 = Button(window, text="Pulsar", command=clicked1)
        btn3 = Button(window, text="Gosper", command=clicked2)
        btn4 = Button(window, text="Glider", command=clicked3)
        btn5 = Button(window, text="Play", command=window.destroy)

        btn1.grid(column=1, row=2)
        btn2.grid(column=2, row=2)

        btn3.grid(column=3, row=2)
        btn4.grid(column=4, row=2)
        btn5.grid(column=1, row=3)


        window.mainloop()