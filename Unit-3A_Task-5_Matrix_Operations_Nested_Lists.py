# Python program to perform matrix operations using nested lists
# (Addition, Subtraction, and Transpose)

# Matrix A
A = [
    [1, 2, 3],
    [4, 5, 6]
]

# Matrix B
B = [
    [7, 8, 9],
    [1, 2, 3]
]

# Matrix Addition
addition = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    addition.append(row)

# Matrix Subtraction
subtraction = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] - B[i][j])
    subtraction.append(row)

# Transpose of Matrix A
transpose = []
for j in range(len(A[0])):
    row = []
    for i in range(len(A)):
        row.append(A[i][j])
    transpose.append(row)

# Display Results
print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nAddition of A and B:")
for row in addition:
    print(row)

print("\nSubtraction of A and B:")
for row in subtraction:
    print(row)

print("\nTranspose of Matrix A:")
for row in transpose:
    print(row)