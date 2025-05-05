import Retailitem
item1=Retailitem.RetailItem("Jacket",12,59.95)
item2=Retailitem.RetailItem("Designer jeans",40,34.94)
item3=Retailitem.RetailItem("shirt",20,24.95)   

def get_menu():
    print()
    print("shop")
    print("1-purchase item")
    print("2-show items")
    print("3-Get total")
    print("4-Exit")

    choice=int(input("Enter a choice"))

    while choice<1 or choice>4:
        choice=int(input("Enter a number(1-4)"))
    return choice
    



def main():
    item={}
    choice=0
    while choice!=4:
        choice=get_menu()
                   
main()