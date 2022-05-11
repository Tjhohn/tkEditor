import tkinter as tk
from tkinter import ttk

from EditorPane.Editor import Editor
from FileNaviator import FileNavigator


def conf(event):
    tab_system.config(height=root.winfo_height(), width=root.winfo_width() - 145)


if __name__ == '__main__':
    root = tk.Tk()
    root.bind("<Configure>", conf)

    paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
    directory_viewer = FileNavigator(root, ".")
    tab_system = ttk.Notebook(root)
    menu_bar = tk.Menu(root)
    paned_window.add(directory_viewer)
    paned_window.add(tab_system, weight=3)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='New File')
    file_menu.add_command(label='Open')
    file_menu.add_command(label='Save')
    file_menu.add_command(label='Save All')
    file_menu.add_command(label='Save As')
    file_menu.add_command(label='Exit')
    menu_bar.add_cascade(label="File", menu=file_menu)

    tab_system.add(Editor(), text="filller")
    tab_system.add(Editor(), text="filller")
    tab_system.add(Editor(), text="filller")
    tab_system.add(Editor(), text="filller")
    tab_system.add(Editor(), text="filller")
    tab_system.add(Editor(), text="filller")

    root.config(menu=menu_bar)
    paned_window.pack()

    root.mainloop()
