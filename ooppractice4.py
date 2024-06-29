import csv


class Item:
    all = []
    pay_rate = 0.8  # CLASS ATTRIBUTE #PAYRATE AFTER 20% DISCOUNT

    def __init__(self, name: str, price: float, quantity) -> None:  # DATA TYPE SPECIFYING
        # RUN VALIDATIONS TO THE RECEIVED ARGUMENTS USING ASSERT KEYWORD and exception handling for assertion error
        assert price >= 0, f"price {price} is not greater or equal to than zero"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero"
        # ASSIGN TO SELF OBJECT
        self.name = name
        self.price = price
        self.quantity = quantity

        # ACTIONS TO EXECUTE
        Item.all.append(self)

    def __repr__(self) -> str:
        return f"('{self.name}', {self.price}, {self.quantity})"
        #print(item.all)

    def calculate_total_length(self):
        return self.price * self.quantity

    def apply_discount(self):  # discount method instance attribute and the class attribute
        self.price = self.price * self.pay_rate
        return
        # NEWLY CREATED 5 INSTANCES

    @classmethod
    def instantiate_from_csv(cls):
        with open('oopitems.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity'))
            )
    @staticmethod
    def is_integer(num):
         # to fish out floats
      if isinstance(num, float):  #count out the floats that are point zero
          return num.is_integer()
      elif isinstance(num, int):
          return True
      else:
          return False

Item.instantiate_from_csv()

# for instance in item.all:
# print(instance.name)
print(Item.all)
#print(Item.is_integer(7.0))