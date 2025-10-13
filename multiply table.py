#print a multiplication table from 1 to 5
n=int(input("Enter a Table No:"))
r=int(input("Enter a Range:"))
for i in range (1,r+1):
    print(i,"*",n,"=",n*i)
