# %%
from tkinter import *
import random
import numpy as np


frame=Tk()
menu=Menu(frame)
file=Menu(menu)
file.add_command(label="Exit", command=frame.quit)
file.add_command(label="EASY LEVEL", command=lambda:easyLvl())
file.add_command(label="EASY LEVEL SOLVED", command=lambda:easyLvlSolved())
file.add_command(label="HARD LEVEL", command=lambda:hardLvl())
file.add_command(label="HARD LEVEL SOLVED", command=lambda:hardLvlSolved())

menu.add_cascade(label="Choose Level (Easy or Hard)", menu=file)
frame.config(menu=menu)

listofnumbers0 = np.random.default_rng().integers(1, 10, size=(81), endpoint = True)

hardUnsolved = np.random.default_rng().integers(1, 10, size=(81), endpoint = True)

hardSolved = np.random.default_rng().integers(1, 10, size=(81), endpoint = True)

easyUnsolved=[5,1,7,6,0,0,0,3,4,
               2,8,9,0,0,4,0,0,0,
               3,4,6,2,0,5,0,9,0,
               6,0,2,0,0,0,0,1,0,
               0,3,8,0,0,6,0,4,7,
               0,0,0,0,0,0,0,0,0,
               0,9,0,0,0,0,0,7,8,
               7,0,3,4,0,0,5,6,0,
               0,0,0,0,0,0,0,0,0]
easySolved=[5,1,7,6,9,8,2,3,4,
             2,8,9,1,3,4,7,5,6,
             3,4,6,2,7,5,8,9,1,
             6,7,2,8,4,9,3,1,5,
             1,3,8,5,2,6,9,4,7,
             9,5,4,7,1,3,6,8,2,
             4,9,5,3,6,2,1,7,8,
             7,2,3,4,8,1,5,6,9,
             8,6,1,9,5,7,4,2,3]
i=0
q=0
thelist=[listofnumbers0,easyUnsolved, easySolved,hardUnsolved, hardSolved]

def easyLvl():
    global q
    q=1
    createGrid()

def easyLvlSolved():
    global q
    q=2
    createGrid()

def hardLvl():
    global q
    q=3
    createGrid()
def hardLvlSolved():
    global q
    q=4
    createGrid()

def btnCommand(x):
    if x==0:
        x=x+1





colourTxt="black"
#-----------------------------MAIN CODE------------------
def createGrid():
    for rowindex in range (9):
        for colindex in range (9):
            if (rowindex in (0,1,2,6,7,8) and colindex in (3,4,5) or \
                (rowindex in (3,4,5) and colindex in (0,1,2,6,7,8))):
                    colour="light blue"
            else:
                colour="white"

            global i
            x=thelist[q][i]
            i=i+1
            if i==81:
                i=0

            if x==0:
                colourTxt="red"
            else:
                colourTxt="black" 
            btn=Button(frame, width=8, height=4, bg=colour, text=x, fg=colourTxt, command=lambda:btnCommand(x))   
            btn.grid(row=rowindex, column=colindex, sticky=N+S+E+W)


            btn.grid(row=rowindex, column=colindex, sticky=N+S+E+W)
createGrid()
frame.mainloop()