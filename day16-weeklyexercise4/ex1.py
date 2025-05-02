class RetailItem:
    def __init__(self, description, quantity, price):
        self.description = description
        self.quantity = quantity
        self.price = price
        # print(f"new Item created:")

class CashRegister:
    def __init__(self):
        self.items = []

    def purchase_item(self, item):
        self.items.append(item)

    def get_total(self):
        total=0
        for item in self.items:
            total += item.price
        return total

    def show_items(self):
        print("\n")
        for item in self.items:
            print(f"Item: {item.description}")
            print ("Quantity: {item.quantity}") 
            print ("Price: Ksh{item.price:.2f}")

    def clear_items(self):
        self.items.clear()