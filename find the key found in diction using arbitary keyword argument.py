#find the key found in diction using arbitary keyword argument

def details(**a):
    for b,c in a.items():
        print("Key",b,"Value is",c)
details(Name="Dinesh",Age=20,Address="Madurai")        
