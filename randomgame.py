import random

for x in range(1,6):
    guesNumber = int(input("Enter a number:"))
    randomNumber = random.randint(1, 5)
    if (guesNumber == randomNumber):
        print("You have won")
    else:
        print("You have lost")
        print("Random number was:", randomNumber)