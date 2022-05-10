import tkinter as tk
from tkinter import ttk
from EditorPane.Editor import Editor
from FileNaviator import FileNavigator
from MenuBar import MenuBar


# The main window, holds everything really
class HubWindow(tk.Tk):

    # Initializer
    def __init__(self):
        super().__init__()
        self.title("TkEditor")
        self.geometry('800x600')
        try:
            self.iconbitmap("TkEditor-logo0.1.ico")
        except:
            pass
            # do nothing just default image then

        self.bind("<Configure>", self.conf)

        self._menu_bar = MenuBar(self)
        self.tab_system = ttk.Notebook(self)
        self.tab_system.pack(expand=True, fill='both')

        self.add_editor_tab(name="Welcome!", file_content="enter code here!")  # so it starts with an open tab?
        self.add_directory_tab()

    def start_mainloop(self):
        self.mainloop()

    def add_directory_tab(self):
        self.tab_system.add( FileNavigator(self, "."), text='directory')

    def add_editor_tab(self, name="New Tab", file_content="", file_path=""):
        self.tab_system.add(Editor(file_content, file_path), text=name)

    def conf(self, event):
        self.tab_system.config(height=self.winfo_height(), width=self.winfo_width() - 145)

    def get_current_editor(self):
        return self.tab_system.nametowidget(self.tab_system.select())

    def rename_current_editor(self, new_name):
        self.tab_system.tab("current", text=[new_name])

    def get_all_open_editors(self):
        tabs = [self.tab_system.nametowidget(i) for i in self.tab_system.tabs()]
        return tabs
