def is_prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)
n = int(input("Enter a positive number: "))
if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
