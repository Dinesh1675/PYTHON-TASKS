#write a python script to display the various date time formats
#Current date and time
import datetime as a
x=a.datetime.now()
y=x.timetuple()
print(x)
#Current Year
print("Current Year is:",y[0])
#Month of year
print("Current Month of Year is:",y[1])
#Week number of the year
print("Current Weak no.of Year is:",x.strftime("%U"))
#Weekday of the week
print("Current W.day of the week is:",x.strftime("%w"))
#day of year
print("Current Day of Year is:",x.strftime("%j"))
#Day of the Month
print("Current Day of the Month is:",y[2])
#Day of week
print("Current Day of week is:",y[6])
