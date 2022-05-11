import tkinter as tk
from tkinter import ttk

from EditorPane.Editor import Editor
from FileNaviator import FileNavigator


def conf(event):
    tab_system.config(height=root.winfo_height(), width=root.winfo_width() - 145)


if __name__ == '__main__':
    root = tk.Tk()
    root.bind("<Configure>", conf)
    menu_bar = tk.Menu(root)
    paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
    directory_viewer = FileNavigator(root, ".")
    tab_system = ttk.Notebook(root)
    paned_window.add(directory_viewer)
    paned_window.add(tab_system, weight=3)

    tab_system.add(Editor(), text="filller")
    tab_system.add(Editor(), text="filller")
    tab_system.add(Editor(), text="filller")
    tab_system.add(Editor(), text="filller")
    tab_system.add(Editor(), text="filller")
    tab_system.add(Editor(), text="filller")

    paned_window.pack()

    root.mainloop()
