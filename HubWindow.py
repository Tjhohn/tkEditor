import tkinter as tk
from MenuBar import MenuBar
from PaneWindow import PaneWindow


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

        self.paned_window = PaneWindow()
        self.menu_bar = MenuBar(self, self.paned_window)

        self.paned_window.pack(expand=True, fill='both')
        self.mainloop()

