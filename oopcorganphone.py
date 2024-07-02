#INHERITANCE
from oopcorganitem import Item


class Phone(Item):
    #all = []  REMOVED
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0) -> None:  # DATA TYPE SPECIFYING
        # RUN VALIDATIONS TO THE RECEIVED ARGUMENTS USING ASSERT KEYWORD and exception handling for assertion error
        # CALL TO SUPER FUNCTION TO HAVE ACCESS TO ALL ATTRIBUTES/METHODS OF PARENT CLASS
        super().__init__(
            name, price, quantity
        )
        assert broken_phones >= 0, f"broken_phones {broken_phones} is not greater than or equal to zero"
        # ASSIGN TO SELF OBJECT

        self.broken_phones = broken_phones

