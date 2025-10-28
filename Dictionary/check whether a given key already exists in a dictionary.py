#check whether a given key already exists in a dictionary
a={1:"varsha",2:"asif",3:"Kiran"}
key=int(input("Enter the key:"))
if key in a:
    print("Exists")
else:
    print("Not Exists")
