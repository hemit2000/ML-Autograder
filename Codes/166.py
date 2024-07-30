def quadratic(a, b, c):
    d = (b ** 2) - (4 * a * c)

    if d < 0:
        return None

    root1 = (-b - d ** 0.5) / (2 * a)
    root2 = (-b + d ** 0.5) / (2 * a)
    return root1, root2

print(quadratic(1, 5, 4))
