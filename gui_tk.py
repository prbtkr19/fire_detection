# import sys
# import os
# from tkinter import *

# window=Tk()

# window.title("FDS")
# window.geometry('1280x680')


# def run():
#     os.system('python3 yolo.py --play_video True --video_path videos/fire1.mp4')


# label = Label(window, text = 'Juke-Box', fg = 'light green',
#                   bg = 'black', font = (None, 30), height = 2)
# label.pack(side = TOP)

# btn = Button(window, text="Click to start detection", bg="red", fg="white",command=run)
# btn.grid(column=0, row=0)
# btn.place(relx=0.5, rely=0.5, anchor=CENTER)

# window.mainloop()

from tkinter import *
from tkinter import messagebox as box
import os
from PIL import Image, ImageTk
def run():
	os.system('python3 yolo.py --play_video True --video_path videos/fire1.mp4')

def Close():
    window.destroy()

# <------------------------------------------------------------------------------>
#def main_menu():
window = Tk()
window.title('FDS')
window.geometry('1200x640')
window.configure(background ="black")
photo = PhotoImage(file="image2_resize.png")

gui_label = Label(window, text = 'FIRE DETECTION SYSTEM', fg = 'red',bg='black'
                    ,font = (None, 30), height = 2)
gui_label.pack(side = TOP)
gridFrame = Frame(window, bg = 'black') # New frame to store buttons

 # <-----------------------------------------------------------------------------------> 

fire = Button(gridFrame, text = 'Start FireDetection',font= (None,20), width = 25, height = 2, command=run,foreground="red")
fire.grid(row=0, column=0, pady = 75, padx = 25, sticky=N) 

log = Button(gridFrame, text = 'logout',font= (None,20), width = 25, height = 2,foreground="red",command=Close)
log.grid(row=1, column=0, pady = 35, padx = 25, sticky=W)

    # Smiths = Button(gridFrame, text = 'The Smiths', width = 25, height = 2)
    # Smiths.grid(row=2, column=0, pady = 10, padx = 25, sticky =N)

    # Wedding = Button(gridFrame, text = 'The Wedding Pressent', width = 25, height = 2)
    # Wedding.grid(row=3, column=0, pady = 10, padx = 25, sticky =N)

    # Blondie = Button(gridFrame, text = 'Blondie', width = 25, height = 2)
    # Blondie.grid(row=4, column=0, pady = 10, padx = 25, sticky =W)

    # Clash = Button(gridFrame, text = 'Clash', width = 25, height = 2)
    # Clash.grid(row=5, column=0, pady = 10, padx = 25, sticky =W)

    # Madness = Button(gridFrame, text = 'Madness', width = 25, height = 2)
    # Madness.grid(row=0, column=1, pady = 10, padx = 25, sticky =N)

    # Pistols = Button(gridFrame, text = 'The Sex Pistols', width = 25, height = 2)
    # Pistols.grid(row=1, column=1, pady = 10, padx = 25, sticky =N)

gridFrame.pack(side=BOTTOM) 
    # Place it a the bottom or top or wherever you want it to go

window.mainloop()

#main_menu()