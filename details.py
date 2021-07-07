from tkinter import *


class details:
    def __init__(self, top, pokemon):
        self.root = top
        self.root.geometry("1200x600")
        self.root.title("Pokemon Details")
        self.root.resizable(False,False)
        self.root.iconbitmap("images/Pokemon.ico")
        self.root.focus_force()
        self.pokemon = pokemon
        self.details_header = Label(self.root, text="Pokemon Profile",bg="#5B111D",fg="white",font=("Impact", 30, "bold"))
        self.details_header.pack(fill=X, padx=10, pady=10)

        # Pokemon Profile Screen
        self.profile_frame = Frame(self.root, bg="#F3F1F1", bd=3, relief=RIDGE)
        self.profile_frame.place(x=20,y=100,width=500,height=450)
        self.frame1_header = Label(self.profile_frame, text="Pokemon Details", bg="#F3F1F1", fg="black", font=("Arial", 15, 'bold'))
        self.frame1_header.pack(padx=10, pady=10)

        #Pokemon Stats Screen
        self.stats_frame = Frame(self.root, bg="#F3F1F1", bd=3, relief=RIDGE)
        self.stats_frame.place(x=550,y=100,width=600,height=200)
        self.frame2_header = Label(self.stats_frame, text="Pokemon Stats", bg="#F3F1F1", fg="black", font=("Arial", 10, 'bold'))
        self.frame2_header.pack(padx=10, pady=10)

        #Pokemon Moves Screen
        self.moves_frame = Frame(self.root, bg="#F3F1F1", bd=3, relief=RIDGE)
        self.moves_frame.place(x=550, y=300, width=600, height=250)
        self.frame3_header = Label(self.moves_frame, text="Pokemon Moves", bg="#F3F1F1", fg="black", font=("Arial", 10, 'bold'))
        self.frame3_header.pack(padx=10, pady=10)