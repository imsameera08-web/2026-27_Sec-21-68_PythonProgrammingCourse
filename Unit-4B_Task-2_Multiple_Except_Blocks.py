# Program to handle ValueError and IndexError separately

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter an index: "))
    print("Value at index", index, "is", numbers[index])

except ValueError:
    print("Error: Please enter a valid integer index.")

except IndexError:
    print("Error: Index out of range.")

finally:
    print("Program execution completed.")
