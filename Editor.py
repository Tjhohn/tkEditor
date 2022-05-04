from tkinter import Text
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
        label.pack() #grid(column=1,row=1)

        #button
        close_button = Button(self, text="close", command=self.close_tab)
        close_button.pack() #.grid(column=0, row=2)

        # defining text editor
        text_editor = Text(self)
        text_editor.pack(expand=True, fill='both') #grid(column=1,row=3,padx=20,pady=20)
