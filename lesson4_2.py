import random
mystery = random.randint(1,100)
tries_left=5
print("You have",tries_left,'tries')

while tries_left > 0:
    guess = int(input("GUESS THE NUMBER:"))
    tries_left -=1
    if guess > mystery and tries_left  > 0:
        print("YOUR NUMBER IS TOO LARGE NOW ITS TIME TO EAT YOU ")
        print("You left with", tries_left,'tries')
    elif guess < mystery and tries_left  >0:
        print("YOUR NUMBER IS TOO SMALL NOW ITS TIME TO EAT YOU")
        print("You left with", tries_left, 'tries')
    elif guess == mystery and tries_left  >0:
        print("Your number is actually correct!GGS!")
        print("You left with", tries_left, 'tries')
        break
    else:
        print("GAME OVER!")
        print("YOU USED ALL UP UR TRIES U NUB!")
        print("the number is ",mystery)
        break