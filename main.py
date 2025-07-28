# The perfect guess game

import random

# Generate a random number between 1-100
random_number = random.randint(1,100)

# user will guess the number
guess = 1

print("Enter any number between 1 - 100")
user_number = int(input("Enter the number: "))
while not 1 <= user_number <= 100:
    print("Enter a valid number")
    user_number = int(input("Enter the number: "))


# the loop will run until the user has guessed correct number
while(user_number != random_number):
    if(user_number > random_number):
        print("Enter a lower number please ⬇️")
    else:
        print("Enter a higher number please ⬆️")

    guess += 1
    user_number = int(input("Enter the number: "))
    while not 1 <= user_number <= 100:
        print("Enter a valid number")
        user_number = int(input("Enter the number: "))

print("You have found the number...")
print(f"The number is {random_number}")
print(f"You found the number in {guess} steps")