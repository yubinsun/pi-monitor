import tkinter as tk
from config import *


class GUI:
    elements = {}
    # If the introductory message is still in the box
    input_text_inited = False
    output_text_inited = False

    def __init__(self):
        pass

    def init_main_screen(self):
        # main Window
        root = tk.Tk()
        root.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
        root.grid()

        #
        # Text boxes / Output Area
        text_frame = tk.Frame(root, height=300, bg='green')
        text_frame.pack(side=tk.TOP, expand=True, fill='both')
        self.elements['text_frame'] = text_frame
        # Put a text box
        display_text_box = tk.Text(text_frame, font=('Courier', 16, 'italic'), width=32, height=3)
        display_text_box.pack(expand=True, fill='both')
        display_text_box.insert('1.0', 'Output will shown here')
        self.elements['display_text_box'] = display_text_box

        #
        # Control Sections/ Input Area
        control_frame = tk.Frame(root, height=30, bg='grey', bd=3)
        control_frame.pack(side=tk.LEFT, expand=True, fill='both')
        self.elements['control_frame'] = control_frame
        # Enter button
        b_enter = tk.Button(control_frame, text='Enter', bg='white', bd=3,
                         command=lambda: self.button_enter()
                         )
        b_enter.pack(side=tk.RIGHT, expand=False, fill='y')
        self.elements['b_enter'] = b_enter
        # Clear Input button
        b_clear_input = tk.Button(control_frame, text='CLR', bg='white', bd=3,
                                  command=lambda: self.button_clear_input()
                                  )
        b_clear_input.pack(side=tk.RIGHT, expand=False, fill='y')
        self.elements['b_clear_input'] = b_clear_input
        # Input text box
        input_text_box = tk.Text(control_frame, font=('Courier', 16, 'italic'), width=64, height=1)
        input_text_box.pack(side=tk.TOP, expand=False, fill='x')
        input_text_box.insert('1.0', 'Input here')
        self.elements['input_text_box'] = input_text_box
        # Number Buttons
        for i in range(0, 10):
            b = tk.Button(control_frame, text=f'{i}', bg='white', bd=3,
                          command=lambda: self.button_number(i)
                          )
            b.pack(side=tk.LEFT, expand=True, fill='both')
            self.elements[f'number_button_{i}'] = b

    # # #
    # Operations for the out Box
    # # #

    def append_output(self, text, newline=False):
        # If the intro message is still in the text box
        if not self.output_text_inited:
            self.clear_output()
            self.output_text_inited = True
        # Append new text to the end
        self.elements['display_text_box'].insert(tk.END, ('\n' if newline else '') + text)

    def clear_output(self):
        self.elements['display_text_box'].delete('1.0', 'end')

    # # #
    # Operations for the input Box
    # # #

    def append_input(self, text, newline=False):
        # If the intro message is still in the text box
        if not self.input_text_inited:
            self.clear_input()
            self.input_text_inited = True
        # append the message
        self.elements['input_text_box'].insert(tk.END, ('\n' if newline else '') + text)

    def clear_input(self):
        self.elements['input_text_box'].delete('1.0', 'end')

    # # #
    # Operations for the buttons
    # # #

    def button_clear_input_output(self):
        self.clear_output()
        # Need to append to init the input box.
        self.append_output("")

    def button_clear_input_input(self):
        self.clear_input()
        # Need to append to init the input box.
        self.append_input("")

    def button_enter(self):
        data = self.elements['input_text_box'].get('1.0', 'end')[:-1]
        self.append_output(data, newline=False)

    def button_number(self, number):
        self.append_input(str(number))
