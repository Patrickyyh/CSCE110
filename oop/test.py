
class Rectangle:
    def __init__(self, color, length=5, width=9):
        self.color = color
        self.length = length
        self.width = width

rectangle1 = Rectangle('brown', width=11, length=10)
rectangle2 = Rectangle('red')
rectangle3 = Rectangle('black', length=3, width=1)

print(rectangle1.length, rectangle1.width)
print(rectangle2.length, rectangle2.width)
print(rectangle3.length, rectangle3.width)