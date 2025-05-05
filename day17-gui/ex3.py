from tkinter import *
from tkinter import messagebox
def displayMessage():
    messagebox.showinfo("welcome", "Hello, welcome to Python GUI programming!")
root = Tk()
BtnclickMe=Button(root, text="Click here",command=displayMessage)
BtnclickMe.pack()
Btnquit=Button(root, text="exit", command=root.quit)
Btnquit.pack()
root.mainloop()