# Nested dictionary of students

students = {
    "S001": {"name": "Anil", "marks": 85},
    "S002": {"name": "Bhavana", "marks": 92},
    "S003": {"name": "Charan", "marks": 78},
    "S004": {"name": "Divya", "marks": 88}
}

# Print student names and marks
print("Student Details:")

for student_id, details in students.items():
    print("Name:", details["name"], "- Marks:", details["marks"])