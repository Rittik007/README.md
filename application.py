from tkinter import *

def show():
    lb2 = float(txt1.get())
    lb3 = float(txt2.get())
    res = lb2 + lb3
    lb4.configure(text=res)

mainframe=Tk()
mainframe.title("My Calculator")
mainframe.resizable()
frame=Frame(mainframe,bg="light blue")
frame2=Frame(mainframe,bg="light blue")
frame.pack()
frame2.pack()
lb=Label(frame,text="My Application",bg="light blue")
lb.pack()
lb2=Label(frame2,text="Enter your first number")
lb3=Label(frame2,text="Enter your second numbber")
lb4=Label(frame2,text="result :-",bg="light blue")
txt1=Entry(frame2)
txt2=Entry(frame2)

btn=Button(frame2,text="submit",command=show)
lb2.grid(row=0,column=0)
lb3.grid(row=1,column=0)
lb4.grid(row=2,column=0)
txt1.grid(row=0,column=1)
txt2.grid(row=1,column=1)

btn.grid(row=2,column=1)

mainframe.mainloop()