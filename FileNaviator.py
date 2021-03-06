import tkinter as tk
from tkinter import ttk
import os

from FileHandler import FileHandler


class FileNavigator(ttk.Frame):
    """
            -----DESCRIPTION-----
    A Treeview that shows all contents of a directory.
            -----USAGE-----
    filenavigator = FileNavigator(parent, directory=[string])
    filenavigator.pack()
            -----PARAMETERS-----
    parent         = The parent of the widget.
    directory      = The directory to show.
            -----CONTENTS-----
    ---VARIABLES---
    parent         = The parent of the widget.
    _directory     = The directory to show.
    images         = A dictionary of images to use.
    selected       = The selected item in the Treeview.
    ---TKINTER VARIABLES---
    None
    ---WIDGETS---
    self
    _tree          = The Treeview widget.
    ---FUNCTIONS---
    _select()      = Sets the selected item
    _open_event()  =
    _close_event() =
    set_directory()= Sets the directory to a new one
    refresh()      = Refreshes the Treeview.
    """

    def __init__(self, parent, directory, *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent
        self._directory = directory
        self._file_handler = FileHandler(parent)

        self.images = {"Directory": tk.PhotoImage(),
                       "File": tk.PhotoImage()}

        self.selected = None

        self._tree = ttk.Treeview(self, show="tree")
        self._tree.pack(fill="both", expand=True)

        self._tree.bind("<<TreeviewSelect>>", self._select, "+")
        self._tree.bind("<Double-1>", self._double_click)
        self._tree.bind("<<TreeviewOpen>>", self._open_event, "+")
        self._tree.bind("<<TreeviewClose>>", self._close_event, "+")

        self.refresh()

    def _select(self, event=None):
        self.selected = self._tree.item(self._tree.focus())
        print('selected: ', self.selected)

    def _open_event(self, event=None):
        self._select()
        self.event_generate("<<{}Open>>".format(self._tree.item(self._tree.focus())["tags"][0]))

    def _close_event(self, event=None):
        self._select()
        self.event_generate("<<{}Close>>".format(self._tree.item(self._tree.focus())["tags"][0]))

    def _double_click(self, event=None):
        self.parent.add_editor_tab(name=self.selected['tags'][2], file_path=self.selected['tags'][2],
                                   file_content=self._file_handler.get_file_contents(self.selected['tags'][2]))
        print('double clicked selected: ', self.selected['tags'])

    def set_directory(self, new_directory):
        self._directory = new_directory

    def refresh(self):
        self._tree.delete(*self._tree.get_children())

        self._tree.insert(parent="",
                          index="end",
                          iid=self._directory,
                          text=self._directory,
                          image=self.images["Directory"],
                          tags=("Directory", "root", self._directory))

        for root, directories, files in os.walk(self._directory, topdown=True):
            # print("Root: {}".format(root))

            for name in directories:
                # print("Directory: {}".format(name))

                self._tree.insert(parent=root,
                                  index="end",
                                  iid=os.path.join(root, name),
                                  text=name,
                                  image=self.images["Directory"],
                                  tags=("Directory", "\\", os.path.join(root, name)))

            for name in files:
                # print("File: {}".format(name))
                extension = os.path.splitext(name)[1]

                self._tree.insert(parent=root,
                                  index="end",
                                  iid=os.path.join(root, name),
                                  text=name,
                                  image=self.images.get(extension) if self.images.get(extension) else self.images[
                                      "File"],
                                  tags=("File", extension, os.path.join(root, name)))

