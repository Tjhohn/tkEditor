#hopefully will use to handle files properly, maybe like a repository patterN?
from tkinter.filedialog import askopenfilename, asksaveasfilename
import ntpath #for getting file name easily


class FileHandler:

    # Initializer
    def __init__(self, master):
        self._file_path = ""
        self._master = master

    # open a few tab and fills tab with contents of the file, may only allow .py files currently?
    def open_file(self):
        file_path = askopenfilename(filetypes=[('Python Files', '*.py')])
        with open(file_path, 'r') as file:
            code = file.read()
            self._master.add_tab(name=ntpath.basename(file_path), file_content=code)


    def save_as(self):
        if self._file_path == '':
            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        else:
            path = self._file_path
        with open(path, 'w') as file:
            pass
            #code = editor.get('1.0', END)
            #file.write(code)

