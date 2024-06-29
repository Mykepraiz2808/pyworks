class item:
    pay_rate = 0.8   #CLASS ATTRIBUTE #PAYRATE AFTER 20% DISCOUNT
    def __init__(self, name : str, price : float, quantity) -> None:  # DATA TYPE SPECIFYING 
        #RUN VALIDATIONS TO THE RECEIVED ARGUMENTS USING ASSERT KEYWORD and exception handling for assertion error
        assert price >= 0, f"price {price} is not greater or equal to than zero"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero"
        # ASSIGN TO SELF OBJECT
        self.name = name
        self.price = price
        self.quantity = quantity
    #def calculate_total_length(self, x, y):
    #    return x*y   REPLACED BY return self.price * self.quantity
    def calculate_total_length(self):
         return self.price * self.quantity
    def apply_discount(self): #discount method instance attribute and the class attribute
        self.price = self.price * self.pay_rate
        return 
    
item1 = item("LAPTOP", 100, 1)
item1.apply_discount()


item2 = item("car", 1000, 3)
item2.pay_rate = 0.7   #INDIVIDUAL PAY RATE ATTRIBUTE FOR ITEM2 NOT USING THE GLOBAL CLASS ATTRIBUTE
item2.apply_discount()

print(item1.calculate_total_length())

print(item2.calculate_total_length())
#print(item.pay_rate) # CLASS ATTRIBUTE ACCESSIBLE BY CLASS
#print(item1.pay_rate) #CLASS ATTRIBUTE ACCESSIBLE AT INSTANCE LEVEL
#print(item2.pay_rate)  #CLASS ATTRIBUTE ACCESSIBLE AT INSTANCE LEVEL

print(item.__dict__) # __dict__ attribute shows all the attributes for class level
print("")
print(item1.__dict__) # __dict__ attribute shows all the attributes for instance level
print(item2.__dict__) # __dict__ attribute shows all the attributes for instance level


item2.has_numpad = False #NOTE 2: # YOU CAN ASSIGN ATTRIBUTES TO SPECIFIC INSTANCES INDIVIDUALLY