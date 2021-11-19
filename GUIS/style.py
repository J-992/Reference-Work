#Additional information from Alex...
import tkinter as tk
from tkinter import ttk #importing files

window=tk.Tk() #Creating the window

style=ttk.Style() #Creating style element
style.configure('RadioButtonStyle.TRadiobutton', #Names the style. Needs to end with: .TRadiobutton
background="blue", #Setting the background colour
foreground='white') #Sets forground colour (Colour of the text)

button=ttk.Radiobutton(window, text = "wow so amazing", style = 'RadioButtonStyle.TRadiobutton') # Creating Button with style
button.place(x=0,y=0) #Placing variable
tk.mainloop()
