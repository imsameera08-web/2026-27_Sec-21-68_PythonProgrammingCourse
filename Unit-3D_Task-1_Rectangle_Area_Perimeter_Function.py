def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))

a, p = rectangle(l, b)

print("Area =", a)
print("Perimeter =", p)