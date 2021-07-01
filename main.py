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
    registration.geometry("500x600")
    registration.resizable(False,False)
    registration.title("Registration")

    Header = Label(registration, text="Registration", fg="#3B247D", font=('Impact', 25, 'bold')).pack()
    user = Label(registration, text="User name: ", fg="#3B247D", font=('Goudy old style', 15)).place(x=50, y=100)
    emailid = Label(registration, text="Email ID: ", fg="#3B247D", font=('Goudy old style', 15)).place(x=50, y=150)
    password = Label(registration, text="Password: ", fg="#3B247D", font=('Goudy old style', 15)).place(x=50, y=200)
    cpassword = Label(registration, text="Confirm Password: ", fg="#3B247D", font=('Goudy old style', 15)).place(x=50, y=250)
    sex = Label(registration, text="Sex: ", fg="#3B247D", font=('Goudy old style', 15)).place(x=50, y=300)

    user_Ent = Entry(registration, width=30, bd=3).place(x=250, y=100)
    emailid_Ent = Entry(registration, width=30, bd=3).place(x=250, y=150)
    password_Ent = Entry(registration, show='*', width=30, bd=3).place(x=250, y=200)
    cpassword_Ent = Entry(registration, show='*', width=30, bd=3).place(x=250, y=250)

    var = IntVar()

    radio1 = Radiobutton(registration, text="Male ", variable=var, value=0, command=lambda:print(var.get())).place(x=250, y=300)
    radio2 = Radiobutton(registration, text="Female ", variable=var, value=1, command=lambda:print(var.get())).place(x=300, y=300)
    radio3 = Radiobutton(registration, text="Other ", variable=var, value=2, command=lambda:print(var.get())).place(x=370, y=300)

    submit = Button(registration, text="Submit", bg='#3B247D', fg='white', font=('Impact', 15), bd=3, width=17)
    submit.place(x=50, y=400)

    cancel = Button(registration, text="Cancel", bg='#3B247D', fg='white', font=('Impact', 15), bd=3, width=17)
    cancel.place(x=270, y=400)


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

btn3 = Button(win, text="First Time? Click here to Register", fg='red', bd=0, font=('Times New Roman', 10), width=45, command=openregistration)
btn3.place(x=190, y=350)

win.mainloop()