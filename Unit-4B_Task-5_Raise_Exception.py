# Program to raise ValueError if age is negative

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age entered:", age)

except ValueError as e:
    print("Error:", e)

finally:
    print("Program finished.")
