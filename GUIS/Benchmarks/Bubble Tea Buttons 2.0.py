#Jaffer Razavi
#Bubble Tea Buttons
#Dec 5 2019

import tkinter as tk
from tkinter import ttk

#-------------- QUIT BUTTON --------------

def QuitWindow():
    def QuitComment():
        Yes_window.destroy()
        No_window.destroy()
        Comment_window.destroy()
        
    def QuitProgram():
        main_window.destroy()
        Yes_window.destroy()
        No_window.destroy()
        Comment_window.destroy()
    
    Yes_window = tk.Tk()
    Yes_window.title("–––––")
    Yes_window.geometry("100x100+400+500")
    
    No_window = tk.Tk()
    No_window.title("–––––")
    No_window.geometry("100x100+500+500")
    
    Comment_window = tk.Tk()
    Comment_window.title("–––––")
    Comment_window.geometry("200x60+400+420")
    
    CheckingLabel = tk.Label(Comment_window,
                             text = 'Are you sure you want to quit?',
                             font = ('comic sans ms',
                                     12,
                                     'bold'))
    ProgramYes = tk.Button(Yes_window,
                           text = 'Yes',
                           command = QuitProgram,
                           cursor = 'X_cursor')
    ProgramNo = tk.Button(No_window,
                          text = 'No',
                          command = QuitComment)
    
    CheckingLabel.place(x=0,
                        y=0,
                        width = 200,
                        height = 70)
    ProgramYes.place(x=0,
                     y=0,
                     width = 100,
                     height = 100)
    ProgramNo.place(x=0,
                    y=0,
                    width = 100,
                    height = 100)

#-------------- LABELS --------------
def ScreenLabels():
    OutputLabel = tk.Label(OutputFrame,
                           text = "Your Choice: ",
                           bg="lightblue")
   
    TitleLabel = tk.Label(TitleFrame,
                          text = "Bubble Tea",
                          bg="lightblue",
                          font='Helvectica 20 bold')
    
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
 
    TitleLabel.place(x=200,
                     y=0)
    OutputLabel.place(x = 0,
                      y = 0)
    TypeLabel.place(x=10,
                    y=50)
    SizeLabel.place(x=250,
                    y=50)
    ToppingLabel.place(x=450,
                       y=50)

#-------------- CLEAR COMMAND --------------
def Clear():
    ClearOutputLabel = tk.Label(OutputFrame,
                                bg='lightblue')
    ClearOutputLabel.place(x=100,
                           y=0,
                           width=200,
                           height=100)
    
    choice_tk.set(0)
    size_tk.set(0)
    extraice_tk.set(0)
    noice_tk.set(0)
    extrasugar_tk.set(0)
    nosugar_tk.set(0)
    heated_tk.set(0)

#-------------- CREATING OUTPUT BOX --------------
def Output():
    Heated = ''
    ExtraIce = ''
    NoIce = ''
    ExtraSugar = ''
    NoSugar = ''

    if (extraice_tk.get() == 1):
        ExtraIce = '\n-Extra Ice'
    if (noice_tk.get() ==1):
        NoIce = '\n-No Ice'
    if (extrasugar_tk.get() ==1):
        ExtraSugar = '\n-Extra Sugar'
    if (nosugar_tk.get() ==1):
        NoSugar = '\n-No Sugar'
    if (heated_tk.get() ==1):
        Heated = 'Heated '
    ChoiceLabel = tk.Label(OutputFrame,
                           text = Heated+
                           size_tk.get()+
                           choice_tk.get()+
                           ' with:'+
                           ExtraIce+
                           NoIce+
                           ExtraSugar+
                           NoSugar,
                           bg="lightblue")
    ChoiceLabel.place(x = 100, y = 0)
    
def CreateButtons():
    ClearButton=tk.Button(OutputFrame,text="CLEAR",
                          command=Clear,
                          bg='lightblue')
    
    QuitButton=tk.Button(OutputFrame,text="QUIT",
                         command=QuitWindow,
                         bg="lightblue")
    OrderButton=tk.Button(OutputFrame,
                          text="CREATE",
                          command=Output)

    QuitButton.place(x=500,
                     y=0,
                     width = 100,
                     height = 50)
    OrderButton.place(x=500,
                      y=50,
                      width = 100,
                      height = 50)
    ClearButton.place(x=500,
                      y=100,
                      width = 100,
                      height = 50)

