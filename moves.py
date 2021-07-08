from tkinter import *
from tkinter import ttk

class moves:
    def __init__(self, top, pokemon, game):
        self.root = top
        self.root.geometry("800x500")
        self.root.title("Pokemon Moves")
        self.root.resizable(False,False)
        self.root.iconbitmap("images/Pokemon.ico")
        self.root.focus_force()
        self.pokemon = pokemon

        self.details_header = Label(self.root, text="Pokemon Moves",bg="#5B111D",fg="white",font=("Impact", 30, "bold"))
        self.details_header.pack(fill=X, padx=10, pady=10)

        self.M_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.M_Frame.place(x=10,y=100,width=740,height=370)

        print (pokemon.moves)

        moves = [[x for x in item]for item in self.pokemon.moves[game]]

        scrollx = Scrollbar(self.M_Frame, orient=HORIZONTAL)
        scrolly = Scrollbar(self.M_Frame, orient=VERTICAL)
        self.MovesTable = ttk.Treeview(self.M_Frame,columns=("Name","LearnMethod","Level"), xscrollcommand= scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.MovesTable.xview)
        scrolly.config(command=self.MovesTable.yview)

        self.MovesTable.heading("Name", text="Name")
        self.MovesTable.heading("LearnMethod", text="LearnMethod")
        self.MovesTable.heading("Level", text="Level")

        self.MovesTable["show"] = "headings"

        self.MovesTable.column("Name")
        self.MovesTable.column("LearnMethod")
        self.MovesTable.column("Level")

        for move in moves:
            self.MovesTable.insert("","end",values=move)

        self.MovesTable.pack(fill=BOTH, expand=1, padx=10, pady=10)
