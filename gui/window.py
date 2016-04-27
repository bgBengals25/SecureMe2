from tkinter import *

class InitGUI():

    def __init__(self):
        self.build()

    def build(self):
        self.root = Tk()
        self.root.geometry("800x600+200+100")
        self.root.title("SecureMe 2.0 - DEV VERSION")
        self.root.resizable(width=False, height=False)
        
        self.root.mainloop()