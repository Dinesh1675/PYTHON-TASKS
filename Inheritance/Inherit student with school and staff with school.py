#Inherit student with school and staff with school

class school:
    def __init__(self,name,mail,mobile,address):
        self.name = name
        self.mail = mail
        self.mobile = mobile
        self.address = address
    def school_details(self):
        print("My Name is",self.name,"My Mail id is",self.mail,"My mobile number is",self.mobile,"My Address is",self.address)
class staff(school):
    def __init__(self,name,mail,mobile,address,dept):
        super().__init__(name,mail,mobile,address)
        self.department=dept
    def staff_details(self):
        super().school_details()
        print("My department is",self.department)
class student(school):
    def __init__(self,name,mail,mobile,address,dept):
        super().__init__(name,mail,mobile,address)
        self.department=dept
    def student_details(self):
        super().school_details()
        print("My department is",self.department)
user=input("Enter whether your student or staff:").strip().lower()
if user=="student":
    obj=student("Dinesh","dineshdinesh165700@gmail.com",9342526388,"Madurai","B.sc")
    obj.student_details()
elif user=="staff":
    obj=staff("Sri","Sri1657@gmail.com",9789629072,"Madurai","Bsc SSS")
    obj.staff_details()
else:
    print("Invalid Input")
