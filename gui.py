import Tkinter
import fileinput
from Tkinter import *
import subprocess

import os
top = Tkinter.Tk()
text=Text(top)
text.grid(row=2,column=1,rowspan=10,columnspan=2,sticky=E)
scr = Scrollbar(top)
scr.config(command=text.yview) 
text.config(yscrollcommand=scr.set)
scr.grid(row=2,column=3,sticky=E,ipady=165,rowspan=10)
L1 = Label(top, text="Access token",width=18)
L1.grid(row=0,column=0,sticky=W)
E1 = Entry(top, bd =5,width=40)
E1.grid(row=0,column=1,sticky=W)

def callback():
    file1=open("utilities.py")
    file2=open("new.py","w")
    for line in file1.readlines():
        if 'access_token = ' in line:
            line='access_token = ' +'"'+str(E1.get())+'"'+'\n'
        file2.write(line)
    file2.close()
    os.remove("utilities.py")
    os.rename("new.py","utilities.py")
    text.insert(INSERT, "Access token saved.")
    #execfile("utilities.py")
    
  
def method():    
    child = subprocess.Popen(['python', '-u', 'getData.py'], stdout=subprocess.PIPE)
    text.delete("1.0",END)
    for line in iter(child.stdout.readline, ''):
        text.insert(INSERT, line)
        text.see(END)
        text.update_idletasks()
    child.stdout.close()
    child.wait()
       
B = Tkinter.Button(top, text ="Find Friends",width=15, command = method)
b = Button(top, text="enter", width=15, command=callback)
b.grid(row=0,column=2,sticky=E)
B.grid(row=2,column=0,sticky=W)

    
c1=""
c2=""
c3=""
id1=0

        
def influence():
    child = subprocess.Popen(['python', '-u', 'getFullInfluenceScore.py'], stdout=subprocess.PIPE)
    text.delete("1.0",END)
    for line in iter(child.stdout.readline, ''):
        text.insert(INSERT, line)
        text.see(END)
        text.update_idletasks()
    child.stdout.close()
    child.wait()
    child = subprocess.Popen(['python', '-u', 'clusterLevelResults.py'], stdout=subprocess.PIPE)
    text.delete("1.0",END)
    for line in iter(child.stdout.readline, ''):
        text.insert(INSERT, line)
        text.see(END)
        text.update_idletasks()
    child.stdout.close()
    child.wait()

    
b2= Button(top, text="Find influencers", width=15, command=influence)


def influencers():
    file1=open("utilities.py")
    file2=open("new.py","w")
    for line in file1.readlines():
        if 'PID = ' in line:
            line='PID = ' +str(E2.get())+'\n'
        file2.write(line)
    file2.close()
    os.remove("utilities.py")
    os.rename("new.py","utilities.py")

    execfile('getResults.py')
    text.delete("1.0",END)
    out = open('tempfile.txt', 'r')
    numLines = int(out.readline())
    for line in range(numLines):
    	text.insert(INSERT, line)

    '''
    child = subprocess.Popen(['python', '-u', 'getResults.py'], stdout=subprocess.PIPE)
    text.delete("1.0",END)
    for line in iter(child.stdout.readline, ''):
        text.insert(INSERT, line)
        text.see(END)
        text.update_idletasks()
    child.stdout.close()
    child.wait()
    '''

def get_likes_button():
#    c2="Button4"
    child = subprocess.Popen(['python', '-u', 'getLikes.py'], stdout=subprocess.PIPE)
    text.delete("1.0",END)
    for line in iter(child.stdout.readline, ''):
        text.insert(INSERT, line)
        text.see(END)
        text.update_idletasks()
    child.stdout.close()
    child.wait()
#    text.delete("1.0",END)
#    text.insert(INSERT,c2)
    
b4= Button(top, text="Get Likes", width=15, command=get_likes_button)

