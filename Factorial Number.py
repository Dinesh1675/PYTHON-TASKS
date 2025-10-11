#calculate the factorial number
n=int(input("Enter a Value:"))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)
