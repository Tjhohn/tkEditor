# tkEditor
A simple text editor made using python for fun and learning. 
It is made using Python an Tkinter in hopes that it can be easily cross-platform as long as the platform supports python.

### Current features
- Open files into a new editor window
- Can save the file in current editor window
- Can save as for current editor tab as well
- Can create a file with editor
- Can delete a file with editor
- Can have multiple editor window tabs open
- Editor has line numbers
- Save all option for all open editors
- Ability to set file-endings for c, cpp, etc.
- Directory tree viewer 

### Planned Features
- Syntax highlighting
- Create directories not through file creation window
- Hot-key shortcuts
- Settings options for font-style, size, and colors
- Add way to see where cursor is located in editor window
- Ability to run code (at least python)

### Possible Feature
- Set up open with
- Set up some form of themes or cutomization
- Possibly create .sln/.idea like file for projects
- Some form of auto-complete
- Save user settings in file
- Right-click menu (cut, paste, copy, delete, etc.)
- Undo/Redo (unlikely, but never know)

***

## Build Environment
Cloning the project should be all you need, as it currently uses only standard python libs 

## Distribution/Executable
dist folder holds an up to-date version of the project for windows, if on linux or OSX you will need to build for your self.
You will need to install : pyinstaller using pip or similar, then run the command that is in main.

## Discussion on Syntax Highlighting
The joys of engineering are trade-offs, and for the syntax highlighting there are plenty of trade-offs.
I could roll my own and handle making my own tags for the Tk text widget. I could use the IDLE syntax highlighting.
I could also use the Pygment library using pip, but as my aim is to use only standard python libs, 
I believe this method is the least likely. 
