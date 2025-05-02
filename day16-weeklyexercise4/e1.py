import ex1
item1 = ex1.RetailItem(description="jacket", quantity=12, price=59.95)
item2 = ex1.RetailItem(description="designer jeans", quantity=40, price=49.95)
item3 = ex1.RetailItem("shirt", 20, 24.95) 
itemlist = []
transaction = ex1.CashRegister()

def getmenu():
    print(" 1: Purchase item")
    print(" 2: Show items")
    print(" 3: Get total")
    print(" 4: exit")

    choice = int(input("Enter your choice: "))
    while choice <1 or choice >4:
        print(" 1: Purchase item")
        print(" 2: Show items")
        print(" 3: Get total")
        print(" 4: exit")
        choice=int(input("enter a number(1-4)"))
        return choice

def purchase_item():
    print("1-jacket, price=59.95")
    print("1-designer jeans, price=49.95")
    print("1-jacket, price=24.95")
    itemchoice = int(input())
    while itemchoice < 1 or itemchoice > 4:
        print("not a valid item")
        print("1-jacket, price=59.95")
        print("1-designer jeans, price=49.95")
        print("1-jacket, price=24.95") 
        itemchoice=int(input("enter a number(1-4)"))

    if itemchoice == 1:
        transaction.purchase(item1)
    elif itemchoice == 2:
        transaction.purchase(item2)
    elif itemchoice == 3:
        transaction.purchase(item3)
    else:
        choice = getmenu()
    return choice

def main ():
    choice=getmenu()
    if choice == 1:
        purchase_item()
main()