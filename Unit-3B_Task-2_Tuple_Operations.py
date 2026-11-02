# Python program to demonstrate tuple operations
# (Concatenation, Slicing, and Unpacking)

# Creating tuples
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

# Concatenation
combined_tuple = tuple1 + tuple2
print("After Concatenation:", combined_tuple)

# Slicing
print("First 3 elements:", combined_tuple[:3])
print("Elements from index 2 to 4:", combined_tuple[2:5])
print("Last 2 elements:", combined_tuple[-2:])

# Unpacking
a, b, c = tuple1
print("\nUnpacked values from tuple1:")
print("a =", a)
print("b =", b)
print("c =", c)