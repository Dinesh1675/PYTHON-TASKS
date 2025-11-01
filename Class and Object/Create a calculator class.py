#Create a calculator class
#class calculator: add a,b sub a,b mul a,b div a,b

class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(slef,a,b):
        return a*b
    def div(self,a,b):
        return a/b
obj_cal = calculator()
print(obj_cal.add(8,5))
print(obj_cal.sub(8,5))
print(obj_cal.mul(8,5))
print(obj_cal.div(8,2))
