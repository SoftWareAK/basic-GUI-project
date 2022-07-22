import tkinter as tk
from tkinter import*

def sec1():
    print("Seçim 1",c1.get())

def sec2():
    print("Seçim 2",c2.get())
def rsec():
    print(r.get())




pencere=tk.Tk()
pencere.geometry("700x700")
pencere.title("basic byKURT's project")
pencere.configure(bg="light blue")

l=Label(text="PROJECT1",bg="blue",font= "Times  22 italic",fg="yellow")
l.place(x=250,y=20)

s=Scrollbar()
s.pack(side=RIGHT,fill=Y)

b=Button(bitmap="questhead")
b.place(x=38,y=10)
b=Button(bitmap="error")
b.place(x=66,y=10)
b=Button(bitmap="gray75")
b.place(x=94,y=10)
b=Button(bitmap="gray50")
b.place(x=122,y=10)
b=Button(bitmap="gray12")
b.place(x=500,y=10)
b=Button(bitmap="gray25")
b.place(x=528,y=10)
b=Button(bitmap="hourglass")
b.place(x=556,y=10)
b=Button(bitmap="info")
b.place(x=584,y=10)
b=Button(bitmap="question")
b.place(x=612,y=10)
b=Button(bitmap="warning")
b.place(x=150,y=10)



c1=IntVar()
c2=IntVar()

cb1=Checkbutton(text="secim1", variable=c1,onvalue=1,offvalue=0,command=sec1)
cb2=Checkbutton(text="secim2", variable=c2,onvalue=1,offvalue=0,command=sec2)
cb1.place(x=20,y=80)
cb2.place(x=100,y=80)


r=IntVar()



rb1=Radiobutton(text="Radıo1",variable=r,value=1,command=rsec)
rb2=Radiobutton(text="Radıo2",variable=r,value=2,command=rsec)
rb1.place(x=20,y=100)
rb2.place(x=100,y=100)

















pencere.mainloop()