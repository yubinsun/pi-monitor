import tkinter as tk
from config import *


def init_main_screen():
    root = tk.Tk()
    root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    root.grid()
    #
    # Text boxes
    text_frame = tk.Frame(root, height=300, bg="green")
    text_frame.pack(side=tk.TOP, expand=True, fill='both')
    # text_frame.place(x=0, y=0, anchor="nw", width=OUTPUT_WIDTH, height=OUTPUT_HEIGHT)
    display_text_box = tk.Text(text_frame, font=("Courier", 16, "italic"), width=64, height= 3)

    display_text_box.pack(expand=True, fill='both')

    display_text_box.insert('1.0', 'Sample Text output')

    #
    # Button Sections


    button_frame = tk.Frame(root, height=30, bg="grey", bd=3)
    button_frame.pack(side=tk.BOTTOM, expand=True, fill='both')

    for i in range(0, 10):
        b = tk.Button(button_frame, text=f"{i}", bg="white", bd=3)
        b.pack(side=tk.LEFT, expand=True, fill='both')

    bEnt = tk.Button(button_frame, text="Enter", bg="white", bd=3)
    bEnt.pack(side=tk.LEFT, expand=True, fill='both')


def main():
    init_main_screen()


if __name__ == '__main__':
    main()
    tk.mainloop()
