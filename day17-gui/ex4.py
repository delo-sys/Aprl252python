from tkinter import *
from tkinter import messagebox 
root = Tk()
root.title("Rectangle area")
root.geometry("300x300")


def getarea():
    side1=float(txtside1.get())
    side2=float(txtside2.get())
    area = side1*side2
    Message=f"Area of rectangle is {area}sq units"
    messagebox.showinfo("rectangle area",Message)

lblslide1=Label(root,text="Enter slide1")
lblslide1.pack()
txtside1=Entry(root)
txtside1.pack()

lblslide2=Label(root,text="Enter slide2")
lblslide2.pack()
txtside2=Entry(root)
txtside2.pack()

BtncalulateArea=Button(root, text="Calculate area",command=getarea)
BtncalulateArea.pack()
Btnquit=Button(root, text="exit", command=root.quit)
Btnquit.pack()
root.mainloop()