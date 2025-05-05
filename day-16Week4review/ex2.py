import Retailitem
item1=Retailitem.RetailItem("Jacket",12,59.95)
item2=Retailitem.RetailItem("Designer jeans",40,34.94)
item3=Retailitem.RetailItem("shirt",20,24.95)  
itemsList=[]
transaction=Retailitem.CashRegister([])

def getMenu():
    print("\n")
    print("shop")
    print("1-purchase item")
    print("2-show items")
    print("3-Get total")
    print("4-Exit")

    choice=int(input("Enter a choice"))
    while choice<1 or choice>4:
        print("shop")
        print("1-purchase item")
        print("2-show items")
        print("3-Get total")
        print("4-quit the program")
        choice=int(input("Enter a number(1-4)"))
    return choice

def purchaseitem():
    print("1-Jacket,price=59.95")
    print("2-Designer jeans,price=34.94")
    print("3-shirt,price=24.95")
    itemChoice=int(input())
    while itemChoice<1 or itemChoice>3:
        print("Not a valid item")
        print("1-Jacket,price=59.95")
        print("2-Designer jeans,price=34.94")
        print("3-shirt,price=24.95")
        itemChoice=int(input("Enter a number(1-3)"))

    if itemChoice==1:
        transaction.purchase_item(item1)
    elif itemChoice==2:
        transaction.purchase_item(item2)
    elif itemChoice==3:
        transaction.purchase_item(item3)   
    choice=getMenu()
    return choice

def show_items(itemsList):
    for item in itemsList:
        print(f"{item.description},{item.price:.2f}")
def get_total(itemsList):
    total=0
    for item in itemsList:
        total+=item.price
        print(f"Total price of items in the cart is KShs {total:.2f}")
def main():
    choice=getMenu()
    if choice==1:
        purchaseitem()
        main()
    elif choice==2:
        show_items(itemsList)
        main()
    elif choice==3:
        get_total(itemsList)
        main()
    elif choice==4:

        SystemExit()

main()