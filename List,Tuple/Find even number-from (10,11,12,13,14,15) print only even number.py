#Find even number-from (10,11,12,13,14,15) print only even number

Num=(10,11,12,13,14,15)
even_number=()
for i in Num:
    if i % 2 == 0:
        even_number +=(i, )
print("Even Numbers:",even_number)        
