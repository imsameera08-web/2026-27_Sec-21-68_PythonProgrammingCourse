# Program to perform list operations:
# Insert, Append, Remove, Sort, and Reverse

# Creating a list
numbers = [20, 10, 40, 30, 50]

print("Original List:", numbers)

# Append operation
numbers.append(60)
print("After Append(60):", numbers)

# Insert operation
numbers.insert(2, 25)   # Insert 25 at index 2
print("After Insert(2, 25):", numbers)

# Remove operation
numbers.remove(40)      # Remove element 40
print("After Remove(40):", numbers)

# Sort operation
numbers.sort()
print("After Sort():", numbers)

# Reverse operation
numbers.reverse()
print("After Reverse():", numbers)