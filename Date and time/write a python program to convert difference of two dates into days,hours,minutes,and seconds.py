#write a python program to convert difference of two dates into days,hours,minutes,and seconds

from datetime import datetime
date1=datetime(2000,2,28)
date2=datetime(2000,2,28)
difference=date2-date1
days=difference.days
hours=days*24
minutes=hours*60
seconds=minutes*60
print("Days:",days)
print("Hours:",hours)
print("Minutes:",minutes)
print("Seconds:",seconds)
