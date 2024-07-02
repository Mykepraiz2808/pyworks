import csv


class Item:
    all = []
    pay_rate = 0.8  # CLASS ATTRIBUTE #PAYRATE AFTER 20% DISCOUNT

    def __init__(self, name: str, price: float, quantity) -> None:  # DATA TYPE SPECIFYING

    # RUN VALIDATIONS TO THE RECEIVED ARGUMENTS USING ASSERT KEYWORD and exception handling for assertion error
        assert price >= 0, f"price {price} is not greater or equal to than zero"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero"
        # ASSIGN TO SELF OBJECT
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # ACTIONS TO EXECUTE
        Item.all.append(self)

    @property  # Property Decorator = Read only attribute = Encapsulation== ALSO GETS AN ATTRIBUTES
    def name(self):
        print("you are trying to get an attribute")
        return self.__name

    @property  # Property Decorator = Read only attribute = Encapsulation== ALSO GETS AN ATTRIBUTES
    def price(self):
        print("you are trying to get an attribute")
        return self.__price


    def apply_discount(self):  # discount method instance attribute and the class attribute
        self.__price = self.__price * self.pay_rate
        return

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @name.setter  #HELPS TO OPERATE THE SET ATTRIBUTE
    def name(self, value):
        if len(value) > 10:   # RAISING EXCEPTION IN THE SETTER
            raise Exception("The name is too long!")
        else:
            self.__name = value
        print("you are trying to set an attribute")

    def connect(self, smtp_server): # EMAIL PROCESSES SERVER
        pass

    def prepare_body(self):      #EMAIL PROCESSING BODY
        return f"""
        Hello dear,
        we have {self.name} {self.quantity} times
        Regards, mike coding
        """

    def send(self):
        pass
    def send_email(self):    # EMAIL INIT #SIMULATING THE PROCESS
        self.connect(80)
        self.prepare_body()
        self.send()

    def __repr__(self) -> str:
        return f"('{self.name}', {self.__price}, {self.quantity})"
        #print(item.all)

    def calculate_total_length(self):
        return self.__price * self.quantity


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



