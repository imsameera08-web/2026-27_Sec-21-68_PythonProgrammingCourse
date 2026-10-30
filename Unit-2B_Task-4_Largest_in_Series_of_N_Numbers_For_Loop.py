# Python program to find the largest number in N numbers using a for loop

n = int(input("Enter the number of elements: "))

largest = float('-inf')  # Smallest possible value

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    
    if num > largest:
        largest = num

print("The largest number is:", largest)