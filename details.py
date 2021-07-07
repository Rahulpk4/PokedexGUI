from tkinter import *


class details:
    def __init__(self, top):
        self.root = top
        self.root.geometry("700x500")
        self.root.title("Pokemon Details")
        self.root.resizable(False,False)
        self.root.iconbitmap("images/Pokemon.ico")
