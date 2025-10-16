#Add names entered by the user into a list until they type STOP
name=[]
while True:
    list = input("Enter the name(type 'stop' to end):")
    if list.lower()=='stop':
       break
    name.append(list)
print("Entered names are:" ,name)    
    



























          
