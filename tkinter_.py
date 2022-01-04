from tkinter import *
click=0

def clicker(event):
    global click
    click+=1
    lbl.configure(text=click)
    if click==100:
       click=0
def clicker_minus(event):
    global click
    click-=1
    lbl.configure(text=click)
    if click==-100:
       click=0
def txt_to_lbl(event):
    #pass
    text=txt.get()#from Entry to text
    lbl.configure(text=text)
    txt.delete(0,END)
def valik():
    valik_=var.get()
    lbl.configure(text=valik_)
    txt.insert(0,valik_)        

aken=Tk()
aken.title("Akna nimetus")
aken.geometry("1920x1080")
nupp=Button(aken,text="Vajuta\nNuppu",font="Arial 20",fg="black",bg="white",height=4,width=20,relief=RAISED)#GROOVE, #SUNKEN
nupp.bind("<Button-1>",clicker)
nupp.bind("<Button-3>",clicker_minus)
lbl=Label(aken,text="...",height=4,width=20,font="Arial 20",fg="white",bg="black")
txt=Entry(aken,font="Arial 20",fg="white",bg="black",justify=RIGHT)
txt.bind("<Return>",txt_to_lbl)#Enter
i1=PhotoImage(file="kot.gif")
i2=PhotoImage(file="kot2.gif")
i3=PhotoImage(file="kot3.gif")
var=StringVar()
var.set("Üks")
r1=Radiobutton(aken,image=i1,variable=var,value="Üks",command=valik)
r2=Radiobutton(aken,image=i2,variable=var,value="Kaks",command=valik)
r3=Radiobutton(aken,image=i3,variable=var,value="Kolm",command=valik)


lbl.pack()
nupp.pack(side=TOP)#side=LEFT,TOP,RIGHT
txt.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)
aken.mainloop()
