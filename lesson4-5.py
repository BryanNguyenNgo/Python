temperature = int(input("Enter the temperature:"))
raining =(input("Is it raining (y/n):"))
if temperature < 25 and raining =='y':
    print("Please wear a raincoat or u will be sick :)")
elif temperature < 25 and raining =="n":
    print("Please wear a Jacket")
elif temperature >= 25 and raining =="n":
    print("Please wear a Shirt")
elif temperature >= 25 and raining =="y":
    print("This is weird ........")


