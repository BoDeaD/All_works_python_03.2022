from tkinter import *
from math import *
root = Tk()
root.geometry("260x370")
def Module_click():
    a=float(ent1.get())
    ent1.delete(0, END)
    if a>=0:
        c=abs(a)
        ent1.insert(END, int(c))
    if a<0:
        c=abs(a)
        ent1.insert(END, int(c))
        
def Radical_click():
    a=float(ent1.get())
    ent1.delete(0, END)
    if a>=0:
        c=sqrt(a)
        ent1.insert(END,int(c))
    if a<0:
        c=abs(a)
        c=sqrt(c)
        ent1.insert(END,int(c))
        
def Equ_click():
    global a, b
    c=float(ent1.get())
    ent1.delete(0, END)
    if b=="+":
        a=a+c
        def result(a):
            if a==int(a):
                ent1.insert(END,int(a))
            else:
                ent1.insert(END,a)
        result(a)
    if b=="-":
        a=a-c
        def result(a):
            if a==int(a):
                ent1.insert(END,int(a))
            else:
                ent1.insert(END,a)
        result(a)
    if b=="*":
        a=a*c
        def result(a):
            if a==int(a):
                ent1.insert(END,int(a))
            else:
                ent1.insert(END,a)
        result(a)
    if b=="/":
        if c!=0:
            a=a/c
            def result(a):
             if a==int(a):
                ent1.insert(END,int(a))
             else:
                ent1.insert(END,a)
        else:
            ent1.insert(END,"помилка")
        result(a)
    
def Delen_click():
    global a, b
    a=float(ent1.get())
    b="/"
    ent1.delete(0, END)
    
def Umnot_click():
    global a, b
    a=float(ent1.get())
    b="*"
    ent1.delete(0, END)
    
def Minus_click():
    global a, b
    if ent1.get()=="":
        ent1.insert(END,"-")
    else:
     a=float(ent1.get())
     b="-"
     ent1.delete(0, END)
    
def Plus_click():
    global a, b
    a=float(ent1.get())
    b="+"
    ent1.delete(0, END)
    
def C_click():
    ent1.delete(0,END)
    
def B7_click():
    ent1.insert(END, "7")
    
def B8_click():
    ent1.insert(END, "8")
    
def B9_click():
    ent1.insert(END, "9")
    
def B4_click():
    ent1.insert(END, "4")
    
def B5_click():
    ent1.insert(END, "5")
    
def B6_click():
    ent1.insert(END, "6")
    
def B1_click():
    ent1.insert(END, "1")
    
def B2_click():
    ent1.insert(END, "2")
    
def B3_click():
    ent1.insert(END, "3")
    
def B0_click():
    ent1.insert(END, "0")
    
ent1 = Entry(justify = "right",font = "14")
ent1.place(x=20,y=20,width=220,height=30)
#---
BC1=Button(text="C", font="14",command=C_click)
BC1.place(x=20, y=70, width=40, height=40)
#---
Equ=Button(text="=", font="14",command=Equ_click )
Equ.place(x=200, y=70, width=40, height=40)
#---
B7 = Button(text = "7", font = "14",command=B7_click)
B7.place(x=20,y=130,width=40,height=40)
#---
B8=Button(text="8", font="14",command=B8_click)
B8.place(x=80, y=130, width=40, height=40)
#---
B9=Button(text="9", font="14",command=B9_click)
B9.place(x=140, y=130, width=40, height=40)
#---
Delen=Button(text="/", font="14",command = Delen_click)
Delen.place(x=200, y=130, width=40, height=40)
#---
B4=Button(text="4", font="14",command=B4_click)
B4.place(x=20, y=190, width=40, height=40)
#---
B5=Button(text="5", font="14",command=B5_click)
B5.place(x=80, y=190, width=40, height=40)
#---
B6=Button(text="6", font="14",command=B6_click)
B6.place(x=140, y=190, width=40, height=40)
#---
Multiply=Button(text="*", font="14",command = Umnot_click)
Multiply.place(x=200, y=190, width=40, height=40)
#---
B1=Button(text="1", font="14",command=B1_click)
B1.place(x=20, y=250, width=40, height=40)
#---
B2=Button(text="2", font="14",command=B2_click)
B2.place(x=80, y=250, width=40, height=40)
#---
B3=Button(text="3", font="14",command=B3_click)
B3.place(x=140, y=250, width=40, height=40)
#---
Minus=Button(text="-", font="14",command = Minus_click)
Minus.place(x=200, y=250, width=40, height=40)
#---
B0=Button(text="0", font="14",command=B0_click)
B0.place(x=20, y=310, width=100, height=40)
#---
Plus=Button(text="+", font="14",command=Plus_click )
Plus.place(x=200, y=310, width=40, height=40)
#---
Point=Button(text=".", font="14")
Point.place(x=140, y=310, width=40, height=40)
#---
Module=Button(text="|x|", font="14", command=Module_click)
Module.place(x=140, y=70, width=40, height=40)
#---
img=PhotoImage(file='radical.png')
Radical=Button(image=img, command=Radical_click)
Radical.place(x=80, y=70, width=40, height=40)
