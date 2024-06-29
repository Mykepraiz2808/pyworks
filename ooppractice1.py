# CONSTRUCTORS
class Item:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
    #def calculate_total_length(self, x, y):
    #    return x*y
    def calculate_total_length(self):
         return self.price * self.quantity
    
item1 = Item("laptop", 100, 3)


item2 = Item("car", 1000, 5)

print(item1.calculate_total_length())

print(item2.calculate_total_length())

#NOTE 2:
# YOU CAN ASSIGN ATTRIBUTES TO SPECIFIC INSTANCES INDIVIDUALLY
item2.has_numpad = False




