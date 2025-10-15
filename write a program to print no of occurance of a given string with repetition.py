#write a program to print no of occurance of a given string with repetition
text="I am new to this office but not new to role"
n=text.lower().split()
for i in set(n):
    print(i,"=",n.count(i))
