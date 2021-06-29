import tkinter as tk
from tkinter import *

win = tk.Tk()

win.title("First GUI")
win.geometry("700x500")
label1 = Label(win, text="LOGIN PAGE", fg="blue", font=('Arial', 25))
label1.pack()
User = Label(win, text="USERNAME: ", fg="red", font=('Arial', 10))
User.place(x=190, y=170)
Pass = Label(win, text="PASSWORD: ", fg="red", font=('Arial', 10))
Pass.place(x=190, y=220)

win.mainloop()