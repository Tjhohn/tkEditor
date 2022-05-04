from tkinter import Menu


class MenuBar(Menu):

    # Initializer
    def __init__(self, master):
        super().__init__()
        self._master = master

        self.add_tab_cascade()
        self._master.config(menu = self)

    def add_option_cascade(self, cascade):
        self.add_cascade(label=cascade.name, menu=cascade)

    def add_tab_cascade(self):
        tab_menu = Menu(self, tearoff=0)
        tab_menu.add_command(label='Add Tab', command=self.add_new_tab)
        self.add_cascade(label="Tab", menu=tab_menu)

        # file_menu = Menu(menu_bar, tearoff=0)

    def add_new_tab(self):
        self._master.add_tab()
