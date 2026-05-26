import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle with Radius: {self.radius:.2f} (Diameter: {self.diameter:.2f})"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        raise TypeError("You can only add a Circle to another Circle.")

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented
    
c1 = Circle(5)

print(c1)
print(f"Area : {c1.area:.2f}")

c1.diameter = 12

print(f"New Radius after setting diameter to 12 : {c1.radius}")
print("-" * 40)

c2 = Circle(4)
c3 = c1 + c2

print("Result of c1 + c2 :", c3)
print("-" * 40)

circle_list = [Circle(10), Circle(2), Circle(7), Circle(5)]
print("Original list :", circle_list)

sorted_circles = sorted(circle_list)

print("Sorted list :  ", sorted_circles)
print("Is Circle(10) > Circle(2) ? :", Circle(10) > Circle(2))


import turtle

screen = turtle.Screen()
screen.setup(600, 400)
t = turtle.Turtle()
t.speed(3)

my_circles = [Circle(40), Circle(15), Circle(60), Circle(30)]
my_circles.sort()

for circle in my_circles:
    t.pendown()
    t.circle(circle.radius)
    t.penup()
    t.forward(circle.diameter + 15) 

turtle.done()