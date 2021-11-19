#jaffer razavi
#nov 29 2019
#Entry Widgets

import tkinter as tk
from tkinter import ttk

#Creates what prints the output
def Convert():
    miles = float(KM.get())*0.6214
    KMLabel = tk.Label(TopFrame,
                       relief = 'sunken',
                       bg = 'snow2',
                       font=('Comic Sans MS',
                             16,
                             'bold'),
                       anchor = 'w',
                       text = format(miles,
                                     '.2f'))
    KMLabel.place(x=450,
                  y=70,
                  width=190,
                  height=25)

#creates quit button
def Quit():
    main_window.destroy()

#Creates the clear label (puts a blank label in place)
def Clear():
    ClearLabel = tk.Label(TopFrame,
                          bg = 'snow2',
                          relief = 'sunken')
    ClearLabel.place (x=450,y=70,width=190,height=25)
    KM.set ('')

#Creates the labels  
def CreateLabels():
    KMOutput = tk.Label(TopFrame,
                          bg = 'snow2',
                          relief = 'sunken')
    DistanceKM = tk.Label(TopFrame,
                          fg = 'black',
                          relief = 'raised',
                          font=('Comic Sans MS',
                                15,
                                'bold'),
                          text = 'Distance in KM: ')
    DistanceMiles = tk.Label(TopFrame,
                             fg = 'black',
                             relief = 'raised',
                             #font is in brackets because it has spaces in the font name
                             font=('Comic Sans MS',
                                   15,
                                   'bold'),
                             text = 'Distance in Miles: ')
    DistanceKM.place(x=200,y=35, width = 200, height = 25 )
    DistanceMiles.place(x=200,y=70,width = 200, height = 25 )
    KMOutput.place (x=450,y=70,width=190,height=25)

#Creates the buttons
def CreateButtons():
    B_Calculate = tk.Button(BottomFrame,
                            text = "Calculate",
                            fg ='green',
                            relief = 'raised',
                            #highlightbackground is used due to the fact mac can't display button colors properly
                            highlightbackground='#3E4149',
                            bd = 20,
                            font=('Comic Sans MS',
                                   20,
                                   'bold'),
                            command = Convert)
    B_Quit = tk.Button(BottomFrame,
                       text = "Quit",
                       fg = "green",
                       relief = 'raised',
                       highlightbackground='#3E4149',
                       bd = 20,
                       font=('Comic Sans MS',
                                   20,
                                   'bold'),
                       command = Quit)
    B_Clear = tk.Button(BottomFrame,
                        text = "Clear",
                        fg = "green",
                        relief = 'raised',
                        highlightbackground='#3E4149',
                        bd = 20,
                        font=('Comic Sans MS',
                                   20,
                                   'bold'),
                        command = Clear)
    B_Calculate.place(x=50,y=50, width = 300, height = 40)
    B_Clear.place(x=400,y=50, width = 300, height = 40)
    B_Quit.place(x=750,y=50, width = 300, height = 40)

#Creates Entry Box
def CreateEntry():
    KMEntry=tk.Entry(TopFrame,
                     font=('Comic Sans MS',
                                   20,
                                   'bold'),
                     textvariable=KM)
    KMEntry.place(x=450,y=35,width = 190, height = 25)

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#Creating Window
main_window = tk.Tk()
main_window.title('Using Entry Widgets')
main_window.minsize(width=1100,height=200)
main_window.maxsize(width=1100,height=200)

#Creating Frames
TopFrame = ttk.Frame(width=1100,
                     height=100)
TopFrame.place(x=0,y=0)

BottomFrame = ttk.Frame(width=1100,
                        height=100)
BottomFrame.place(x=0,y=100)

#Defining the entry window
KM=tk.DoubleVar()
KM.set('')

#Calling All the defs
CreateLabels()
CreateButtons()
CreateEntry()

#Mainloop
tk.mainloop()
