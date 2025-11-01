#write a python program to create a person class,Include attributes like name,country and date of birth Implement a method to determine the persons age
#class person: init(name,country,dob) age(dob)

from datetime import date
class person:
    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob
    def age(self):
        today = date.today()
        age = today.year - self.dob.year
        if (today.month,today.day) < (self.dob.month,self.dob.day):
            age -= 1
        return age
obj_person = person("Dinesh","India",date(2005,7,16))
print(obj_person.name,obj_person.country,obj_person.dob)
print("The age is",obj_person.age())
