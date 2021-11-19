#Name: Alex Fernandes
#Date: 12.3.2019
#Description: A programs the presents the user with 3 choices

#importing libraries
import tkinter as tk
from tkinter import ttk

#Functions--------------------------------------------------

#Creating Quite Window
#Creating the Labels
def Labels():
    TitleLabel=tk.Label(TitleFrame, text="Bubble Tea",
                        fg="snow",
                        bg="MediumOrchid1",
                        font="Verdana 30 bold italic")
    Title2Label=tk.Label(TitleFrame, text="Create your Bubble Tea",
                         fg="snow",
                         bg="MediumOrchid1",
                         font="Verdana 10 italic")
    TitleLabel.place(x=0, y=10, width=450,  height=35)
    Title2Label.place(x=0, y=50, width=450, height=20)

    TypeLabel=tk.Label(TypeFrame, text="Type:",
                       bg="SkyBlue2",
                       fg="snow",
                       font="Verdana 10 bold ")
    TypeLabel.place(x=10,y=10)

    SizeLabel=tk.Label(SizeFrame, text="Size:",
                       bg="SkyBlue2",
                       fg="snow",
                       font="Verdana 10 bold "
                       )
    SizeLabel.place(x=10,y=10)

    AddOnLabel=tk.Label(AddOnFrame, text="Add Ons:",
                        bg="SkyBlue2",
                        fg="snow",
                        font="Verdana 10 bold ")
    AddOnLabel.place(x=10,y=10)

#Command to create bubble tea
def Output():
    ChoiceLabel=ttk.Label(OutputFrame,
text=choice2.get()+choice1.get()+" with"+choice3.get()+choice4.get()+choice5.get()+choice6.get()+choice7.get())
    ChoiceLabel.place(x=200, y=50)

#Creating the Buttons
def Buttons():
    CreateButton=tk.Button(OutputFrame,
                           text="Create",
                           fg="SlateBlue3",
                           bg="salmon",
                           command=Output)
    CreateButton.place(x=0, y=0, width=200, height=75)

#Creating the Radio Buttons
def setupRadioButtons():
    s = ttk.Style()
    s.configure('Style.TRadiobutton',
    background="SkyBlue2",
                foreground="white")
    Type1=ttk.Radiobutton(TypeFrame, text="Coffee", variable=choice1,
value=" coffee", style='Style.TRadiobutton')
    Type2=ttk.Radiobutton(TypeFrame, text="Tea", variable=choice1,
value=" tea", style='Style.TRadiobutton')
    Type3=ttk.Radiobutton(TypeFrame, text="Water", variable=choice1,
value=" water", style='Style.TRadiobutton')
    Type4=ttk.Radiobutton(TypeFrame, text="Juice", variable=choice1,
value=" juice", style='Style.TRadiobutton')
    Type1.place(x=10, y=50, width=150, height=25)
    Type2.place(x=10, y=100, width=150, height=25)
    Type3.place(x=10, y=150, width=150, height=25)
    Type4.place(x=10, y=200, width=150, height=25)

    Size1=ttk.Radiobutton(SizeFrame, text="Small", variable=choice2,
value="A small ", style='Style.TRadiobutton')
    Size2=ttk.Radiobutton(SizeFrame, text="Medium", variable=choice2,
value="A medium ", style='Style.TRadiobutton')
    Size3=ttk.Radiobutton(SizeFrame, text="Large", variable=choice2,
value="A large ", style='Style.TRadiobutton')
    Size1.place(x=10, y=50, width=150, height=25)
    Size2.place(x=10, y=100, width=150, height=25)
    Size3.place(x=10, y=150, width=150, height=25)

    AddOn1=ttk.Radiobutton(AddOn1Frame, text="Grass",
variable=choice3, value="grass ", style='Style.TRadiobutton')
    AddOn2=ttk.Radiobutton(AddOn2Frame, text="Air", variable=choice4,
value="air ", style='Style.TRadiobutton')
    AddOn3=ttk.Radiobutton(AddOn3Frame, text="My tears",
variable=choice5, value="my tears ", style='Style.TRadiobutton')
    AddOn4=ttk.Radiobutton(AddOn4Frame, text="Eternal Suffering",
variable=choice6, value="eternal suffering ",
style='Style.TRadiobutton')
    AddOn5=ttk.Radiobutton(AddOn5Frame, text="A black hole",
variable=choice7, value="a black hole", style='Style.TRadiobutton')
    AddOn1.place(x=10, y=0, width=150, height=25)
    AddOn2.place(x=10, y=0, width=150, height=25)
    AddOn3.place(x=10, y=0, width=150, height=25)
    AddOn4.place(x=10, y=0, width=150, height=25)
    AddOn5.place(x=10, y=0, width=150, height=25)



#MainProgram------------------------------------------------

#Creating the window
window=tk.Tk()
window.title("Bubble Buttons")
window.minsize(width=450, height=500)

#Creating the  Frames
TitleFrame=tk.Frame(master=window, width=450, height=100)
OutputFrame=tk.Frame(master=window, width=450, height=100)
TypeFrame=tk.Frame(master=window, width=150, height=300)
SizeFrame=tk.Frame(master=window, width=150, height=300)
AddOnFrame=tk.Frame(master=window, width=150, height=50)
AddOn1Frame=tk.Frame(master=window, width=150, height=50)
AddOn2Frame=tk.Frame(master=window, width=150, height=50)
AddOn3Frame=tk.Frame(master=window, width=150, height=50)
AddOn4Frame=tk.Frame(master=window, width=150, height=50)
AddOn5Frame=tk.Frame(master=window, width=150, height=50)


TitleFrame.place(x=0, y=0)
OutputFrame.place(x=0, y=400)
TypeFrame.place(x=0, y=100)
SizeFrame.place(x=150, y=100)
AddOnFrame.place(x=300, y=100)
AddOn1Frame.place(x=300, y=150)
AddOn2Frame.place(x=300, y=200)
AddOn3Frame.place(x=300, y=250)
AddOn4Frame.place(x=300, y=300)
AddOn5Frame.place(x=300, y=350)

TitleFrame.config(bg="MediumOrchid1")
OutputFrame.config(bg="MediumOrchid1")
TypeFrame.config(bg="SkyBlue2")
SizeFrame.config(bg="SkyBlue2")
AddOnFrame.config(bg="SkyBlue2")
AddOn1Frame.config(bg="SkyBlue2")
AddOn2Frame.config(bg="SkyBlue2")
AddOn3Frame.config(bg="SkyBlue2")
AddOn4Frame.config(bg="SkyBlue2")
AddOn5Frame.config(bg="SkyBlue2")

choice1=tk.StringVar()
choice2=tk.StringVar()
choice3=tk.StringVar()
choice4=tk.StringVar()
choice5=tk.StringVar()
choice6=tk.StringVar()
choice7=tk.StringVar()

Labels()
Buttons()
setupRadioButtons()
