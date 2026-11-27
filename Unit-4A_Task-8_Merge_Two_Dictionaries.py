# First dictionary
dict1 = {
    "Math": 90,
    "Science": 85
}

# Second dictionary
dict2 = {
    "English": 88,
    "Computer": 95
}

# Create a copy of dict1 to keep the original unchanged
merged_dict = dict1.copy()

# Merge dict2 into the copied dictionary
merged_dict.update(dict2)

# Display results
print("Original Dictionary 1:", dict1)
print("Original Dictionary 2:", dict2)
print("Merged Dictionary:", merged_dict)