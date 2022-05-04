from tkinter import Text
from tkinter.constants import LEFT
from tkinter.ttk import Label, Frame, Button

from LineNumberText import LineNumbers


class Editor(Frame):

    # Initializer
    def __init__(self, tab_group):
        super().__init__()
        self._tab_group = tab_group

        self.create_page()

    def close_tab(self):
        self.destroy()

    def create_page(self):
        #button
        close_button = Button(self, text="close", command=self.close_tab)
        close_button.pack(side=LEFT)



        # defining text editor
        text_editor = Text(self)
        line_numbers = LineNumbers(self, text_editor, width=1)
        line_numbers.pack(fill='both', side=LEFT)
        text_editor.pack(expand=1, fill='both', side=LEFT) #grid(column=1,row=3,padx=20,pady=20)
