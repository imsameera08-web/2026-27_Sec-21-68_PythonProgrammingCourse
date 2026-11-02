# Python program to demonstrate set membership testing
# and set methods: add(), remove(), discard()

# Creating a set
numbers = {10, 20, 30, 40, 50}

print("Original Set:", numbers)

# Membership Testing
if 30 in numbers:
    print("30 is present in the set")
else:
    print("30 is not present in the set")

if 100 not in numbers:
    print("100 is not present in the set")

# add() method
numbers.add(60)
print("\nAfter add(60):", numbers)

# remove() method
numbers.remove(20)
print("After remove(20):", numbers)

# discard() method
numbers.discard(40)
print("After discard(40):", numbers)

# discard() does not raise an error if the element is absent
numbers.discard(100)
print("After discard(100):", numbers)