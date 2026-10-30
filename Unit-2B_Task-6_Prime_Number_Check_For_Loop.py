# Python program to check whether a number is prime or not using for loop

num = int(input("Enter a number (1 to 100): "))

if num <= 1:
    print(num, "is not a prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")