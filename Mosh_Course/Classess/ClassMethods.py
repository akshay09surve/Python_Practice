class Point:
    default_color = "red"

    # this __init__ magic method functions as a constructor
    def __init__(self,x,y):
        self.x=x
        self.y=y

    # class method - cls refers to class itself
    @classmethod
    def zero(cls):
        return cls(0,0)


    def draw(self):
        print(f"Point ({self.x},{self.y})")


point2 = Point.zero() #Factory method of creating objects- class method
point2.draw()