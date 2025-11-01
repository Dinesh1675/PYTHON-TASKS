#write a python class names as personal with information function with argument of name,mail,mobile,address
#write a another class named as educational with information function with argument of marks of each subject,total and percentage inherit educational with personal

class person:
    def __init__(self,name,mail,mobile,address):
        self.name = name
        self.mail = mail
        self.mobile = mobile
        self.address = address
    def details(self):
        print("My Name is",self.name,"My Mail id is",self.mail,"My mobile number is",self.mobile,"My Address is",self.address)
class education(person):
    def __init__(self,name,mail,mobile,address,marks,total,percentage):
        super().__init__(name,mail,mobile,address)
        self.marks=marks
        self.total=total
        self.percentage=percentage
    def information(self):
        super().details()
        print("My Marks are",self.marks,"My Total is",self.total,"My Percentage is",self.percentage)
obj_details=education("Dinesh","dineshdinesh165700@gmail.com",9342526388,"Madurai",[69,77,81,97,92],416,83.2)
obj_details.information()
