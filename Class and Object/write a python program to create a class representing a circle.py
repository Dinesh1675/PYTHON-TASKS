#write a python program to create a class representing a circle
#Include methods to calculate its area and parameter
#class circle:area(r) parameter(r)

class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius
    def parameter(self):
        return 2*3.14*self.radius
obj_circle = circle(8)
print(obj_circle.area())
print(obj_circle.parameter())
