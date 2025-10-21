#find the number of vowels in each name in a set

names={"Sundar","Amaresh","Kumar","Rakesh","Dinesh"}
vowels = "AEIOUaeiou"
vowel_count = {name: sum(1 for char in name if char in vowels) for name in names}
for name,count in vowel_count.items():
    print(f"{name}: {count} vowels")
