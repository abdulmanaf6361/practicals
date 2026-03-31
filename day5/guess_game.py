import random

secret = random.randint(1, 10)
guess = int(input("Guess the number between 1 and 10: "))

if guess == secret:
    print("Congratulations! You guessed the number.")
else:
    print("Sorry, the correct number was", secret)