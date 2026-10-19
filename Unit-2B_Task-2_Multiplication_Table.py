# Example solution: multiplication table using a while loop
number = int(input("Enter a number: "))

multiplier = 1
while multiplier <= 10:
    product = number * multiplier
    print(f"{number} x {multiplier} = {product}")
    multiplier = multiplier + 1