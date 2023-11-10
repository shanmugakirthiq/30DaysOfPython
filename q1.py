side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))

if side1 == side2 == side3:
    print("It's an equilateral triangle.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("It's an isosceles triangle.")
else:
    print("It's a scalene triangle.")
