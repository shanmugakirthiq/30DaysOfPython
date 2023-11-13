n = int(input("Enter the number of gold coins: "))
a = int(input("Enter the share for friend 1: "))
b = int(input("Enter the share for friend 2: "))
c = int(input("Enter the share for friend 3: "))

if a == 0 or b == 0 or c == 0 or a == b or b == c or a == c or (a + b + c != n):
    print("UNFAIR")
else:
    print("FAIR")
