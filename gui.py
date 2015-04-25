import Tkinter
from Tkinter import *
from utilities import *

top = Tkinter.Tk()
text=Text(top)
text.grid(row=2,column=1,rowspan=7,columnspan=2,sticky=E)
L1 = Label(top, text="Access token",width=13)
L1.grid(row=0,column=0,sticky=W)
E1 = Entry(top, bd =5,width=40)
E1.grid(row=0,column=1,sticky=W)

def callback():
    setAccessToken(E1.get())
    #execfile("utilities.py")
    
  
def method():    
    s1="Data retrieved"
    text.delete("1.0",END)
    text.insert(INSERT,s1)
    
    
B = Tkinter.Button(top, text ="get data",width=10, command = method)
b = Button(top, text="enter", width=15, command=callback)
b.grid(row=0,column=2,sticky=E)
B.grid(row=2,column=0,sticky=W)


def cluster():
    textm()
    
    
b1 = Button(top, text="clusterpages", width=10, command=cluster)
b1.grid(row=3,column=0,sticky=W)
c1=""
c2=""
c3=""
id1=0


def textm():
    c1="4 clusters are formed after clustering"
    text.delete("1.0",END)
    text.insert(INSERT,c1)
    
    
def influence():
    c2="The influencers are A,B,C"
    text.delete("1.0",END)
    text.insert(INSERT,c2)
    
    
b2= Button(top, text="Find influencers", width=10, command=influence)


def influencers():
    c3="The influencers of this page are X,Y,Z"
    global id1
    id1=E2.get()
    text.delete("1.0",END)
    text.insert(INSERT,c3)
    
    
def button4():
    c2="Button4"
    text.delete("1.0",END)
    text.insert(INSERT,c2)
    
b4= Button(top, text="button 4", width=10, command=button4)

def button5():
    c2="button5"
    text.delete("1.0",END)
    text.insert(INSERT,c2)
    
b5= Button(top, text="button 5", width=10, command=button5)

def button6():
    c2="button6"
    text.delete("1.0",END)
    text.insert(INSERT,c2)
    
b6= Button(top, text="button6", width=10, command=button6)

def button7():
    c2="button7"
    text.delete("1.0",END)
    text.insert(INSERT,c2)
    
b7= Button(top, text="button7", width=10, command=button7)

b4.grid(row=4,column=0,sticky=W)
b5.grid(row=5,column=0,sticky=W)
b6.grid(row=6,column=0,sticky=W)
b7.grid(row=7,column=0,sticky=W)

b3= Button(top, text="Find influencers for my page", width=25, command=influencers)
L2 = Label(top, text="page id",width=15)
E2 = Entry(top, bd =5,width=40)
b3.grid(row=9,column=2,sticky=W)
E2.grid(row=9,column=1,sticky=W)
L2.grid(row=9,column=0,sticky=W)
b2.grid(row=8,column=0,sticky=W)
top.mainloop()
