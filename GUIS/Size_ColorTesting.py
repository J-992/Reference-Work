#jaffer razavi
#nov 22 2019
#window widget

import tkinter as tk

def main():
    Window2=tk.Tk()
    Window2.title("Second Window")
    Window2.minsize(width=500,height=300)

    Intro = tk.Label (Window2, text = "Label1",
                      fg = 'white',
                      bg = 'brown',
                      font = "Helvetica 16 bold")
    Intro.place(x=10,y=40,width=200,height=25)

    Intro2 = tk.Label (Window2, text = "Label2",
                      fg = 'blue',
                      bg = 'orange',
                      font = "Helvetica 16 bold")
    Intro2.place(x=10,y=65,width=200,height=25)

    Intro3 = tk.Label (Window2, text = "Label3",
                      fg = 'red',
                      bg = 'green',
                      font = "Helvetica 16 bold")
    Intro3.place(x=10,y=90,width=200,height=25)

    Intro4 = tk.Label (Window2, text = "Label4",
                      fg = 'purple',
                      bg = 'black',
                      font = "Helvetica 16 bold")
    Intro4.place(x=10,y=115,width=200,height=25)

    Intro5 = tk.Label (Window2, text = "Label5",
                      fg = 'yellow',
                      bg = 'navy',
                      font = "Helvetica 16 bold")
    Intro5.place(x=10,y=140,width=200,height=25)

    Intro6 = tk.Label (Window2, text = "Label6",
                      fg = 'blanched almond',
                      bg = 'silver',
                      font = "Helvetica 16 bold")
    Intro6.place(x=10,y=165,width=200,height=25)
    tk.mainloop()

main()
