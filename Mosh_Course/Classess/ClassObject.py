# class : blueprint for creating new objects
# object : instance of a class

class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point,Point))