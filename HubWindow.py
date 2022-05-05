import tkinter as tk
from tkinter import ttk
from EditorPane.Editor import Editor
from MenuBar import MenuBar


# The main window, holds everything really
class HubWindow(tk.Tk):

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

        self.add_tab(name="Welcome!", file_content="enter code here!")# so it starts with an open tab?

    def start_mainloop(self):
        self.mainloop()

    def add_tab(self, name="New Tab", file_content="", file_path = ""):
        self.tab_system.add(Editor(file_content, file_path), text=name)

    def conf(self, event):
        self.tab_system.config(height=self.winfo_height(), width=self.winfo_width() - 145)

    def get_current_editor(self):
        return self.tab_system.nametowidget(self.tab_system.select())

