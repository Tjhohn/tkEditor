from HubWindow import HubWindow

# to distribute for windows make sure you are in the directory then in cmd: pyinstaller --onefile main.py --windowed
# in the distribution dir, make sure you add the .ico!
if __name__ == '__main__':
    hub_window = HubWindow()
    hub_window.start_mainloop()



