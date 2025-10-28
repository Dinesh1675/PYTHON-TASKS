#count odd numbers - count how many odd numbers are in (1,2,3,4,5,6,7)

a=(1,2,3,4,5,6,7)
count=0
for i in a:
    if i % 2 != 0:
      count+=1
print("Number of odd numbers:",count) 
