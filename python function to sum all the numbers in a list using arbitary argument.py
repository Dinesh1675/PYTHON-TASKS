#python function to sum all the numbers in a list using arbitary argument

def add(*a):
 sum=0
 for i in a:
     sum+=i
 print("value is",sum)
add(1,2,3,4,5,6)     
add(4,5)
