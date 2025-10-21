#check if two lists have at-least one element common

L1=[1,2,3,4,5]
L2=[5,6,7,8,9]

s1=set(L1)
s2=set(L2)

if s1 & s2:
    print("List have at least one common element.")
else:
    print("List have no common element.")
