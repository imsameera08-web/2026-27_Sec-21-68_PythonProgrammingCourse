# Sample dictionary
student = {
    "name": "Anil",
    "age": 20,
    "course": "Python"
}

# keys()
print("Keys:", student.keys())

# values()
print("Values:", student.values())

# items()
print("Items:", student.items())

# get()
print("Course:", student.get("course"))

# update()
student.update({"age": 21, "city": "Hyderabad"})
print("After update:", student)

# pop()
student.pop("course")
print("After pop:", student)