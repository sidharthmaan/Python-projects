import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number from 1 to {x}:-> "))
        if guess < random_number:
            print("Sorry, guess again. Its low. ")
        elif guess > random_number:
            print("Sorry, Guess again. Its High. ")

    print(f'Yay, congrats. You have guessed the number {random_number} correctly. ')

guess(100)