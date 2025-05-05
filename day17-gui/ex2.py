from tkinter import *

root = Tk()

root.title("First GUI program")
root.geometry("500x500")

topFrame=Frame(root)
bottomFrame = Frame(root)

lblMessage=Label(topFrame,text="Welocme to python GUI programming",borderwidth=2, relief="solid")
lblMessage.pack(ipadx=20, ipady=10, padx=20, pady=20, )

lblMessage2=Label(topFrame,text="Using the tkinder module")
lblMessage2.pack()

txtName=Entry(bottomFrame)
txtName.pack()

btnClickMe=Button(bottomFrame, text="Click here")
btnClickMe.pack()
topFrame.pack(side="top")
bottomFrame.pack(side="top")

chkTickme=Checkbutton(bottomFrame, text="on/off") 
chkTickme.pack()


root.mainloop()