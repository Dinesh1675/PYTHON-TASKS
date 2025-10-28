#Find smallest number-find the smallest value in (45,12,89,33,67) using a loop

num=(45,12,89,33,67)
smallest = num[0]
for i in num:
    if i<smallest:
        smallest=i
print("smallest number:",smallest)        
