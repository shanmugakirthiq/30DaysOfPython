hour = int(input("Enter an integer representing the hour: "))

if 0 <= hour <= 5:
    print("NIGHT")
elif 6 <= hour <= 11:
    print("MORNING")
elif 12 <= hour <= 17:
    print("AFTERNOON")
elif 18 <= hour <= 23:
    print("EVENING")
else:
    print("INVALID")
