#Name: Alex Fernandes
#Date: 12.3.2019
#Description: A programs the presents the user with 3 choices

#importing libraries
import tkinter as tk
from tkinter import ttk
from tkinter import *

#Functions--------------------------------------------------


#Creating the clear window function
def ClearWindow():
    choice1.set(0)
    choice2.set(0)
    choice3.set(0)
    choice4.set(0)
    choice5.set(0)
    choice6.set(0)
    choice7.set(0)
    ClearLabel=tk.Label(OutputFrame, text="",
                         anchor="w",
                          fg="salmon",
                          bg="MediumPurple1",
                          font="none 10 bold")
    ClearLabel.place(x=250, y=15, width=300, height=300)

#Creating Quit Window
def WindowQuitter():
    QuitWindow=tk.Tk()
    QuitWindow.minsize(width=200, height=50)
    QuitWindow.title("")

    QuitLabel=tk.Label(QuitWindow, text="Are you sure you \nwant to quit?")
    QuitLabel.place(x=40, y=0)
    def UltimateQuitWindow():
        QuitWindow.destroy()
        window.destroy()

    QuitQuitterButton=tk.Button(QuitWindow,
                                text=" Quit ",
                                command=UltimateQuitWindow)
    CancelQuitterButton=tk.Button(QuitWindow,
                                  text="Cancel",
                                  command=QuitWindow.destroy)
    QuitQuitterButton.place(x=25,y=100)
    CancelQuitterButton.place(x=120, y=100)

#Creating the Labels
def Labels():
    TitleLabel=tk.Label(TitleFrame, text="Bubble Tea",
                        fg="snow",
                        bg="MediumPurple1",
                        font="Verdana 30 bold italic")
    Title2Label=tk.Label(TitleFrame, text="Create your Bubble Tea",
                         fg="snow",
                         bg="MediumPurple1",
                         font="Verdana 10 italic")
    TitleLabel.place(x=0, y=10, width=460,  height=45)
    Title2Label.place(x=0, y=70, width=460, height=20)

    TypeLabel=tk.Label(TypeFrame, text="Type:",
                       bg="SkyBlue2",
                       fg="snow",
                       font="Verdana 10 bold ")
    TypeLabel.place(x=10,y=10)

    SizeLabel=tk.Label(SizeFrame, text="Size:",
                       bg="SkyBlue2",
                       fg="snow",
                       font="Verdana 10 bold ")
    SizeLabel.place(x=10,y=10)

    AddOnLabel=tk.Label(AddOnFrame, text="Add Ons:",
                        bg="SkyBlue2",
                        fg="snow",
                        font="Verdana 10 bold ")
    AddOnLabel.place(x=10,y=10)

#Command to create bubble tea
def Output():
    var3=""
    if(choice3.get()==1):
        var3="\n-grass"
    var4=""
    if(choice4.get()==1):
        var4="\n-air"
    var5=""
    if(choice5.get()==1):
        var5="\n-my tears"
    var6=""
    if(choice6.get()==1):
        var6="\n-eternal suffering"
    var7=""
    if(choice7.get()==1):
        var7="\n-a black hole"
    ChoiceLabel=tk.Label(OutputFrame,
text=choice2.get()+choice1.get()+" with:"+var3+var4+var5+var6+var7,
                         anchor="w",
                          fg="white",
                          bg="MediumPurple1",
                          font="none 10 bold")
    ChoiceLabel.place(x=250, y=15)

#Creating the Buttons
def Buttons():
    CreateButton=tk.Button(OutputFrame,
                           text="Create",
                           fg="SlateBlue3",
                           bg="salmon",
                           command=Output)
    CreateButton.place(x=16, y=15, width=150, height=50)

    QuitButton=tk.Button(OutputFrame,
                         text="Quit",
                         fg="SlateBlue3",
                         bg="salmon",
                         command=WindowQuitter)
    QuitButton.place(x=16, y=75, width=150, height=50)

    ClearButton=tk.Button(OutputFrame,
                          text="Clear",
                          fg="SlateBlue3",
                          bg="salmon",
                          command=ClearWindow)
    ClearButton.place(x=16, y=135, width=150, height=50)

#Creating the Radio Buttons
def setupRadioButtons():
    s = ttk.Style()
    s.configure('Style.TRadiobutton',
    background="SkyBlue2",
                foreground="black",
                font="Ariel 10 italic")

    Type1=ttk.Radiobutton(TypeFrame, text="Coffee", variable=choice1,
value="coffee", style='Style.TRadiobutton')
    Type2=ttk.Radiobutton(TypeFrame, text="Tea", variable=choice1,
value="tea", style='Style.TRadiobutton')
    Type3=ttk.Radiobutton(TypeFrame, text="Water", variable=choice1,
value="water", style='Style.TRadiobutton')
    Type4=ttk.Radiobutton(TypeFrame, text="Juice", variable=choice1,
value="juice", style='Style.TRadiobutton')
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

    AddOn1=tk.Checkbutton(AddOnFrame, text="Grass", variable=choice3,
bg="SkyBlue2", font="Ariel 10 italic", anchor='w')
    AddOn2=tk.Checkbutton(AddOnFrame, text="Air", variable=choice4,
bg="SkyBlue2", font="Ariel 10 italic", anchor='w')
    AddOn3=tk.Checkbutton(AddOnFrame, text="My tears",
variable=choice5,  bg="SkyBlue2", font="Ariel 10 italic", anchor='w')
    AddOn4=tk.Checkbutton(AddOnFrame, text="Eternal Suffering",
variable=choice6,  bg="SkyBlue2", font="Ariel 10 italic", anchor='w')
    AddOn5=tk.Checkbutton(AddOnFrame, text="A black hole",
variable=choice7,  bg="SkyBlue2", font="Ariel 10 italic", anchor='w')
    AddOn1.place(x=10, y=50, width=150, height=25)
    AddOn2.place(x=10, y=100, width=150, height=25)
    AddOn3.place(x=10, y=150, width=150, height=25)
    AddOn4.place(x=10, y=200, width=150, height=25)
    AddOn5.place(x=10, y=250, width=150, height=25)



#MainProgram------------------------------------------------

#Creating the window
window=tk.Tk()
window.title("Bubble Buttons 2.0")
window.minsize(width=460, height=600)

#Creating the  Frames
TitleFrame=tk.Frame(master=window, width=460, height=100)
OutputFrame=tk.Frame(master=window, width=460, height=200)
TypeFrame=tk.Frame(master=window, width=160, height=300)
SizeFrame=tk.Frame(master=window, width=160, height=300)
AddOnFrame=tk.Frame(master=window, width=160, height=300)


TitleFrame.place(x=0, y=0)
OutputFrame.place(x=0, y=400)
TypeFrame.place(x=0, y=100)
SizeFrame.place(x=150, y=100)
AddOnFrame.place(x=300, y=100)

TitleFrame.config(bg="MediumPurple1")
OutputFrame.config(bg="MediumPurple1")
TypeFrame.config(bg="SkyBlue2")
SizeFrame.config(bg="SkyBlue2")
AddOnFrame.config(bg="SkyBlue2")

choice1=tk.StringVar()
choice2=tk.StringVar()
choice3=tk.IntVar()
choice4=tk.IntVar()
choice5=tk.IntVar()
choice6=tk.IntVar()
choice7=tk.IntVar()

Labels()
Buttons()
setupRadioButtons()