def RadioButtons():
    #------------- FLAVOUR RADIO BUTTONS -------------
    MilkRadioButton=tk.Radiobutton(TeaFlavourFrame,
                                   text="Milk Tea",
                                   variable=choice_tk,
                                   value=" Milk Tea",
                                   bg="lightblue")
    MangoRadioButton=tk.Radiobutton(TeaFlavourFrame,
                                    text="Mango Slushie",
                                    variable=choice_tk,
                                    value=" Mango Slushie",
                                    bg="lightblue")
    StrawberryRadioButton=tk.Radiobutton(TeaFlavourFrame,
                                         text="Strawberry",
                                         variable=choice_tk,
                                         value=" Strawberry",
                                         bg="lightblue")
    #------------- SIZE RADIO BUTTONS -------------
    
    SmallRadioButton=tk.Radiobutton(TeaSizeFrame,text="Small",
                                    variable=size_tk,
                                    value="Small",
                                    bg="lightblue")
    MediumRadioButton=tk.Radiobutton(TeaSizeFrame,
                                     text="Medium",
                                     variable=size_tk,
                                     value="Medium",
                                     bg="lightblue")
    LargeRadioButton=tk.Radiobutton(TeaSizeFrame,
                                    text="Large",
                                    variable=size_tk,
                                    value="Large",
                                    bg="lightblue")

    #------------- ADDITION CHECK BOXES -------------
    
    ExtraIceCheckButton=tk.Checkbutton(OptionFrame,text="Extra Ice",
                                       variable=extraice_tk,
                                       bg="lightblue")
    NoIceCheckButton=tk.Checkbutton(OptionFrame,text="No Ice",
                                    variable=noice_tk,
                                    bg="lightblue")
    ExtraSugarCheckButton=tk.Checkbutton(OptionFrame,
                                         text="Extra Sugar",
                                         variable=extrasugar_tk,
                                         bg="lightblue")
    NoSugarCheckButton=tk.Checkbutton(OptionFrame,text="No Sugar",
                                      variable=nosugar_tk,
                                      bg="lightblue")
    HeatedChoiceCheckButton=tk.Checkbutton(OptionFrame,
                                           text="Heated",
                                           variable=heated_tk,
                                           bg="lightblue")

    #------------- PLACING CHECK BOXES -------------
    
    ExtraIceCheckButton.place(x=0,
                              y=0,
                              width=100,
                              height=25)
    NoIceCheckButton.place(x=0,
                           y=60,
                           width=100,
                           height=25)
    ExtraSugarCheckButton.place(x=0,
                                y=120,
                                width=100,
                                height=25)
    NoSugarCheckButton.place(x=0,
                             y=180,
                             width=100,
                             height=25)
    HeatedChoiceCheckButton.place(x=0,
                                  y=240,
                                  width=100,
                                  height=25)

    #------------- PLACING BUTTONS -------------
    
    SmallRadioButton.place(x=10,
                           y=100,
                           width=100,
                           height=25)
    MediumRadioButton.place(x=10,
                            y=150,
                            width=100,
                            height=25)
    LargeRadioButton.place(x=10,
                           y=200,
                           width=100,
                           height=25)
    MilkRadioButton.place(x=10,
                          y=100,
                          width=100,
                          height=25)
    MangoRadioButton.place(x=10,
                           y=150,
                           width=150,
                           height=25)
    StrawberryRadioButton.place(x=10,
                                y=200,
                                width=100,
                                height=25)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------MAIN PROGRAM--------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#--------------Creating Window--------------
main_window = tk.Tk()
main_window.title('Bubble Tea Buttons - Jaffer Razavi')
main_window.minsize(width=600,
                    height=550)
main_window.maxsize(width=600,
                    height=550)

#--------------FRAMES--------------
TitleFrame = tk.Frame(width=700,
                      height=100)
TitleFrame.place(x=0,
                 y=0)
TitleFrame.config(bg="lightblue")

TeaFlavourFrame = tk.Frame(width=200,
                           height=300)
TeaFlavourFrame.place(x=0,
                      y=100)
TeaFlavourFrame.config(bg="lightblue")

TeaSizeFrame = tk.Frame(width=200,
                        height=300)
TeaSizeFrame.place(x=200,
                   y=100)
TeaSizeFrame.config(bg="lightblue")

OptionFrame = tk.Frame(width = 200,
                       height = 300)
OptionFrame.place(x=400,
                  y=100)
OptionFrame.config(bg="lightblue")

#--------------OUTPUT--------------

OutputFrame = tk.Frame(width=700,
                       height=300)
OutputFrame.place(x=0,
                  y=400)
OutputFrame.config(bg="lightblue")

#--------------INITIALIZING VARIABLES--------------
choice_tk = tk.StringVar()
size_tk = tk.StringVar()
extraice_tk = tk.IntVar()
noice_tk = tk.IntVar()
extrasugar_tk = tk.IntVar()
nosugar_tk = tk.IntVar()
heated_tk = tk.IntVar()

#--------------CALLING DEFS--------------
ScreenLabels()
CreateButtons()
RadioButtons()
