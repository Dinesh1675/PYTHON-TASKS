#remove a last key from a dictionary using Arbitary keyword Argument

def s(**a):
    for i,j in a.items():
        s.remove(3)
        print("Key",i,"Value is",j)
s(a=2,b=5,c="Tech",d=90)        
