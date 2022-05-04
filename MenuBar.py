from tkinter import Menu
from FileHandler import FileHandler
from sys import exit as sexit


class MenuBar(Menu):

    # Initializer
    def __init__(self, master):
        super().__init__()
        self._master = master
        self._file_handler = FileHandler(master)

        self.add_tab_cascade()
        self.add_file_cascade()
        self._master.config(menu=self)

    def add_option_cascade(self, cascade):
        self.add_cascade(label=cascade.name, menu=cascade)

    def add_tab_cascade(self):
        tab_menu = Menu(self, tearoff=0)
        tab_menu.add_command(label='Add Tab', command=self.add_new_tab)
        self.add_cascade(label="Tab", menu=tab_menu)

    def add_new_tab(self):
        self._master.add_tab()

    def add_file_cascade(self):
        file_menu = Menu(self, tearoff=0)
        #file_menu.add_command(label='New File', command=self.add_new_tab)
        file_menu.add_command(label='Open', command=self._file_handler.open_file)
        #file_menu.add_command(label='Save', command=self._master.get_current_editor)
        file_menu.add_command(label='Save As', command=self.save_file_as)
        file_menu.add_command(label='Exit', command=sexit)
        self.add_cascade(label="File", menu=file_menu)

    def save_file_as(self):
        self._file_handler.save_as(self._master.get_current_editor())
