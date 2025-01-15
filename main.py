class Rectangle:
    def __init__(self,*args):
        if len(args) != 2:
            raise ValueError("Rectangle has only 2 sides")
        self.width = args[0]
        self.height = args[1]
    def set_height(self,height):
        self.height = height
    def set_width(self,width):
        self.width = width
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return (2*self.width) + (2*self.height)
    def get_diagonal(self):
        return(self.width ** 2 + self.height ** 2)**0.5
    def get_picture(self):
        output = ""
        if self.height >= 50 or self.width >= 50:
            return "Too big for picture."
        for _ in range(self.height):
            output += "*" * self.width
            output += "\n"
        return output
    def get_amount_inside(self,shape):
        if isinstance(shape,Rectangle) or isinstance(shape,Square):
            area = self.get_area()
            shape_area = shape.get_area()
            return area // shape_area
        return "shape must be an instance of Square or Ractangle"
class Square(Rectangle):
    def __init__(self,*args):
        if len(args) != 1:
            raise ValueError("Square has only 1 side")
        self.side = args[0]
        self.height = self.side
        self.width = self.side
    def set_side(self,side):
        self.side = side
        self.height = side
        self.width = side
    def set_height(self,height):
        self.side = height
        self.width = height
        self.height = height
    def set_width(self, width):
        self.side = width
        self.height = width
        self.width = width
    def __str__(self):
        return f"Square(side={self.side})"

rec1 = Rectangle(15,10)
sqr1 = Square(5)
rec2 = Rectangle(3,6)
print(rec1.get_amount_inside(sqr1))
