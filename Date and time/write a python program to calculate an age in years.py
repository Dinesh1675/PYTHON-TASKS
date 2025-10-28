#write a python program to calculate an age in years

from datetime import datetime

x=datetime.today()
birthday=datetime(2005,7,16)
age=x-birthday
print(age)
