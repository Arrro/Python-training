# Object Oriented Programming
# Homework Assignment
# Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line:
    import math
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        d = (self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2
        print(self.math.sqrt(d))

    def slope(self):
        s = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
        print(s)
    
# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()
#9.433981132056603

li.slope()
#1.6

# Problem 2
# Fill in the class

class Cylinder:
    pi = 3.14

    def __init__(self,height,radius):
        self.height = height
        self.radius = radius

    def volume(self):
        v = self.pi * (self.radius)**2 * self.height
        print(v)

    def surface_area(self):
        a = 2 * self.pi * self.radius * self.height + 2 * self.pi * (self.radius)**2
        print(a)

# EXAMPLE OUTPUT
c = Cylinder(2,3)
c.volume()
#56.52

c.surface_area()
#94.2