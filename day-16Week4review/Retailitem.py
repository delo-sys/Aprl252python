class RetailItem:
    def __init__(self,description,quantity,price):
        self.description=description
        self.quantity=quantity
        self.price=price
        # print("new item created")

class CashRegister:
    def __init__(self,itemsList):
        self.itemsList=itemsList
    def purchase_item(self,item):
        self.itemsList.append(item)

    def get_total(self):
        total=0
        for item in self.itemsList:
            total+=item.price
        return total
        
    
    def show_items(self):
        print("\n")
        for item in self.itemsList:
            print(f"Description: {item.description}")
            print(f"Units in inventory: {item.quantity}")
            print(f"price:KShs {item.price:.2f}")

    def Clear(self):
        self.itemsList.clear()

    
        