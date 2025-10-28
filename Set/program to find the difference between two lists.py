#program to find the difference between two lists

a=[1,2,3,4,5]
b=[3,4,5,6,7]

s1=set(a)
s2=set(b)

difference=s1 - s2
print("Elements in A but not in B:", difference)
