# Python program to remove duplicates from a list using sets

# Original list with duplicate elements
numbers = [10, 20, 30, 20, 40, 10, 50, 30]

print("Original List:", numbers)

# Remove duplicates using set
unique_numbers = list(set(numbers))

print("List after removing duplicates:", unique_numbers)
