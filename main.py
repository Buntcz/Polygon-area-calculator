class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def set_height(self,height):
        self.height = height
    def set_width(self,width):
        self.width = width
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    pass

print(Rectangle(3,6))