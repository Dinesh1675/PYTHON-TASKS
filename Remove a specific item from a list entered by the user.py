#Remove a specific item from a list entered by the user
cities=["madurai","chennai","salem"]
user=input("enter the city you want to remove :madurai/chennai/salem:")
if user in cities:
    cities.remove(user)
    print("The updated cities are:",cities)
else:
    print("You have entered the incorrect city name")
