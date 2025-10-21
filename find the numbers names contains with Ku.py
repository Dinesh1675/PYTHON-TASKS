#find the numbers names contains with "Ku"

names={"Kunal","Mukesh","Suresh","Kumar"}
names_with_ku = {name for name in names if "Ku" in name}
print("Names containing 'Ku':",names_with_ku)
