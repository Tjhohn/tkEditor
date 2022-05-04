#from tkinter import Frame
from tkinter import Text
from tkinter.constants import BOTH
from tkinter.ttk import Label, Frame, Button


class Editor(Frame):

    # Initializer
    def __init__(self, tab_group):
        super().__init__()
        self._tab_group = tab_group

        self.create_page()

    def close_tab(self):
        self.destroy()

    def create_page(self):
        label = Label(self, text="Welcome in TkEditor!")
        label.grid(column=1,
                   row=1,
                   padx=40,
                   pady=40)

        #button
        close_button = Button(self, text="close", command=self.close_tab)
        close_button.grid(column=1, row=2)

        # defining text editor
        text_editor = Text(self)
        text_editor.grid(column=1,
                   row=3,
                   padx=40,
                   pady=40)
