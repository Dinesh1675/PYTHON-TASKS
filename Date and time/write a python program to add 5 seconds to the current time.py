#write a python program to add 5 seconds to the current time

from datetime import datetime,timedelta
x=datetime.now()
y=x+timedelta(seconds=5)
print("The current time is",x)
print("The current time after 5 seconds is",y)
