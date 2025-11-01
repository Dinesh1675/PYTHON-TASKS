#write a python class named as personal with information function with argument of name,mail,mobile,address
#write a another class named as educational with information function with argument of marks of each subject,total and percentage
#Inherit bank with educational and educational with personal

class person:
    def __init__(self,name,mail,mobile,address):
        self.name = name
        self.mail = mail
        self.mobile = mobile
        self.address = address
    def details(self):
        print("My Name is",self.name,"My Mail id is",self.mail,"My mobile number is",self.mobile,"My Address is",self.address)
class educational(person):
    def __init__(self,name,mail,mobile,address,marks,total,percentage):
        super().__init__(name,mail,mobile,address)
        self.marks=marks
        self.total=total
        self.percentage=percentage
    def information(self):
        super().details()
        print("My Marks are",self.marks,"My Total is",self.total,"My Percentage is",self.percentage)
class bank(educational):
    def __init__(self,name,mail,mobile,address,marks,total,percentage,acc_number,branch_name,bank_name,ifsc_code,available_balance):
        super().__init__(name,mail,mobile,address,marks,total,percentage)
        self.account=acc_number
        self.branch=branch_name
        self.bank=bank_name
        self.ifsc=ifsc_code
        self.available=available_balance
    def overall(self):
        super().information()
        print("My account number is",self.account,"My Branch name is",self.branch,"My Bank name is",self.bank,"Bank IFSC Code is",self.ifsc,"and My Available balance is",self.available)
obj_total=bank("Dinesh","dineshdinesh165700@gmail.com",9342526388,"Madurai",[69,77,81,97,92],416,83.2,1250010000,"Kadachanendhal","Indian Overseas Bank","IOB10125",673.12)
obj_total.overall()
