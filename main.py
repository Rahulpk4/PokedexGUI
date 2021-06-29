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

ent1 = Entry(win, width=30, bd=3)
ent1.place(x=300, y=170)

ent2 = Entry(win, show='*', width=30, bd=3)
ent2.place(x=300, y=220)

btn1 = Button(win, text="Submit", bg='#C70039', fg='white', font=('Arial', 10), bd=3, width=17)
btn1.place(x=190, y=290)

btn2 = Button(win, text="Cancel", bg='#C70039', fg='white', font=('Arial', 10), bd=3, width=17)
btn2.place(x=370, y=290)

win.mainloop()