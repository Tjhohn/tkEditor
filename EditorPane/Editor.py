from EditorPane.CustomText import CustomText
from EditorPane.TextLineNumbers import TextLineNumbers
import tkinter as tk


#basic editor, has ability to close self, and add text with line numbers
class Editor(tk.Frame):
    def __init__(self, file_contents="", file_path="", *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)
        self._file_path = file_path

        # button
        close_button = tk.Button(self, text="close", command=self.close_tab)
        close_button.pack(side=tk.LEFT)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

        if file_contents == "":
            self.text.insert("end", "one\ntwo\nthree\n")
            self.text.insert("end", "four\n", ("bigfont",))
            self.text.insert("end", "five\n")
        else:
            self.text.insert("end", file_contents)

    def _on_change(self, event):
        self.linenumbers.redraw()

    def close_tab(self):
        self.destroy()

    def get_text_contents(self):
        return self.text.get('1.0', tk.END)

    def get_file_path(self):
        return self._file_path

    def set_file_path(self, new_path):
        self._file_path = new_path
