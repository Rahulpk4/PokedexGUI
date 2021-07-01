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


class Registration:
    def openregistration(self):
        self.registration = Toplevel(win)
        self.registration.geometry("500x600")
        self.registration.resizable(False,False)
        self.registration.title("Registration")

        self.Header = Label(self.registration, text="Registration", fg="#3B247D", font=('Impact', 25, 'bold')).pack()
        self.user = Label(self.registration, text="User name: ", fg="#3B247D", font=('Goudy old style', 15)).place(x=50, y=100)
        self.emailid = Label(self.registration, text="Email ID: ", fg="#3B247D", font=('Goudy old style', 15)).place(x=50, y=150)
        self.password = Label(self.registration, text="Password: ", fg="#3B247D", font=('Goudy old style', 15)).place(x=50, y=200)
        self.cpassword = Label(self.registration, text="Confirm Password: ", fg="#3B247D", font=('Goudy old style', 15)).place(x=50, y=250)
        self.sex = Label(self.registration, text="Sex: ", fg="#3B247D", font=('Goudy old style', 15)).place(x=50, y=300)

        self.varuser = StringVar()
        self.user_Ent = Entry(self.registration, width=30, bd=3, bg='lightgray', textvariable=self.varuser).place(x=250, y=100)

        self.varemail = StringVar()
        self.emailid_Ent = Entry(self.registration, width=30, bd=3, bg='lightgray', textvariable=self.varemail).place(x=250, y=150)

        self.varpass = StringVar()
        self.password_Ent = Entry(self.registration, show='*', width=30, bd=3, bg='lightgray', textvariable=self.varpass).place(x=250, y=200)

        self.varcpass = StringVar()
        self.cpassword_Ent = Entry(self.registration, show='*', width=30, bd=3, bg='lightgray', textvariable=self.varcpass).place(x=250, y=250)

        self.var = IntVar()

        self.radio1 = Radiobutton(self.registration, text="Male ", variable=self.var, value=0).place(x=250, y=300)
        self.radio2 = Radiobutton(self.registration, text="Female ", variable=self.var, value=1).place(x=300, y=300)
        self.radio3 = Radiobutton(self.registration, text="Other ", variable=self.var, value=2).place(x=370, y=300)

        self.submit = Button(self.registration, text="Submit", bg='#3B247D', fg='white', font=('Impact', 15), bd=3, width=17, command=self.reg_submit)
        self.submit.place(x=50, y=400)

        self.cancel = Button(self.registration, text="Cancel", bg='#3B247D', fg='white', font=('Impact', 15), bd=3, width=17)
        self.cancel.place(x=270, y=400)


    def reg_submit(self):
        print(self.varuser.get())
        print(self.varemail.get())
        print(self.varpass.get())
        print(self.varcpass.get())
        print(self.var.get())

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

obj = Registration()

btn3 = Button(win, text="First Time? Click here to Register", fg='red', bd=0, font=('Times New Roman', 10), width=45, command=obj.openregistration)
btn3.place(x=190, y=350)

win.mainloop()