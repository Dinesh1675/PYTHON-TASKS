#count vowels-create a tuple of letters and count how many vowels are there using a loop

t=("a","b","c","e","i","o","u")
vowels_count=0
for i in t:
    if i in "aeiou":
        vowels_count+=1
print("Vowels:", vowels_count)        
