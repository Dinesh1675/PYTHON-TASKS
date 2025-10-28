#write a python program to convert a string to datetime
#sample string:July 1 14 2:43PM
#Expected output:2014-07-01 14:43:00

from datetime import datetime
x="July 1 14 2:43PM"
y=datetime.strptime(x, "%B %d %y %I:%M%p")
print(y)
