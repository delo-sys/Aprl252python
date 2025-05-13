import sqlite3
from tkinter import *

root = Tk()
root.geometry("500x500")
conn=sqlite3.connect("books.db")
c=conn.cursor()

def addBook():
    conn=sqlite3.connect("books.db")
    c=conn.cursor()
    querystring=f"INSERT INTO Books VALUES ('{txtBookTitle.get()}','{txtBookPrice.get()}')"
    c.execute(querystring)
    conn.commit()
    conn.close()

    txtBookTitle.delete(0,END)
    txtBookPrice.delete(0,END)

LblTitle=Label(root,text="Books")
LblBookTitle=Label(root,text="Book Title")
txtBookTitle=Entry(root,width=50)
LblTitle.grid(row=0,column=0,columnspan=2)
LblBookTitle.grid(row=1,column=0,pady=10)
txtBookTitle.grid(row=1,column=1,pady=10)

LblBookPrice=Label(root,text="Book price")
txtBookPrice=Entry(root,width=50)
LblBookPrice.grid(row=2,column=0,pady=10)
txtBookPrice.grid(row=2,column=1,pady=10)

lblShowBooks=Label(root,text="Display Books")
lblShowBooks.grid(row=6,column=0,columnspan=2)

lstBooks = Listbox(root, width=50, height=10)
lstBooks.grid(row=7, column=0, columnspan=2, pady=10)


btnAddRecord=Button(root,text="Add New Book",command=addBook)
btnAddRecord.grid(row=4,column=0,columnspan=2,ipadx=100)

def showBooks():
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    querystring="SELECT * FROM Books"
    c.execute(querystring)
    records = c.fetchall()
    lstBooks.delete(0, END)
    for record in records:
        lstBooks.insert(END, f"Title: {record[0]}, Price: {record[1]}")
    conn.close()


lblShowBooks=Button(root,text="Show Books",command=showBooks)
lblShowBooks.grid(row=6,column=0,columnspan=2,ipadx=100)

conn.commit()
conn.close()
root.mainloop()