#jaffer Razavi
#Check Buttons
#dec 9 2019
import tkinter as tk
from tkinter import ttk

def QuitButton():
      main_window.destroy()

def SummaryButton():
      Milk = 'Milk: '+str(MilkChoice.get())
      Honey = 'Honey: '+str(HoneyChoics.get())
      MilkChoiceLabel = tk.Label(CheckButtonFrame,text = Milk)
      HoneyChoiceLabel = tk.Label(CheckButtonFrame,text = Honey)
      MilkChoiceLabel.place(x=650,y=200)
      HoneyChoiceLabel.place(x=650,y=200)
      
def ScreenLabels():
      Title = tk.Label(CheckButtonFrame,text = 'Title')
      Title.place(x=0,y=0)

def ScreenButtons():
      B_Quit = tk.Button(ButtonFrame, text = 'Quit', command = QuitButton)

def SetupCheckButtons():
      MilkCheckButton = tk.Checkbutton(CheckButtonFrame,text = 'Milk',variable = MilkChoice)
      HoneyCheckButton = tk.Checkbutton(CheckButtonFrame,text = 'Honey',variable = HoneyChoice)
      MilkCheckButton.place(x=400,y=100,width=150,height=25)
      HoneyCheckButton.place(x=700,y=100,width=150,height=25)

main_window = tk.Tk()
main_window.title('CheckButtons')
main_window.minsize(width=1100,height=600)
main_winow.maxsize(width = 100,height=600)
