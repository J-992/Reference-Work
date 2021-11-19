#jaffer Razavi
#Check Buttons
#dec 9 2019
import tkinter as tk
from tkinter import ttk

def QuitButton():
      main_window.destroy()

def SummaryButton():
      Milk = 'Milk: '+str(MilkChoice.get())
      Honey = 'Honey: '+str(HoneyChoice.get())
      MilkChoiceLabel = tk.Label(CheckButtonFrame,
                                 text = Milk)
      HoneyChoiceLabel = tk.Label(CheckButtonFrame,
                                  text = Honey)
      MilkChoiceLabel.place(x = 650,y = 200)
      HoneyChoiceLabel.place(x = 650,y = 240)
      
def ScreenLabels():
      Title = tk.Label(CheckButtonFrame,
                       text = 'Title',
                       font= ('comic sans ms', 20, 'bold'))
      Title.place(x = 550, y = 50)

def ScreenButtons():
      B_Quit = tk.Button(ButtonFrame,
                         text = 'Quit',
                         command = QuitButton)
      B_Summary = tk.Button(ButtonFrame,
                            text = 'Summary',
                            command = SummaryButton)
      B_Quit.place(x = 800, y = 100)
      B_Summary.place(x = 300, y = 100)
      
def SetupCheckButtons():
      MilkCheckButton = tk.Checkbutton(CheckButtonFrame,text = 'Milk',variable = MilkChoice)
      HoneyCheckButton = tk.Checkbutton(CheckButtonFrame,text = 'Honey',variable = HoneyChoice)
      MilkCheckButton.place(x=400,y=100,width=150,height=25)
      HoneyCheckButton.place(x=700,y=100,width=150,height=25)


#------------------- MAIN PROGRAM -------------------

main_window = tk.Tk()
main_window.title('CheckButtons')
main_window.minsize(width=1100,height=600)
main_window.maxsize(width = 100,height=600)

#------------------- CREATING FRAMES -------------------

CheckButtonFrame = tk.Frame(main_window)
CheckButtonFrame.place(x=0,y=0,width=1100,height=400)
CheckButtonFrame.config(bg='light blue')

ButtonFrame = tk.Frame(main_window)
ButtonFrame.place(x=0,y=400,width=1100,height=200)
ButtonFrame.config(bg='light blue')

#------------------- DEFINING VARIABLES -------------------

MilkChoice = tk.IntVar()
HoneyChoice = tk.IntVar()
MilkChoice.set(1)

#------------------- CALLING DEFS -------------------

ScreenLabels()
ScreenButtons()
SetupCheckButtons()

tk.mainloop()






