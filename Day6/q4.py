a = int(input("Enter a positive integer a: "))
b = int(input("Enter a positive integer b: "))

sum_result = 0

for num in range(1000, 2000):
    if num % a == 0 and num % b == 0:
        sum_result += num

print("Sum of numbers divisible by both", a, "and", b, "in the range [1000, 2000]:", sum_result)
