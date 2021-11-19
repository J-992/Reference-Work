

#Making Cursors

import tkinter as tk

def QuitButton():
    main_window.destroy()

def main():
    B_Quit = tk.Button(main_window,
                       text = "Quit",
                       fg = "black",
                       font = 'Helvetica 30 bold italic', \
                       cursor = "X_cursor",
                       command = QuitButton)

    B_Quit.place(x=750,y=520,width=250)


main_window = tk.Tk()
main_window.minsize(width = 1000, height = 600)
main_window.configure(bg = 'gray', \
                          cursor="circle")
main()
tk.mainloop()

