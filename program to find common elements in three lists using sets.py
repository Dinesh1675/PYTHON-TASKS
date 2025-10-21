#program to find common elements in three lists using sets

a=[1,2,3,4,5]
b=[3,4,5,6,7]
c=[5,6,7,8,9]

s1=set(a)
s2=set(b)
s3=set(c)

common_elements = s1 & s2 & s3
print("common elements in the three lists are:",common_elements)
