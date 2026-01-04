n = int(input("Enter a positive number: "))

if n <= 1:
    print(n, "is not a prime number")
else:
    flag = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            flag = 1
            break
    if flag == 0:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")
