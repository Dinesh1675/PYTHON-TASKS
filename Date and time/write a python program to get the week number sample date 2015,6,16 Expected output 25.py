#write a python program to get the week number sample date:2015,6,16 Expected output:25

from datetime import datetime
x=datetime(2015,6,16)
print(x.strftime("%V"))
