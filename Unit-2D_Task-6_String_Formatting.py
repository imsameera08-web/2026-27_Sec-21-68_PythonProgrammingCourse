# Python program to demonstrate string formatting

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

# Using format()
print("\nUsing format():")
print("Name: {}, Age: {}, Marks: {:.2f}".format(name, age, marks))

# Using f-strings
print("\nUsing f-strings:")
print(f"Name: {name}, Age: {age}, Marks: {marks:.2f}")

# Using % operator
print("\nUsing % operator:")
print("Name: %s, Age: %d, Marks: %.2f" % (name, age, marks))
