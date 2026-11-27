# Program to read numerator and denominator
# and handle ZeroDivisionError and ValueError

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator / denominator

    print("Result =", result)

except ValueError:
    print("Error: Please enter valid integer values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

finally:
    print("Program completed.")
