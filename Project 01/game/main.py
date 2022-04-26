from tkinter import *
import os
from PIL import ImageTk, Image
import tkinter.font as font

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600

page = Tk()
page.title('Game - Homeless')

page.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))

path = "../Assets/purplelight.jpeg"

dirname = os.path.dirname(__file__)
img = ImageTk.PhotoImage(Image.open(os.path.join(dirname, path)))
#page.configure(background='')

background_label = Label(page, image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

myfont = font.Font(size = 12, weight="bold")

btnStart = Button(page, text="Start", bg='black', fg='white', font=myfont)
btnStart.place(relx=0.5, rely=0.3, width=150, height = 50, anchor=CENTER)
 
btnAbout = Button(page, text="About Game", bg='black', fg='white', font = myfont)
btnAbout.place(relx=0.5, rely=0.45, width=150, height = 50, anchor=CENTER)

btnDonate = Button(page, text="Donate", bg='black', fg='white', font = myfont)
btnDonate.place(relx=0.5, rely=0.6, width=150, height = 50, anchor=CENTER)

page.mainloop()

userName = Label(page, text = "Enter your first name")
userName.pack()