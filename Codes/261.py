def parallelogram_perimeter(b, h):
    perimeter = 2 * (b + h)
    return perimeter

b = int(input("Enter the base of the parallelogram: "))
h = int(input("Enter the height of the parallelogram: "))
print("The perimeter of the parallelogram is:", parallelogram_perimeter(b, h))
