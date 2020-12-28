temperature = int(input("Temperature for today:"))
if temperature >= 40:
    print("Very Hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Good")
elif temperature >= 10:
    print("Cooling")
elif temperature >= 0:
    print("Cold")
else:
    print("Very Cold")




