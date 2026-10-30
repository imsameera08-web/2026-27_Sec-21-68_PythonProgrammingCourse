# Python program to print a right-angled triangle pattern

rows = int(input("Enter the number of rows: "))
symbol = input("Enter the symbol to print: ")

for i in range(1, rows + 1):
    print(symbol * i)