import random

selected_num = random.randrange(1, 10)

print("Guess the number between 1 and 10")
guess = int(input("Enter your guess: "))

while guess != selected_num:
    if guess < selected_num:
        print("Too low! Try again.")
        guess = int(input("guess another number: "))
    elif guess > selected_num:
        print("Too high! Try again.")
        guess = int(input("guess another number: "))
    else:
        break

print("Congratulations! You guessed the number.")