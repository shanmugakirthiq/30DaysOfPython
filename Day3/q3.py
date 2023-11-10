a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    root1 = (-b + (discriminant ** 0.5)) / (2 * a)
    root2 = (-b - (discriminant ** 0.5)) / (2 * a)
    print("The roots are real and distinct:")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif discriminant == 0:
    root = -b / (2 * a)
    print("The root is real and equal:")
    print("Root:", root)
else:
    real_part = -b / (2 * a)
    imaginary_part = (abs(discriminant) ** 0.5) / (2 * a)
    print("The roots are complex:")
    print("Root 1:", real_part, "+", imaginary_part, "i")
    print("Root 2:", real_part, "-", imaginary_part, "i")
