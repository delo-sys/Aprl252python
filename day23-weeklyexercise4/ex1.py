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

def showBooks():
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    querystring="SELECT * FROM Books"
    c.execute(querystring)
    records = c.fetchall()
    lstBooks.delete(0, END)
    for record in records:
        lstBooks.insert(END, f"Title: {record[0]}, Price: {record[2]}")
    conn.close()

def deleteBook():
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    querystring ="DELETE FROM Books WHERE rowid =" +txtBookID.get()
    c.execute(querystring)
    conn.commit()
    conn.close()

def updatebook():
    updatewin=Tk()
    updatewin.title("Update Book Record")
    updatewin.geometry("500x500")
    bookID=txtBookID.get()
    
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    querystring ="SELECT * FROM Books WHERE rowid =" +txtBookID.get()
    c.execute(querystring)
    records = c.fetchall()

    LblTitleUpdate=Label(updatewin,text="Update Books")
    LblBookTitleUpdate=Label(updatewin,text="Update Book Title")
    txtBookTitleUpdate=Entry(updatewin,width=50)
    LblTitleUpdate.grid(row=0,column=0,columnspan=2)
    LblBookTitleUpdate.grid(row=1,column=0,pady=10)
    txtBookTitleUpdate.grid(row=1,column=1,pady=10)
    
    LblBookPriceUpdate=Label(updatewin,text="Update Book price")
    txtBookPriceUpdate=Entry(updatewin,width=50)
    LblBookPriceUpdate.grid(row=2,column=0,pady=10)
    txtBookPriceUpdate.grid(row=2,column=1,pady=10)

    for record in records:
        txtBookTitleUpdate.insert(0,record[0])
        txtBookPriceUpdate.insert(0,record[1])

    def savechanges():
        # conn = sqlite3.connect("books.db")
        c = conn.cursor()
        btitle = txtBookTitleUpdate.get()
        bprice = txtBookPriceUpdate.get()
        c.execute(
            "UPDATE Books SET BookTitle = ?, BookPrice = ? WHERE rowid = ?",
            (btitle, bprice, bookID)
        )
        conn.commit()
        conn.close()
        # querystring ="""UPDATE BOOKS SET
        # BookTitle=:btitle,
        # BookPrice=:bprice,
        # WHERE rowid=oid
        # """,{
        #     'btitle':txtBookTitleUpdate.get(),
        #     'bprice':txtBookPriceUpdate.get()
        # }
        c.execute(querystring)
        conn.commit()
        conn.close()

    btnUpdateBook=Button(updatewin,text="Save Changes", command=savechanges)
    btnUpdateBook.grid(row=3,column=0,pady=20)

    # conn.commit()
    conn.close

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

lblShowBooks=Button(root,text="Show Books",command=showBooks)
lblShowBooks.grid(row=6,column=0,columnspan=2,ipadx=100)

btnDelete=Button(root,text="Delete Book Record",command=deleteBook)
btnDelete.grid(row=10,column=0,columnspan=2,ipadx=100)

btnUpdateBook=Button(root,text="Update Book",command=updatebook)
btnUpdateBook.grid(row=12,column=0,columnspan=2,ipadx=100)

lblBookID=Label(root,text="Enter Book ID")
lblBookID.grid(row=8,column=0,pady=10)
txtBookID=Entry(root)
txtBookID.grid(row=8,column=1,padx=10)


conn.commit()
conn.close()
root.mainloop()