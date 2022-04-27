from tkinter import *
import os
import tkinter.font as font

from Home import Home
from About import About
from Start import Start
from Donate import Donate


class Main(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.WINDOW_WIDTH = 400
        self.WINDOW_HEIGHT = 600

        self.title('Game - Homeless')
        self.geometry(str(self.WINDOW_WIDTH) + "x" + str(self.WINDOW_HEIGHT))

        self.dirname = os.path.dirname(__file__)
        self.font = font.Font(size=12, weight="bold")

        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for frame in (Home, About, Start, Donate):
            f = frame(self.container, self)
            f.grid(row=0, column=0, sticky="nsew")
            self.frames[frame.__name__] = f

        self.show_frame('Home')
        self.mainloop()

    def show_frame(self, frame):
        self.frames[frame].tkraise()


main = Main()
