import sqlite3
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
conn=sqlite3.connect("window.db")
c=conn.cursor()


def login():
    conn=sqlite3.connect("window.db")
    c=conn.cursor()
    username = txtusername.get()
    password = txtpassword.get()
    if username and password:
        messagebox.showinfo(f"Username: {username}, Password: {password}")
        querystring = "INSERT INTO account VALUES (?, ?)"
        c.execute(querystring, (username, password))
        conn.commit()
        conn.close()
    else:
        messagebox.showinfo("Please enter both username and password.")

def createAccount():
    conn=sqlite3.connect("window.db")
    c=conn.cursor()
    username = txtusername.get()
    password = txtpassword.get()
    if username and password:
        messagebox.showinfo("Account Created", f"Creating account for Username: {username}, Password: {password}")
        querystring = "INSERT INTO account VALUES (?, ?)"
        c.execute(querystring, (username, password))
        conn.commit()
        conn.close()
    else:
        messagebox.showinfo("Please enter both username and password.")

lbltitle=Label(root,text="Window")
lbltitle.grid(row=0, column=0,)

lblusername=Label(root,text="Username")
lblusername.grid(row=1,column=0)
txtusername = Entry(root, width=60)
txtusername.grid(row=1, column=1)

btncreateaccount=Button(root,text="Create Account", command=createAccount)
btncreateaccount.grid(row=4,column=1)


lblpassword = Label(root, text="Password")
lblpassword.grid(row=2, column=0)
txtpassword = Entry(root, width=60)
txtpassword.grid(row=2, column=1)

btnlogin=Button(root,text="Login", command=login)
btnlogin.grid(row=3,column=1)


conn.commit()
conn.close()
root.mainloop()