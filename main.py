import tkinter as tk
from tkinter import *
from PIL import ImageTk

win = tk.Tk()

win.title("Login Page")
win.geometry("700x500")
win.resizable(False,False)
bg = ImageTk.PhotoImage(file="assets/login-background.jpg")
bg_image = Label(win,image=bg).place(x=0,y=0,relwidth=1,relheight=1)


def submit():
    str1 = "Hello "
    str2 = "Your Password is: "
    print(str1 + ent1.get())
    print(str2 + ent2.get())


def cancel():
    ent1.delete(0, END)
    ent2.delete(0, END)


def openregistration():
    registration = Toplevel(win)
    registration.geometry("500x700")
    registration.resizable(False,False)
    registration.title("Registration")


label1 = Label(win, text="DEDUPE APPLICATION", fg="blue", font=('Impact', 25, 'bold'))
label1.pack()
label2 = Label(win, text="LOGIN PAGE", fg="blue", font=('Impact', 20, 'bold'))
label2.pack()
User = Label(win, text="USERNAME: ", bg='white', fg="red", font=('Goudy old style', 10))
User.place(x=190, y=170)
Pass = Label(win, text="PASSWORD: ", bg='white', fg="red", font=('Goudy old style', 10))
Pass.place(x=190, y=220)

username = StringVar()
ent1 = Entry(win, width=30, bd=3)
ent1.place(x=300, y=170)

password = StringVar()
ent2 = Entry(win, show='*', width=30, bd=3)
ent2.place(x=300, y=220)

btn1 = Button(win, text="Submit", bg='#C70039', fg='white', font=('Arial', 10), bd=3, width=17, command=submit)
btn1.place(x=190, y=290)

btn2 = Button(win, text="Cancel", bg='#C70039', fg='white', font=('Arial', 10), bd=3, width=17, command=cancel)
btn2.place(x=370, y=290)

btn3 = Button(win, text="First Time? Click here to Register", fg='red', bd=0, font=('Goudy old style', 10), width=45, command=openregistration)
btn3.place(x=190, y=350)

win.mainloop()