def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si

# Using default rate
print("Simple Interest (Default Rate):", simple_interest(1000, 2))

# Using explicit rate
print("Simple Interest (Explicit Rate):", simple_interest(1000, 2, 10))