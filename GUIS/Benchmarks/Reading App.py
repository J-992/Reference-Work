'''
jaffer razavi
nov 27 2019
benchmark button
'''

import tkinter as tk
from tkinter import ttk



def QuitButton():
    main_window.destroy()

def Name():
    name=tk.Label(NameFrame,text="Jaffer Razavi",
                  fg = 'black',
                  bg = 'gray',
                  font = 'Arial 50 bold')
    name.place(x=0,y=0,width = 950, height = 50)

def FavButton():
    fave = tk.Label(InfoFrame,text="""
After The Flood
by Robert Polidori

Eragon
by Christopher Paolini

A Brief History of Time
by Stephen Hawking
""",
                      fg = 'green2',
                      bg = 'gray',
                      bd = 2,
                      font = 'Helvetica 20 bold')
    fave.place(x=0,y=0,width=950,height=300)

def SuggestButton():
    sug = tk.Label(InfoFrame,text="""Harry Potter Series
by JK Rowling

Eragon
by Christopher Paolini

The Happiness Project
by Gretchen Rubin

The Martian
by Andy Weir
""",
                      fg = 'green2',
                      bg = 'gray',
                      bd = 2,
                      font = 'Helvetica 20 bold')
    sug.place(x=0,y=0,width=950,height=300)

def MovieButton():
    mov = tk.Label(InfoFrame,text="""
Harry Potter Series

Eragon

The Giver

The Maze Runner

The Hobbit

""",
                      fg = 'green2',
                      bg = 'gray',
                      bd = 2,
                      font = 'Helvetica 20 bold')
    mov.place(x=0,y=0,width=950,height=300)
  
def main():
    Name()
    B_Fav = tk.Button(main_window,
                      text = "Favourites",
                      fg ='red',
                      font = 'Helvetica 20 bold italic',
                      command = FavButton)
    B_Sug = tk.Button(main_window,
                      text = "Suggestions",
                      fg ='red',
                      font = 'Helvetica 20 bold italic',
                      command = SuggestButton)
    B_Movie = tk.Button(main_window,
                       text = "Movies",
                       fg = "red",
                       font = 'Helvetica 20 bold italic',
                       command = MovieButton)
    B_Quit = tk.Button(main_window,
                       text = "Quit",
                       fg = "red",
                       font = 'Helvetica 20 bold italic',
                       command = QuitButton)

    FrameClr= tk.Label(InfoFrame, bg = 'gray')
    FrameClr.place(x=0,y=0,width=950,height=600)
    
    B_Sug.place(x=250,y=520,width=250)
    B_Fav.place(x=0,y=520,width=250)
    B_Quit.place(x=750,y=520,width=250)
    B_Movie.place(x=500,y=520,width=250)

main_window = tk.Tk()
main_window.title('Reading App')
main_window.minsize(width = 1000, height = 600)
main_window.configure(bg = 'gray')

InfoFrame = ttk.Frame(master=main_window,width=560,height=300)
InfoFrame.place(x=20,y=100,width=950)

NameFrame = ttk.Frame(master=main_window,width=560,height=50)
NameFrame.place(x=20,y=20,width=950,height=50)

main()






