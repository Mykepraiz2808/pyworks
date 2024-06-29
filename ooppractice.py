# BASIC CLASS AND OBJECTS
class Item:
    def calculate_total_length(self, x, y):
        return x*y
    

item1 = Item()
item1.name = "phone"
item1.price = 100
item1.quantity = 3
print(item1.calculate_total_length(item1.price, item1.quantity))

item2 = Item()
item2.name = "phone"
item2.price = 1000
item2.quantity = 5
print(item2.calculate_total_length(item2.price, item2.quantity))
