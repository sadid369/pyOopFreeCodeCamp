from item import Item
class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phone =0):
        # Call to supper function to have access to all attributes / methos
        super().__init__(
            name,price,quantity
        )

        # Run validation to the received arguments
        assert broken_phone >= 0, f"Broken Phone {broken_phone} is not grater than or equal to zero"
        # Assign to self object

        self.broken_phone= broken_phone