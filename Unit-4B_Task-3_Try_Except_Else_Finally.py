# Program to convert text to an integer,
# print its square in else,
# and always print a message in finally

try:
    text = input("Enter a number: ")
    number = int(text)

except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

else:
    print("Square of the number is:", number ** 2)

finally:
    print("Program finished")