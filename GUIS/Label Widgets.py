#jaffer razavi
#nov 22 2019
#window widget

import tkinter as tk

def main():
    Window2=tk.Tk()
    Window2.minsize(width=500,height=200)
    Window2.title("Second Window")
    Window2.configure(bg="yellow")
    
    Intro = tk.Label (Window2, text = 'Hello World',
                      fg = 'red3',
                      bg = 'yellow',
                      font = "Helvetica 10 bold italic")
    
    Intro.place(x=10,y=10,width=200,height=25)
    
    tk.mainloop()

main()
