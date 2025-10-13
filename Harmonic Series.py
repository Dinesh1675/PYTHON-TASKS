#Harmonic Series
Num=int(input("Enter the Number:"))
sum=0
for i in range(1,Num+1):
    print("1/",i)
    sum=sum+1/i
print("The harmonic series given numbers is",sum)    
              
