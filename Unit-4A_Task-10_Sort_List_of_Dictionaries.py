# List of student dictionaries
students = [
    {"name": "Anil", "marks": 85},
    {"name": "Bhavana", "marks": 92},
    {"name": "Charan", "marks": 78},
    {"name": "Divya", "marks": 88}
]

# Sort by marks in ascending order
ascending = sorted(students, key=lambda student: student["marks"])

# Sort by marks in descending order
descending = sorted(students, key=lambda student: student["marks"], reverse=True)

# Display results
print("Students Sorted by Marks (Ascending):")
for student in ascending:
    print(student)

print("\nStudents Sorted by Marks (Descending):")
for student in descending:
    print(student)