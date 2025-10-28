#write a python program to get the current time in milliseconds in python

from datetime import datetime
x=datetime.now()
milliseconds=int(x.timestamp()*1000)
print(milliseconds)
