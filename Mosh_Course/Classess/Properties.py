class Product:

    def __init__(self,price):
        self.price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative.")
        self.__price=value


p1 = Product(-1) 
print(p1.price)