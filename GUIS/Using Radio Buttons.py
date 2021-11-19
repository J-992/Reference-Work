#Jaffer Razavi
#December 3 2019
#Using Radio Buttons

import tkinter as tk
from tkinter import ttk

def QuitButton():
    main_window.destroy()

def ScreenLabels():
    OutputLabel = ttk.Label(OutputFrame,
                            text = "Your Choice: ")
    ChoiceLabel = ttk.Label(OutputFrame,
                            textvariable = choice)
    OutputLabel.place(x = 400, y = 100, width = 150, height = 25)
    ChoiceLabel.place(x=550,y = 100,width=150,height=25)

def ScreenButtons():
    B_Quit = tk.Button(BottomFrame,
                       text = "Quit",
                       command = Quit)

def SetupRadioButtons():
    choice1RadioButton = ttk.Radiobutton(RadioButtonFrame,
                                         text = "Choice 1",
                                         variable = choice,
                                         value = 'Radio Button 1')
    choice2RadioButton = ttk.Radiobutton(RadioButtonFrame,
                                         text = "Choice 2",
                                         variable = choice,
                                         value = 'Radio Button 2')
    choice3RadioButton = ttk.Radiobutton(RadioButtonFrame,
                                         text = "Choice 3",
                                         variable = choice,
                                         value = 'Radio Button 3')
    
#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#Creating Window
main_window = tk.Tk()
main_window.title('Using Radio Buttons - Jaffer Razavi')
main_window.minsize(width=1100,height=600)
main_window.maxsize(width=1100,height=600)

#Creating Frames
RadioButtonFrame = ttk.Frame(width=600,
                     height=200)
RadioButtonFrame.place(x=0,y=0)

OutputFrame = ttk.Frame(width=1100,
                        height=200)
OutputFrame.place(x=0,y=300)

ButtonFrame = ttk.Frame(width=1100,
                        height=200)
ButtonFrame.place(x=0,y=300)

choice = tk.StringVar()

#Calling All the defs

SetupRadioButtons()
ScreenLabels()
QuitButton()


#Mainloop
tk.mainloop()
