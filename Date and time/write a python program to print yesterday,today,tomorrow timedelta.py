#write a python program to print yesterday,today,tomorrow timedelta

from datetime import datetime,timedelta

x=datetime.today()
y=x-timedelta(days=1)
z=x+timedelta(days=1)
print("The current day is",x)
print("The yesterday is",y)
print("the tomorrow is",z)
