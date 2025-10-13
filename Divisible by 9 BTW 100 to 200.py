#Divisible by 9
sum=0
count=0
print("Numbers divisible by 9 100 to 200 are:")
for i in range(100,201):
    if i % 9==0:
        print(i,end=" ")
        sum+=i
        count+=1
print("\nCount:", count)
print("sum:",sum)
