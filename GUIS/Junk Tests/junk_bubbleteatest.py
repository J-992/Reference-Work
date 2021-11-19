#Kevin Zheng
#12/5/2019
#Bubble Tea Benchmark

import tkinter as tk
from tkinter import ttk

def Quit():
        Window.destroy()

def Buttons():
        B_Quit=tk.Button(Summary,
                         text="Quit",
                         command=Quit)

        B_Quit.place(x=545,y=150)

        B_Order=tk.Button(Summary,
                          text="Order Summary",
                          command=Labels)
        B_Order.place(x=450,y=150)

        B_Reset=tk.Button(Summary,
                          text="Reset",
                          command=Reset)
        B_Reset.place(x=410,y=150)

def Reset():
    Resetsize=ttk.Label(Summary,
                        text="              ")
    Resetdrink=ttk.Label(Summary,
                        text="                                  ")
    ResetGj=ttk.Label(Summary,
                        text="              ")
    ResetT=ttk.Label(Summary,
                        text="              ")
    ResetC=ttk.Label(Summary,
                        text="              ")
    ResetWp=ttk.Label(Summary,
                        text="              ")
    ResetWc=ttk.Label(Summary,
                        text="              ")

    Resetsize.place(x=32.5,y=45)

    Resetdrink.place(x=10,y=80)
    ResetGj.place(x=10,y=100)
    ResetT.place(x=10,y=120)
    ResetC.place(x=10,y=140)
    ResetWp.place(x=10,y=160)
    ResetWc.place(x=10,y=180)
           
def Labels():
        OrderSummary=ttk.Label(Summary,
                          text="Order Summary:")                  
        drink=ttk.Label(Summary,
                        textvariable=Drink)
        size=ttk.Label(Summary,
                       textvariable=Size)        
        GJ=ttk.Label(Summary,
                     textvariable=Gj)
        Tt=ttk.Label(Summary,
                    textvariable=T)
        Cc=ttk.Label(Summary,
                    textvariable=C)
        WP=ttk.Label(Summary,
                     textvariable=Wp)
        WC=ttk.Label(Summary,
                     textvariable=Wc)      
        Line=ttk.Label(Summary,
                       text="------------------")
                                       
        OrderSummary.place(x=10,y=25)
        size.place(x=32.5,y=45)
        drink.place(x=10,y=80)
        GJ.place(x=290,y=25)
        Tt.place(x=370,y=25)
        Cc.place(x=440,y=25)
        WP.place(x=515,y=25)
        WC.place(x=600,y=25)
        Line.place(x=10,y=65)
       
def RadioButtons():
        Milktea=ttk.Radiobutton(Drink,
                                text="Milktea",
                                variable=Drink,
                                value="       Milktea")
        Brownsugarlatte=ttk.Radiobutton(Drink,
                                text="Brown sugar latte",
                                variable=Drink,
                                value="Brown sugar latte")
        Watermelonjuice=ttk.Radiobutton(Drink,
                                text="Watermelon Juice",
                                variable=Drink,
                                value="Watermelon Juice")
        Grassjelly=ttk.Radiobutton(Drink,
                                text="GrassJelly",
                                variable=Drink,
                                value="      GrassJelly")
        Large=ttk.Radiobutton(Size,
                              text="Large",
                              variable=Size,
                              value="Large")
        Medium=ttk.Radiobutton(Size,
                              text="Medium",
                              variable=Size,
                              value="Medium")
        Small=ttk.Radiobutton(Size,
                              text="Small",
                              variable=Size,
                              value="Small")
        Mini=ttk.Radiobutton(Size,
                              text="Mini",
                              variable=Size,
                              value="Mini")

        Milktea.place(x=10,y=10)
        Brownsugarlatte.place(x=10,y=40)
        Watermelonjuice.place(x=10,y=70)
        Grassjelly.place(x=10,y=100)
        Large.place(x=10,y=10)
        Medium.place(x=10,y=40)
        Small.place(x=10,y=70)
        Mini.place(x=10,y=100)
       
def Checkbuttons():
    GrassJelly=tk.Checkbutton(Gj,
                          text="GrassJelly",
                          variable=Gj)
    Tapioca=tk.Checkbutton(T,
                          text="Tapioca",
                          variable=T)
    Coconut=tk.Checkbutton(C,
                          text="Coconut",
                          variable=C)
    WhitePearls=tk.Checkbutton(Wp,
                          text="WhitePearls",
                          variable=Wp)
    Whippedcream=tk.Checkbutton(Wc,
                          text="Whippedcream",
                          variable=Wc)
   
    GrassJelly.place(x=0,y=0)
    Tapioca.place(x=0,y=0)
    Coconut.place(x=0,y=0)
    WhitePearls.place(x=0,y=0)
    Whippedcream.place(x=0,y=0)

Window=tk.Tk()
Window.title("Bubble Button 2.0")
Window.minsize(width=750,height=310)

Drink=tk.Frame(Window,width=160,height=150)
Size=tk.Frame(Window,width=150,height=150)
Gj=tk.Frame(Window,width=160,height=30)
T=tk.Frame(Window,width=160,height=60)
C=tk.Frame(Window,width=160,height=90)
Wp=tk.Frame(Window,width=160,height=120)
Wc=tk.Frame(Window,width=160,height=150)
Summary=tk.Frame(Window,width=700,height=200)


Drink.place(x=0,y=0)
Size.place(x=166,y=0)
Gj.place(x=332,y=10)
T.place(x=332,y=32.5)
C.place(x=332,y=55)
Wp.place(x=332,y=77.5)
Wc.place(x=332,y=100)
Summary.place(x=0,y=130)

Gj=tk.StringVar()
T=tk.StringVar()
C=tk.StringVar()
Wp=tk.StringVar()
Wc=tk.StringVar()
DDrink=tk.StringVar()
SSize=tk.StringVar()
AAddons=tk.StringVar()

Gj.set(1)
T.set(1)
C.set(1)
Wp.set(1)
Wc.set(1)

Buttons()
Labels()
RadioButtons()
Checkbuttons()

tk.mainloop()
