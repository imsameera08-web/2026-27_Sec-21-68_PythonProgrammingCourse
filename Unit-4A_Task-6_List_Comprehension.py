# List comprehension to create squares of numbers from 1 to 10
squares = [num ** 2 for num in range(1, 11)]

# List comprehension to create even numbers from 1 to 10
even_numbers = [num for num in range(1, 11) if num % 2 == 0]

# Display the results
print("Squares of 1 to 10:")
print(squares)

print("\nEven numbers from 1 to 10:")
print(even_numbers)