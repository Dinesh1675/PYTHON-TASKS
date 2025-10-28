#find the number of even numbers and odd numbers in a set

num={1,2,3,4,5,6,7,8,9,10}
even_count=sum(1 for num in num if num % 2 == 0)
odd_count=sum(1 for num in num if num % 2 != 0)
print("Number of Even numbers:", even_count)
print("Number of Odd numbers:", odd_count)
