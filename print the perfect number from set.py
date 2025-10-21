#print the perfect number from set

def is_perfect(n):
    if n < 1:
        return False
    returm sum(i for i in range(1, n) if n % i == 0) == n
numbers={6,12,28,15,24,496}
perfect_numbers={num for num in numbers if is_perfect(num)}
print("Perfect Numbers in the set:", perfect_numbers)
