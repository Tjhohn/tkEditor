from HubWindow import HubWindow
import sys

# to distribute for windows make sure you are in the directory then in cmd: pyinstaller --onefile main.py --windowed
# in the distribution dir, make sure you add the .ico!
# handle way to allow open with files probably via sys args
if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    hub_window = HubWindow()
    hub_window.start_mainloop()



