def purchaseItem():
    while itmechoice<1 or itmechoice>4:
        print("1."jacket",price=ksh59.95")
        print("2."designer jeans",price=ksh49.95")
        print("3."shirt",price=ksh24.95")
        itmechoice = int(input())
    return itmechoice

def main(): 
    choice=getMenu()
    if choice==1:
        purchaseItem()