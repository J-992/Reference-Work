#Jaffer Razavi
#Bubble Tea Buttons
#Dec 5 2019

import tkinter as tk
from tkinter import ttk

def QuitButton():
    main_window.destroy()

def ScreenLabels():
    OutputLabel = tk.Label(OutputFrame,
                           text = "Your Choice: ",
                           bg="lightblue")
   
    Title = tk.Label(TitleFrame,
                     text = "Bubble Tea",
                     bg="lightblue",font='Helvectica 20 bold')

    
    SizeLabel = tk.Label(TitleFrame,
                         text="Size",
                         bg="lightblue",
                         font='Helvectica 20 bold')
    TypeLabel = tk.Label(TitleFrame,
                         text = "Flavour",
                         bg="lightblue",
                         font='Helvectica 20 bold')
    ToppingLabel = tk.Label(TitleFrame,
                            text = "Toppings",
                            bg="lightblue",
                            font='Helvectica 20 bold')


    Title.place(x=400,y=0)
    OutputLabel.place(x = 0, y = 50)
    TypeLabel.place(x=100,y=50)
    SizeLabel.place(x=450,y=50)
    ToppingLabel.place(x=650,y=50)

##def Clear():
##    ClearOutput = tk.Label(OutputFrame,bg='lightblue')
##    ClearOutput.place(x=200,y=50,width=700,height=25)
##    RadioButtons()
    
def Output():
    ChoiceLabel = tk.Label(OutputFrame,
                           text=heated.get()+' '+
                           size.get()+' '+
                           choice.get()+
                           ' with'+' '+
                           extraice.get()+' '+
                           noice.get()+' '+
                           extrasugar.get()+' '+
                           nosugar.get(),
                           bg="lightblue")
    ChoiceLabel.place(x = 200, y = 50)
    
    
def CreateButtons():
##    B_Clear=tk.Button(OutputFrame,text="CLEAR",
##                      command=Clear,
##                      bg='lightblue')
    
    B_Quit=tk.Button(OutputFrame,text="QUIT",
                     command=QuitButton,
                     bg="lightblue")
    SubmitButton=tk.Button(OutputFrame,
                           text="Create",
                           fg="SlateBlue3",
                           bg="salmon",
                           command=Output)

##    B_Clear.place(x=0,y=20)
    SubmitButton.place(x=0, y=0)
    B_Quit.place(x=850,y=65)
    
def RadioButtons():
    
    Milk=tk.Radiobutton(TeaFlavourFrame,
                         text="Milk Tea",
                         variable=choice,
                         value="Milk Tea",
                         bg="lightblue")
    Mango=tk.Radiobutton(TeaFlavourFrame,
                          text="Mango Slushie",
                          variable=choice,
                          value="Mango Slushie",
                          bg="lightblue")
    Strawberry=tk.Radiobutton(TeaFlavourFrame,
                              text="Strawberry",
                              variable=choice,
                              value="Strawberry",
                              bg="lightblue")
    
    Small=tk.Radiobutton(TeaSizeFrame,text="Small",
                          variable=size,
                          value="Small",
                          bg="lightblue")
    Medium=tk.Radiobutton(TeaSizeFrame,
                          text="Medium",
                          variable=size,
                          value="Medium",
                          bg="lightblue")
    Large=tk.Radiobutton(TeaSizeFrame,
                         text="Large",
                         variable=size,
                         value="Large",
                         bg="lightblue")
    
    ExtraIce=tk.Radiobutton(Extra_Ice,text="Extra Ice",
                            variable=extraice,
                            value="Extra Ice",
                            bg="lightblue")
    NoIce=tk.Radiobutton(No_Ice,text="No Ice",
                         variable=noice,
                         value="No Ice",
                         bg="lightblue")
    ExtraSugar=tk.Radiobutton(Extra_Sugar,text="Extra Sugar",
                              variable=extrasugar,
                              value="Extra Sugar",
                              bg="lightblue")
    NoSugar=tk.Radiobutton(No_Sugar,text="No Sugar",
                           variable=nosugar,
                           value="No Sugar",
                           bg="lightblue")
    HeatedChoice=tk.Radiobutton(Heated,text="Heated",
                                variable=heated,
                                value="Heated",
                                bg="lightblue")
    
    ExtraIce.place(x=0,y=0,width=100,height=25)
    NoIce.place(x=0,y=0,width=100,height=25)
    ExtraSugar.place(x=0,y=0,width=100,height=25)
    NoSugar.place(x=0,y=0,width=100,height=25)
    HeatedChoice.place(x=0,y=0,width=100,height=25)
    Small.place(x=100,y=100,width=100,height=25)
    Medium.place(x=100,y=150,width=100,height=25)
    Large.place(x=100,y=200,width=100,height=25)
    Milk.place(x=100,y=100,width=100,height=25)
    Mango.place(x=100,y=150,width=150,height=25)
    Strawberry.place(x=100,y=200,width=100,height=25)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------MAIN PROGRAM--------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#--------------Creating Window--------------
main_window = tk.Tk()
main_window.title('Bubble Tea Buttons - Jaffer Razavi')
main_window.minsize(width=900,height=500)
main_window.maxsize(width=900,height=500)

#--------------PRIMARY FRAMES--------------
TitleFrame = tk.Frame(width=900,
                     height=100)
TitleFrame.place(x=0,y=0)
TitleFrame.config(bg="lightblue")

TeaFlavourFrame = tk.Frame(width=300,
                     height=300)
TeaFlavourFrame.place(x=0,y=100)
TeaFlavourFrame.config(bg="lightblue")

TeaSizeFrame = tk.Frame(width=300,
                     height=300)
TeaSizeFrame.place(x=300,y=100)
TeaSizeFrame.config(bg="lightblue")


#--------------OPTION FRAMES--------------

Extra_Ice = tk.Frame(width=300,
                     height=60)
Extra_Ice.place(x=600,y=100)
Extra_Ice.config(bg="lightblue")

No_Ice = tk.Frame(width=300,
                     height=60)
No_Ice.place(x=600,y=160)
No_Ice.config(bg="lightblue")

Extra_Sugar = tk.Frame(width=300,
                     height=60)
Extra_Sugar.place(x=600,y=220)
Extra_Sugar.config(bg="lightblue")

No_Sugar = tk.Frame(width=300,
                     height=60)
No_Sugar.place(x=600,y=280)
No_Sugar.config(bg="lightblue")

Heated = tk.Frame(width=300,
                     height=60)
Heated.place(x=600,y=340)
Heated.config(bg="lightblue")

#--------------OUTPUT--------------

OutputFrame = tk.Frame(width=900,
                        height=100)
OutputFrame.place(x=0,y=400)
OutputFrame.config(bg="lightblue")

#--------------INITIALIZING VARIABLES--------------
choice = tk.StringVar()
size = tk.StringVar()
extraice = tk.StringVar()
noice = tk.StringVar()
extrasugar = tk.StringVar()
nosugar = tk.StringVar()
heated = tk.StringVar()

#--------------CALLING DEFS--------------
RadioButtons()
CreateButtons()
ScreenLabels()