def getPages_button():
#    c2="button5"
#    text.delete("1.0",END)
#    text.insert(INSERT,c2)
    child = subprocess.Popen(['python', '-u', 'getPages.py'], stdout=subprocess.PIPE)
    text.delete("1.0",END)
    for line in iter(child.stdout.readline, ''):
        text.insert(INSERT, line)
        text.see(END)
        text.update_idletasks()
    child.stdout.close()
    child.wait()
    
b5= Button(top, text="Get Page Posts", width=15, command=getPages_button)

def button6():
    child = subprocess.Popen(['python', '-u', 'getPageData2.py'], stdout=subprocess.PIPE)
    text.delete("1.0",END)
    for line in iter(child.stdout.readline, ''):
        text.insert(INSERT, line)
        text.see(END)
        text.update_idletasks()
    child.stdout.close()
    child.wait()
#    c2="button6"
#    text.delete("1.0",END)
#    text.insert(INSERT,c2)
    
    
b6= Button(top, text="Remove Stopwords", width=15, command=button6)
L3 = Label(top, text="No.of clusters",width=18)
E3 = Entry(top, bd =5,width=20)
def number():
    file1=open("utilities.py")
    file2=open("new.py","w")
    for line in file1.readlines():
        if 'KVAL = ' in line:
            line='KVAL = '+str(E3.get())+'\n'
        file2.write(line)
    file2.close()
    os.remove("utilities.py")
    os.rename("new.py","utilities.py")

    child = subprocess.Popen(['python', '-u', 'kmeans.py'], stdout=subprocess.PIPE)
    text.delete("1.0",END)
    for line in iter(child.stdout.readline, ''):
        text.insert(INSERT, line)
        text.see(END)
        text.update_idletasks()
    child.stdout.close()
    child.wait()

    child = subprocess.Popen(['python', '-u', 'pageAnalytics.py'], stdout=subprocess.PIPE)
    for line in iter(child.stdout.readline, ''):
        text.insert(INSERT, line)
        text.see(END)
        text.update_idletasks()
    child.stdout.close()
    child.wait()

b1 = Button(top, text="Cluster Pages", width=15, command=number)
b1.grid(row=8,column=0,sticky=W)
L3.grid(row=6,column=0,sticky=W)
E3.grid(row=7,column=0,sticky=W)
#def button7():
#    c2="button7"
#    text.delete("1.0",lEND)
#    text.insert(INSERT,c2)
    
#b7= Button(top, text="button7", width=10, command=button7)

b4.grid(row=3,column=0,sticky=W)
b5.grid(row=4,column=0,sticky=W)
b6.grid(row=5,column=0,sticky=W)
#b7.grid(row=7,column=0,sticky=W)

b3= Button(top, text="Find Influencers for a Page", width=25, command=influencers)
L2 = Label(top, text="Page ID",width=18)
E2 = Entry(top, bd =5,width=40)
b3.grid(row=12,column=2,sticky=W)
E2.grid(row=12,column=1,sticky=W)
L2.grid(row=12,column=0,sticky=W)
b2.grid(row=11,column=0,sticky=W)

def community():
    child = subprocess.Popen(['python', '-u', 'getPartialInfluenceScore.py'], stdout=subprocess.PIPE)
    text.delete("1.0",END)
    for line in iter(child.stdout.readline, ''):
        text.insert(INSERT, line)
        text.see(END)
        text.update_idletasks()
    child.stdout.close()
    child.wait()

def contribution():
    child = subprocess.Popen(['python', '-u', 'clusterContribution.py'], stdout=subprocess.PIPE)
    text.delete("1.0",END)
    for line in iter(child.stdout.readline, ''):
        text.insert(INSERT, line)
        text.see(END)
        text.update_idletasks()
    child.stdout.close()
    child.wait()
    
b7= Button(top, text="Open Community Score", width=15, command=community)
b7.grid(row=9,column=0,sticky=W)
b8= Button(top, text="Cluster Contribution", width=15, command=contribution)
b8.grid(row=10,column=0,sticky=W)
top.mainloop()
