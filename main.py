import tkinter as tk

from InterLayer import InterLayer
from config import *
from GUI import GUI

def main():
    il = InterLayer()
    gui = GUI(il)
    root = gui.init_main_screen()



    tk.mainloop()




if __name__ == '__main__':
    main()


