employee1 = int(input("Enter employee 1 ID: "))
employee2 = int(input("Enter employee 2 ID: "))
employee3 = int(input("Enter employee 3 ID: "))
employee4 = int(input("Enter employee 4 ID: "))
employee5 = int(input("Enter employee 5 ID: "))

if (employee1 + employee2) % 2 == 0 and \
   (employee2 + employee3) % 2 == 0 and \
   (employee3 + employee4) % 2 == 0 and \
   (employee4 + employee5) % 2 == 0 and \
   (employee5 + employee1) % 2 == 0:
    result = "YES"
else:
    result = "NO"

print(result)
