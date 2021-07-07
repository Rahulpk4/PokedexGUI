from tkinter import *
import pypokedex
import numpy as np
from details import *

# p = pypokedex.get(name="swampert")
#
# print (p.moves)
#
# for item in range(0, len(p.moves['omega-ruby'])):
#     print (p.moves['omega-ruby'][item])
#
#
# print(np.sum(np.array(p.base_stats)))

class front():
    def __init__(self, win):
        self.root = win
        self.root.geometry("500x350")
        self.root.title("Pokedex")
        self.root.iconbitmap("images/Pokemon.ico")

        self.lbl_header = Label(self.root, text="PokeDex", font=('Impact', 25, 'bold')).pack()

        options = ["By Dex No.", "By Name"]

        self.clicked = StringVar()

        self.clicked.set("By Dex No.")

        self.drop = OptionMenu(self.root, self.clicked, *options)
        self.drop.pack(padx=10, pady=10)

        self.button = Button(self.root, text=">", font=("Arial", 12, 'bold'), command=self.show).pack()

        self.frame = Frame(win, bd=5, bg="#D5CFD0").place(x=100, y=140, width=300, height=150)

        self.label = Label(self.frame, text="Select an option", bg="#D5CFD0", font=('Arial', 12, 'bold'))
        self.label.place(x=180, y=150)

        self.search = StringVar()
        self.frame_entry = Entry(self.frame, bd=3, width=24, textvariable=self.search).place(x=180, y=200)

        self.submit_button = Button(self.frame, text="Submit", font=("Arial", 12, 'bold'), fg='black', command=self.submit).place(x=170, y=280)
        self.cancel_button = Button(self.frame, text="Cancel", font=("Arial", 12, 'bold'), fg='black', command=self.cancel).place(x=260, y=280)


    def show(self):
        self.label.config(text="Search "+self.clicked.get())

    def submit(self):
        top = Toplevel()
        newobj = details(top)


    def cancel(self):
        self.search.set('')



if __name__ == "__main__":
    win = Tk()
    obj = front(win)
    win.mainloop()
