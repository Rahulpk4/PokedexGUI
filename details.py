from tkinter import *
import PIL.Image, PIL.ImageTk
import urllib3
from io import BytesIO
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from moves import *


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
        self.profile_frame.place(x=20,y=100,width=500,height=480)
        self.frame1_header = Label(self.profile_frame, text="Pokemon Details", bg="#F3F1F1", fg="black", font=("Arial", 15, 'bold'))
        self.frame1_header.pack(padx=10, pady=10)

        http = urllib3.PoolManager()
        response = http.request('GET', self.pokemon.sprites.front.get('default'))
        image = PIL.Image.open(BytesIO(response.data))
        img = PIL.ImageTk.PhotoImage(image)
        self.pokemon_image = Label(self.profile_frame, image=img)
        self.pokemon_image.image=img
        self.pokemon_image.pack(padx=10,pady=10)

        self.dex_lbl = Label(self.profile_frame, text='DEX NO: {}'.format(pokemon.dex), font=("Arial", 10, 'bold'))
        self.dex_lbl.pack(padx=5, pady=5)
        self.name_lbl = Label(self.profile_frame, text="NAME: "+(pokemon.name).upper(), font=("Arial", 10, 'bold'))
        self.name_lbl.pack(padx=5, pady=5)
        self.height_lbl = Label(self.profile_frame, text="HEIGHT: {}".format(pokemon.height), font=("Arial", 10, 'bold'))
        self.height_lbl.pack(padx=5, pady=5)
        self.weight_lbl = Label(self.profile_frame, text="WEIGHT: {}".format(pokemon.weight), font=("Arial", 10, 'bold'))
        self.weight_lbl.pack(padx=5, pady=5)
        self.base_exp_lbl = Label(self.profile_frame, text="BASE EXP: {}".format(pokemon.base_experience), font=("Arial", 10, 'bold'))
        self.base_exp_lbl.pack(padx=5, pady=5)
        self.type_lbl = Label(self.profile_frame, text="TYPES: "+('/'.join([type for type in pokemon.types])).upper(), font=("Arial", 10, 'bold'))
        self.type_lbl.pack(padx=5, pady=5)
        self.ability_lbl = Label(self.profile_frame, text="ABILITIES: "+('/'.join([ability[0] for ability in pokemon.abilities])).upper(), font=("Arial", 10, 'bold'))
        self.ability_lbl.pack(padx=5, pady=5)

        self.game = StringVar()
        self.game_chosen = ttk.Combobox(self.profile_frame,width=27,textvariable=self.game)
        self.game_chosen['values'] = ['red-blue', 'yellow', 'gold-silver',
                                 'crystal', 'ruby-sapphire', 'emerald',
                                 'diamond-pearl', 'platinum', 'heart-gold-soul-silver',
                                 'black-white', 'black-2-white-2', 'x-y', 'omega-ruby-alpha-sapphire'
                                 'sun-moon', 'ultra-sun-ultra-moon','sword-shield']

        self.game_chosen.current(3)
        self.game_chosen.pack(padx=5,pady=5)
        self.moves_btn = Button(self.profile_frame, text="MOVES", font=("Arial", 10, 'bold'), command=self.moves)
        self.moves_btn.pack(padx=5, pady=5)


        #Pokemon Stats Screen
        self.stats_frame = Frame(self.root, bg="#F3F1F1", bd=3, relief=RIDGE)
        self.stats_frame.place(x=550,y=100,width=600,height=480)
        self.frame2_header = Label(self.stats_frame, text="Pokemon Stats", bg="#F3F1F1", fg="black", font=("Arial", 10, 'bold'))
        self.frame2_header.pack(padx=10, pady=10)
        stats = np.array(self.pokemon.base_stats)
        labs = ['HP','ATK','DEF','SPATK','SPDEF','SPD']

        fig = Figure(figsize=(40,40), dpi=90)
        a = fig.add_subplot(111)
        a.bar(labs,stats,width=0.4)
        a.set_title("Base Stat Distribution")
        a.set_xlabel("Attributes")
        a.set_ylabel("Stat Points")

        canvas = FigureCanvasTkAgg(fig,master=self.stats_frame)
        canvas.draw()

        canvas.get_tk_widget().pack(padx=40, pady=10)


    def moves(self):
        top = Toplevel()
        obj = moves(top,self.pokemon,self.game.get())