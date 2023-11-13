number = int(input("Enter a positive integer: "))

digit_sum = 0

while number > 0:
    digit_sum += number % 10  
    number //= 10           

print("Sum of digits:", digit_sum)
