# Python program to demonstrate set creation and
# basic set operations: Union, Intersection, Difference

# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# Union
union_set = set1.union(set2)
print("\nUnion:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference
difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)

print("Difference (set1 - set2):", difference_set1)
print("Difference (set2 - set1):", difference_set2)