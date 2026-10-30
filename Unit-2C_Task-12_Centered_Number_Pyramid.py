# Python program to print a centered pyramid pattern of numbers

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    # Print leading spaces
    print(" " * (rows - i), end="")

    # Print numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    print()
    