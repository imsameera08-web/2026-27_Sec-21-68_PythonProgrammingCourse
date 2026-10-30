# Python program to demonstrate string methods

text = "  Hello World Python  "

print("Original String:", text)

# upper()
print("Upper Case:", text.upper())

# lower()
print("Lower Case:", text.lower())

# strip()
print("After Strip:", text.strip())

# split()
words = text.strip().split()
print("Split into List:", words)

# join()
joined_text = "-".join(words)
print("Joined String:", joined_text)

# replace()
print("Replace 'World' with 'Python':", text.replace("World", "Python"))

# find()
position = text.find("World")
print("Position of 'World':", position)