#  hopefully will use to handle files properly, maybe like a repository patterN?
#  need to have a way to set file extension, as currently it is hard set to .py
from tkinter.filedialog import askopenfilename, asksaveasfilename
import ntpath #for getting file name easily


class FileHandler:

    # Initializer
    def __init__(self, master):
        self._master = master

    # open a few tab and fills tab with contents of the file, may only allow .py files currently?
    def open_file(self):
        file_path = askopenfilename(filetypes=[('Python Files', '*.py')])

        if file_path != '':
            with open(file_path, 'r') as file:
                code = file.read()
                self._master.add_tab(name=ntpath.basename(file_path), file_content=code, file_path=file_path)

    def save_as(self, current_tab):  # also npw all files are .py
        file_path = asksaveasfilename(filetypes=[('Python Files', '*.py')])

        if file_path != '':
            self._master.rename_current_editor(ntpath.basename(file_path))
            with open(file_path + '.py', 'w') as file:
                code = current_tab.get_text_contents()
                file.write(code)

    def save(self, current_tab):
        file_path = current_tab.get_file_path()
        if file_path == '':
            self.save_as(current_tab)
            return

        if file_path != '':
            with open(file_path + '.py', 'w') as file:
                code = current_tab.get_text_contents()
                file.write(code)
