#Remove all even numbers from a list using a for loop

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

odd_numbers=[]
for i in list:
    if i%2!=0:
        odd_numbers.append(i)
print(odd_numbers)        
