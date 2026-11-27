# Subject-Marks Dictionary
subject_marks = {
    "Maths": 95,
    "Science": 88,
    "English": 92,
    "Computer": 98
}

# Print keys using a loop
print("Subjects:")
for key in subject_marks.keys():
    print(key)

# Print values using a loop
print("\nMarks:")
for value in subject_marks.values():
    print(value)

# Print items using a loop
print("\nSubject and Marks:")
for subject, marks in subject_marks.items():
    print(subject, ":", marks)