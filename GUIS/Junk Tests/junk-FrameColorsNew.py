#importing tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk

#The normal background color displayed behind the label and indicator.
def main():
    frameTop=tk.Frame(Window1,width=600,height=100,background="red") #FrameTop will be red
    frameMiddle=tk.Frame(Window1,width=600,height=50,background="blue") #FrameMiddle will be bue
    frameBottom=tk.Frame(Window1,width=600,height=150,background="yellow") #FrameBottom will be yellow

    frameTop.place(x=0,y=0)
    frameBottom.place(x=0,y=150)



#Creating Window
Window1=tk.Tk()
Window1.title("Frame Tutorial")
Window1.minsize(width=600,height=300)

#Calling out the function
main()
