from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("mile to gallon")

root .geometry("300x300")

def getgallon():
    mile=float(txtmile.get())
    gallons=float(txtgallon.get())
    mpg=mile/gallons
    Message=f"mpg is {mpg}"
    messagebox.showinfo("mile to gallon",Message)

lblmile=Label(root,text="Enter mile")
lblmile.pack()   
txtmile=Entry(root)
txtmile.pack()
lblgallon=Label(root,text="Enter gallon")
lblgallon.pack()   
txtgallon=Entry(root)
txtgallon.pack()


Btncalulategallon=Button(root, text="Calculate mile",command=getgallon)
Btncalulategallon.pack()
Btnquit=Button(root, text="exit", command=root.quit)
Btnquit.pack()
root.mainloop()