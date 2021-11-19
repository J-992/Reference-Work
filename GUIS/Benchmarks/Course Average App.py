#jaffer razavi
#dec 2 2019
#Course Average Program

import tkinter as tk
from tkinter import ttk

#creates quit button
def Quit():
    main_window.destroy()

#Clear Button
def Clear():
    ClearLabel = tk.Label(TopFrame)
    ClearLabel.place (x=300,y=225,width=190,height=25)
    P1.set ('0')
    P2.set('0')
    P3.set('0')
    P4.set('0')

#Creates Labels
def CreateLabels():
    PD1 = tk.Label(TopFrame,
                    fg = 'black',
                    text = 'Tech: ')
    PD2 = tk.Label(TopFrame,
                    fg = 'black',
                    text = 'Math:')
    PD3 = tk.Label(TopFrame,
                    fg = 'black',
                    text = 'English:')
    PD4 = tk.Label(TopFrame,
                    fg = 'black',
                    text = 'Computer Science')
    Avg = tk.Label(TopFrame,
                    fg = 'black',
                    text = 'Average')
    
    PD1.place(x=100,y=25, width = 200, height = 25 )
    PD2.place(x=100,y=50, width = 200, height = 25 )
    PD3.place(x=100,y=75, width = 200, height = 25 )
    PD4.place(x=100,y=100, width = 200, height = 25 )
    Avg.place(x=100,y=225, width = 200, height = 25 )

#creates entry widgets
def Calculate():
    avg1 = float(P1.get())
    avg2= float(P2.get())
    avg3= float(P3.get())
    avg4= float(P4.get())
    topavg = (avg1+avg2+avg3+avg4)/4
    AverageLabel = tk.Label(TopFrame,
                            anchor = 'w',
                            text = format(topavg,
                                          '.2f'))
    AverageLabel.place(x=300,y=225, width = 190, height = 25 )

    
#Creates Entry Box
def CreateEntry():
    P1Entry=tk.Entry(TopFrame,
                     textvariable=P1)
    
    P2Entry=tk.Entry(TopFrame,
                     textvariable=P2)
    
    P3Entry=tk.Entry(TopFrame,
                     textvariable=P3)
    
    P4Entry=tk.Entry(TopFrame,
                     textvariable=P4)
    P1Entry.place(x=300,y=25, width = 200, height = 25 )
    P2Entry.place(x=300,y=50, width = 200, height = 25 )
    P3Entry.place(x=300,y=75, width = 200, height = 25 )
    P4Entry.place(x=300,y=100, width = 200, height = 25 )


#Creates the buttons
def CreateButtons():
    B_Calculate = tk.Button(BottomFrame,
                            text = "Calculate",
                            fg ='black',
                            command = Calculate)
    B_Quit = tk.Button(BottomFrame,
                       text = "Quit",
                       fg = "black",
                       command = Quit)
    B_Clear = tk.Button(BottomFrame,
                        text = "Clear",
                        fg = "black",
                        command = Clear)
    B_Calculate.place(x=0,y=50, width = 200, height = 40)
    B_Clear.place(x=200,y=50, width = 200, height = 40)
    B_Quit.place(x=400,y=50, width = 200, height = 40)

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#Creating Window
main_window = tk.Tk()
main_window.title('Course Average Program - Jaffer Razavi')
main_window.minsize(width=600,height=400)
main_window.maxsize(width=600,height=600)

#Creating Frames
TopFrame = ttk.Frame(width=600,
                     height=300)
TopFrame.place(x=0,y=0)

BottomFrame = ttk.Frame(width=600,
                        height=100)
BottomFrame.place(x=0,y=300)

#Defining the entry window
P1=tk.DoubleVar()
P2=tk.DoubleVar()
P3=tk.DoubleVar()
P4=tk.DoubleVar()
P1.set('0')
P2.set('0')
P3.set('0')
P4.set('0')

#Calling All the defs
CreateLabels()
CreateButtons()
CreateEntry()

#Mainloop
tk.mainloop()
