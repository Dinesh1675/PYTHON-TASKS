#count even numbers-from a list [1,2,3,4,5,6,7,8],count how many are even
a=[1,2,3,4,5,6,7,8,9]
count=0
for i in a:
    if i%2==0:
      count+=1
print("Number of even numbers:",count) 
