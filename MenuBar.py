from tkinter import Menu
from FileHandler import FileHandler
from sys import exit as sexit


class MenuBar(Menu):

    # Initializer
    def __init__(self, root, pane):
        super().__init__()
        self._master = root
        self._pane = pane
        self._file_handler = FileHandler(pane)

        self.add_file_cascade()
        self.add_settings_cascade()
        self._master.config(menu=self)

    #  This function is for easy expansion without having to constantly change this object
    def add_option_cascade(self, name, menu):
        self.add_cascade(label=name, menu=menu)

    def add_settings_cascade(self):
        settings_menu = Menu(self, tearoff=0)
        #  add commands?
        self.add_cascade(label="Settings", menu=settings_menu)

    def add_file_cascade(self):
        file_menu = Menu(self, tearoff=0)
        file_menu.add_command(label='New File', command=self._pane.add_editor_tab)
        file_menu.add_command(label='Open', command=self._file_handler.open_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_command(label='Save All', command=self.save_all)
        file_menu.add_command(label='Save As', command=self.save_file_as)
        file_menu.add_command(label='Exit', command=sexit)
        self.add_cascade(label="File", menu=file_menu)

    def save_file_as(self):
        self._file_handler.save_as(self._pane.get_current_editor())

    def save_file(self):
        self._file_handler.save(self._pane.get_current_editor())

    def save_all(self):
        tabs = self._pane.get_all_open_editors()
        for tab in tabs:
            self._file_handler.save(tab)
