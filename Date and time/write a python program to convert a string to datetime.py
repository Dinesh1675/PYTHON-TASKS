#write a python program to convert a string to datetime

from datetime import datetime
x="May 5 25 2:43pm"
y=datetime.strptime(x, "%B %d %y %I:%M%p")
print(y)
