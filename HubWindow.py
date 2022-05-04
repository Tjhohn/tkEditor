import tkinter
from tkinter import ttk

from Editor import Editor
from MenuBar import MenuBar


class HubWindow(tkinter.Tk):

    # Initializer
    def __init__(self):
        super().__init__()
        self.title("TkEditor")
        self.geometry('800x600')
        self.iconbitmap("TkEditor-logo0.1.ico")
        self.bind("<Configure>", self.conf)

        self._menu_bar = MenuBar(self)
        self.tab_system = ttk.Notebook(self)
        self.tab_system.pack(expand=True, fill='both')

        self.add_tab()# so it starts with an open tab?

    def start_mainloop(self):
        self.mainloop()

    def add_tab(self):
        self.tab_system.add( Editor(self.tab_system), text='First Tab')

    def conf(self, event):
        self.tab_system.config(height=self.winfo_height(), width=self.winfo_width() - 145)


