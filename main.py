from tkinter import *
import pypokedex
import numpy as np

p = pypokedex.get(name="swampert")

print (p.moves)

for item in range(0, len(p.moves['omega-ruby'])):
    print (p.moves['omega-ruby'][item])


print(np.sum(np.array(p.base_stats)))


win = Tk()
win.geometry("500x300")
win.title("Pokedex")


# Change the label text
def show():
    label.config(text="Search "+clicked.get())


lbl_header = Label(win, text="PokeDex", font=('Impact', 25, 'bold')).pack()

# Dropdown menu options
options = ["By Dex No.","By Name"]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("By Dex No.")

# Create Dropdown menu
drop = OptionMenu(win, clicked, *options)
drop.pack(padx=10, pady=10)

# Create button, it will change label text
button = Button(win, text=">", font=("Arial", 12, 'bold'), command=show).pack()

# Trail Frame
frame = Frame(win, bd=5, bg="#D5CFD0").place(x=100, y=140, width=300, height=150)

# Create Label
label = Label(frame, text=" ", bg="#D5CFD0", font=('Arial', 12, 'bold'))
label.place(x=180, y=150)

frame_entry = Entry(frame, bd=3, width=24).place(x=180, y=200)
# Execute tkinter
win.mainloop()
