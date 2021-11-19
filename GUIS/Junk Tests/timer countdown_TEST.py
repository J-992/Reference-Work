import time
import tkinter as tk


def label():
    timerlabel = tk.Label(main_window,text = timing)
    a=120
    for i in range (120):
        
        a = a-1
        timerlabel.place(x=250,y=250)
        timing.set(a)
        #time.sleep(1)
        
    
    




main_window = tk.Tk()
main_window.title('Timer')
main_window.minsize(width=500,height=500)
main_window.maxsize(width=500,height=500)

timing=tk.IntVar()
label()
tk.mainloop()


