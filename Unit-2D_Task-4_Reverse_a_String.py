# Python program to reverse a string

string = input("Enter a string: ")

reverse = ""

for char in string:
    reverse = char + reverse

print("Reversed string:", reverse)