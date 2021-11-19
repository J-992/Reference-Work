#collin zhong
#nov 3
#radio button learning
#why am i here
#winterlude tonight
#ughhhhh
"""
IF THIS NIGHT IS NOT FOREVER
AT LEAST WE ARE TOGETHER
AT LEAST I'M NOT ALONE
AT LEAST I'M NOT ALONE
EVERYWHERE WHENEVER
APART BUT STILL TOGETHER
I KNOW I'M NOT ALONE
I KNOW I'M NOT ALONE.
"""

import tkinter as tk
from tkinter import ttk


def quitButton():
    mainWindow.destroy()
    
def createLabels():
    outputLabel=tk.Label(outputFrame,
                         text="Your Choice:")
    choiceLabel=tk.Label(outputFrame,
                         textvariable=choice)
    outputLabel.place(x=150,y=100)
    choiceLabel.place(x=250,y=100)
def createButtons():
    B_Quit=tk.Button(quitFrame,text="QUIT",
                     command=quitButton)
    B_Quit.place(x=450,y=65)
def radioButtons():
    choice1Radio=ttk.Radiobutton(radioButtonFrame,text="choice 1",
                                 variable=choice,value="radio1")
    choice2Radio=ttk.Radiobutton(radioButtonFrame,text="choice 2",
                                 variable=choice,value="radio2")
    choice3Radio=ttk.Radiobutton(radioButtonFrame,text="choice 3",
                                 variable=choice,value="radio3")
    choice1Radio.place(x=100,y=100,width=100,height=25)
    choice2Radio.place(x=200,y=100,width=100,height=25)
    choice3Radio.place(x=300,y=100,width=100,height=25)
###=============PROGRAM STARTS==============###
mainWindow=tk.Tk()
mainWindow.title("Entry Widgets")
mainWindow.minsize(width=500,height=600)
mainWindow.maxsize(width=500,height=600)
radioButtonFrame=ttk.Frame(mainWindow,
                   width=500,
                   height=300)
outputFrame=ttk.Frame(mainWindow,
                      width=500,
                      height=200)
quitFrame=ttk.Frame(mainWindow,
                    width=500,
                    height=100)
radioButtonFrame.place(x=0,y=0)
outputFrame.place(x=0,y=300)
quitFrame.place(x=0,y=500)
choice=tk.StringVar()
createLabels()
createButtons()
radioButtons()

tk.mainloop
