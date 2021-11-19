#Kevin Zheng
#12/5/2019
#Bubble Tea Benchmark

import tkinter as tk
from tkinter import ttk

#Definitions
def Quit():
        Window.destroy()

def Buttons():
        B_Quit=tk.Button(Summary,
                         text="Quit",
                         fg="blue",
                         command=Quit)

        B_Order=tk.Button(Summary,
                          text="Order Summary",
                          fg="red",
                          command=summary)

        B_Request=tk.Button(Summary,
                           text="Special request",
                           fg="orange",
                           command=Request)

        B_send=tk.Button(Summary,
                         text="Send request",
                         fg="purple",
                         command=sppecial)
        B_Reset=tk.Button(Summary,
                          text="Reset",
                          fg="green",
                          command=Reset)

        B_Quit.place(x=475,y=150)
        B_Order.place(x=380,y=150)
        B_Reset.place(x=340,y=150)
        B_Request.place(x=510,y=150)
        B_send.place(x=600,y=150)

def Request():
        Rq=tk.Label(Summary,text="Request:")
        Rq.place(x=10,y=150)
        special=tk.Entry(Summary,textvariable=request)
        special.place(x=60,y=150)

def sppecial():
        sspecial=(request.get())

        ssspecial=tk.Label(Summary,text=sspecial)
        ssspecial.place(x=10,y=120)
       
def summary():
       DDDrink=(drink.get())
       SSSize=(size.get())
       Gr="+",str(GJ.get())
       Ta="+",str(Tt.get())
       Co="+",str(Cc.get())
       Wh="+",str(WP.get())
       Whi="+",str(WC.get())

       DDrink=tk.Label(Summary,text= "")
       SSize=tk.Label(Summary,text= "")
       Extra=tk.Label(Summary,text= "")

       DDrink.place(x=32.5,y=40)
       SSize.place(x=10,y=80)
       Extra.place(x=0,y=70)

   
       if(GJ.get()==1):
                      gj="with Grass Jelly "
       else:
                      gj=""
       if(Tt.get()==1):
                      t="with Tapioca "
       else:
                      t=""
       if(Cc.get()==1):
                      c="with Coconut "
       else:
                      c=""
       if(WP.get()==1):
                      wp="with White Pearls "
       else:
                      wp=""
       if(WC.get()==1):
                      wc="with Whipped Cream "
       else:
                      wc=""

       EXTra=gj+t+c+wp+wc

       ddDrink=tk.Label(Summary,text=DDDrink)
       ssSize=tk.Label(Summary,text=SSSize)
       EXtra=tk.Label(Summary,text=EXTra)

       ddDrink.place(x=10,y=80)
       ssSize.place(x=32.5,y=50)
       EXtra.place(x=10,y=100)
                         
def Reset():
    drink.set(0)
    size.set(0)
    GJ.set(0)
    Tt.set(0)
    Cc.set(0)
    WP.set(0)
    WC.set(0)
   
    Resetsize=ttk.Label(Summary,
                        text="                                                  ")
    Resetdrink=ttk.Label(Summary,
                        text="                                                                     ")
    ResetExtra=ttk.Label(Summary,
                        text="                                             ")
    ResetRequest=ttk.Label(Summary,text="                                                                                                                                                                                                                        ")
   
    ResetRequest.place(x=10,y=120)                      
    Resetsize.place(x=32.5,y=50)
    Resetdrink.place(x=10,y=80)
    ResetExtra.place(x=10,y=100)
           
def Labels():
        OrderSummary=ttk.Label(Summary,
                          text="Order Summary:")                  
   
        Line=ttk.Label(Summary,
                       text="------------------")
                                       
        OrderSummary.place(x=10,y=25)

        Line.place(x=10,y=65)
       
def RadioButtons():
        Milktea=ttk.Radiobutton(Drink,
                                text="Milktea",
                                variable=drink,
                                value="       Milktea")
        Brownsugarlatte=ttk.Radiobutton(Drink,
                                text="Brown sugar latte",
                                variable=drink,
                                value="Brown sugar latte")
        Watermelonjuice=ttk.Radiobutton(Drink,
                                text="Watermelon Juice",
                                variable=drink,
                                value="Watermelon Juice")
        Grassjelly=ttk.Radiobutton(Drink,
                                text="GrassJelly",
                                variable=drink,
                                value="      GrassJelly")
        Large=ttk.Radiobutton(Size,
                              text="Large",
                              variable=size,
                              value="Large")
        Medium=ttk.Radiobutton(Size,
                              text="Medium",
                              variable=size,
                              value="Medium")
        Small=ttk.Radiobutton(Size,
                              text="Small",
                              variable=size,
                              value="Small")
        Mini=ttk.Radiobutton(Size,
                              text="Mini",
                              variable=size,
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
                          variable=GJ)
    Tapioca=tk.Checkbutton(T,
                          text="Tapioca",
                          variable=Tt)
    Coconut=tk.Checkbutton(C,
                          text="Coconut",
                          variable=Cc)
    WhitePearls=tk.Checkbutton(Wp,
                          text="WhitePearls",
                          variable=WP)
    Whippedcream=tk.Checkbutton(Wc,
                          text="Whippedcream",
                          variable=WC)
   
    GrassJelly.place(x=0,y=0)
    Tapioca.place(x=0,y=0)
    Coconut.place(x=0,y=0)
    WhitePearls.place(x=0,y=0)
    Whippedcream.place(x=0,y=0)

#Creating window
Window=tk.Tk()
Window.title("Bubble Button 2.0")
Window.minsize(width=680,height=310)

Drink=tk.Frame(Window,width=160,height=150)
Size=tk.Frame(Window,width=150,height=150)
Gj=tk.Frame(Window,width=160,height=30)
T=tk.Frame(Window,width=160,height=60)
C=tk.Frame(Window,width=160,height=90)
Wp=tk.Frame(Window,width=160,height=120)
Wc=tk.Frame(Window,width=160,height=150)
Summary=tk.Frame(Window,width=680,height=200)


Drink.place(x=0,y=0)
Size.place(x=166,y=0)
Gj.place(x=332,y=10)
T.place(x=332,y=32.5)
C.place(x=332,y=55)
Wp.place(x=332,y=77.5)
Wc.place(x=332,y=100)
Summary.place(x=0,y=130)

request=tk.StringVar()
drink=tk.StringVar()
size=tk.StringVar()
special=tk.StringVar()
GJ=tk.IntVar()
Tt=tk.IntVar()
Cc=tk.IntVar()
WP=tk.IntVar()
WC=tk.IntVar()

Buttons()
Labels()
RadioButtons()
Checkbuttons()

tk.mainloop()
