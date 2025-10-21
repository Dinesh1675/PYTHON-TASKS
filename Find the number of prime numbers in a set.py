#Find the number of prime numbers in a set
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i==0:
            return False
    return True
a={2,3,4,5,6,7,8,9,10}
prime_count=sum(1 for num in a if is_prime(num))
print("Numbers of prime numbers in the set:", prime_count)
