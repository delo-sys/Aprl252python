from tkinter import *

root = Tk()

root.title("First GUI program")
root.geometry("500x500")

lblMessage=Label(root,text="Welocme to python GUI programming",borderwidth=2, relief="solid")
lblMessage.pack(ipadx=20, ipady=10, padx=20, pady=20, )

lblMessage2=Label(root,text="Using the tkinder module")
lblMessage2.pack()

txtName=Entry(root)
txtName.pack()

btnClickMe=Button(root, text="Click here")
btnClickMe.pack()


root.mainloop()