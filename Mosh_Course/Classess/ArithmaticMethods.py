class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return f"({self.x+other.x},{self.y+other.y})"
    
    def __str__(self,other):
        return f"({self.x+other.x},{self.y+other.y})"
    
point = Point(3,9)
another = Point(6,9)
sumObj = point+another
print(point+another)
print(sumObj)
