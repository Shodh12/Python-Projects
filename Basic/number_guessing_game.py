import random

random_number=random.randint(1,100)

while True:

    try:
        guess=int(input("Enter guess a number between 1 and 100: "))

        if guess < random_number:
            print("Too low!")
        elif guess> random_number:
            print("Too high!")
        else:
            print("Congratulations! You've guessed the number!")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")