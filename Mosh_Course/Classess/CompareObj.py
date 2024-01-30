class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    
    def __gt__(self,other):
        return self.x > other.x and self.y > other.y

point = Point(6,9)
another = Point(3,6)

print(point==another)
print(point < another)
# Magic methods for comparison
# __cmp__
# __eq__ : ==
# __ne__ : !=
# __lt__ : <
# __gt__ : >
