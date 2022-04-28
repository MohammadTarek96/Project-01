from tkinter import *
import tkinter.font as tkfont
from PIL import ImageTk, Image
import os


class About(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        path = "../Assets/purplelight.jpeg"
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(self.controller.dirname, path)))

        background_label = Label(self, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        textAboutGame = Label(self, text="we thank you for playing our game there are a lot of homless people", bg='black',
                     fg='white')
        aboutGameFont = tkfont.Font(family="Times New Roman", size=16, weight="bold" )  # slant="italic"
        textAboutGame.configure(font=aboutGameFont)
        textAboutGame.place(relx=0.5, rely=0.1, anchor=CENTER)

        btn_about = Button(self, text="Go Back", bg='black', fg='white',
                           command=lambda: self.controller.show_frame('Home'))
        btn_about.place(relx=0.5, rely=0.3, width=150, height=50, anchor=CENTER)
