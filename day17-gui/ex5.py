from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("degree to radian")

root.geometry("300x300")
def getradian():
    degree=float(txtdegree.get())
    radian=degree*(3.14/180)
    Message=f"Radian is {radian}"
    messagebox.showinfo("degree to radian",Message)


lbldegree=Label(root,text="Enter degree")
lbldegree.pack()   
txtdegree=Entry(root)
txtdegree.pack()

Btncalulatedegree=Button(root, text="Calculate degree",command=getradian)
Btncalulatedegree.pack()
Btnquit=Button(root, text="exit", command=root.quit)
Btnquit.pack()
root.mainloop()