from tkinter import *
import tkinter.font as tkfont
from PIL import ImageTk, Image
import os


class Start(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        path = "../Assets/purplelight.jpeg"
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(self.controller.dirname, path)))

        background_label = Label(self, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        my_font = tkfont.Font(family="Times New Roman", size=20, weight="bold", )  # slant="italic"

        text = Label(self, text='Play as', bg='black', fg='white')

        text.configure(font=my_font)

        text.place(relx=0.5, rely=0.3, anchor=CENTER)

        btn_start = Button(self, text='Male', bg='black', fg='white',
                           command=lambda: self.controller.show_frame('Home'))
        btn_start.place(relx=0.5, rely=0.5, width=150, height=50, anchor=CENTER)

        btn_start = Button(self, text='Female', bg='black', fg='white',
                           command=lambda: self.controller.show_frame('Home'))
        btn_start.place(relx=0.5, rely=0.4, width=150, height=50, anchor=CENTER)

        btn_start = Button(self, text="Go Back", bg='black', fg='white',
                           command=lambda: self.controller.show_frame('Home'))
        btn_start.place(relx=0.5, rely=0.6, width=150, height=50, anchor=CENTER)
