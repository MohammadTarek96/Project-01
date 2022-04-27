from tkinter import *
from PIL import ImageTk, Image
import os


class Donate(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        path = "../Assets/purplelight.jpeg"
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(self.controller.dirname, path)))

        background_label = Label(self, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        text = Label(self, text="we thank you for playing our game there are a lot of homless people", bg='black',
                     fg='white')
        text2 = Label(self, text="who have to go through the struglles you experinced in the game in real life.",
                      bg='black', fg='white')
        text3 = Label(self, text="Please help them by donating to National Alliance to End Homelessness", bg='black',
                      fg='white')
        text.place(x=20, y=80)
        text.config(font=('Sail bold',20))
        text2.place(x=30, y=120)
        text2.config(font=('Sail bold',20))
        text3.place(x=40, y=160)
        text3.config(font=('Sail bold',20))

        btn_about = Button(self, text="Go Back", bg='black', fg='white',
                           command=lambda: self.controller.show_frame('Home'))
        btn_about.place(width=150, height=50, x=250,y=400)
