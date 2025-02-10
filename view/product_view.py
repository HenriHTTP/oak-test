from tkinter import *

run = Tk()

class ApplicationView():
    def __init__(self) -> None:
        self.__run =  run
        self.__screen()
        run.mainloop()

    def __screen (self):
        self.__run.title("storage product")
        self.__run.configure(background="red")
        self.__run.geometry("800x600")
        self.__run.resizable(False,False)



ApplicationView()
