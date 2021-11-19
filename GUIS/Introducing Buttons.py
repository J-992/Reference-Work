'''
jaffer razavi
nov 26 2019
buttons
'''

import tkinter as tk
from tkinter import ttk

def QuitButton():
    main_window.destroy()



def SloganButton():
    slogan = tk.Label(frame,text="Don't cry because its over, \n Smile because it happened",
                      fg = 'red3',
                      bg = 'pink',
                      font = 'Helvetica 10 bold italic')
    slogan.place(x=10,y=10,width=200,height=35)

 

def main():
    B_Slogan = tk.Button(main_window,
                         text = "Quote",
                         fg ='red',
                         command = SloganButton)
    B_Quit = tk.Button(main_window,
                       text = "Quit",
                       fg = "red",
                       command = QuitButton)
    B_Slogan.place(x=20,y=400)
    B_Quit.place(x=120,y=400)
 

#------------------------------------------------------------------------------------------------------

main_window = tk.Tk()
main_window.title('Introducing Buttons')
main_window.minsize(width=500,height=500)
frame = ttk.Frame(master=main_window,width=500,height=500)
frame.place(x=0,y=0)

main()
