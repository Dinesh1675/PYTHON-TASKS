#python function to print the even numbers from a given list using arbitary argument

def add(*a):
 even=[]
 for i in a:
     if i%2==0:
         even+=(i, )
 print("Even value is",even)
add(1,2,3,4,5,6,7,8,9,10) 
