#include methods to calculate its area and parameter
#implement subclasses for shapes like circle,triangle and square
#class circle
#area(r),A=3.14*r*r
#parameter(r),c=2*3.14*r
#class triangle
#area(l,b) ,A=1/2*b*h
#parameter(a,b,c),p=a+b+c
#class square
#area(a) A=A*A
#parameter(a),p=4a

class Shape:
    pass
class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r
    def parameter(self):
        return 2 * 3.14 * self.r
class Triangle(Shape):
    def __init__(self,b,h,a1,a2,a3):
        self.b=b
        self.h=h
        self.a1=a1
        self.a2=a2
        self.a3=a3
    def area(self):
        return 0.5 * self.b * self.h
    def parameter(self):
        return self.a1 + self.a2 + self.a3
class Square(Shape):
    def __init__(self,a):
        self.a=a
    def area(self):
        return self.a * self.a
    def parameter(self):
        return 4 * self.a
c=Circle(8)
t=Triangle(6,4,3,4,5)
s=Square(8)
print("Circle area:",c.area())
print("Circle parameter:",c.parameter())
print("Triangle area:",t.area())
print("Triangle parameter:",t.parameter())
print("Square area:",s.area())
print("Square parameter:",s.parameter())
        
    
