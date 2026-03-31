import random

secret = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Guess (1-10): "))
    
    if guess == secret:
        print("You won!")
        break
    else:
        attempts -= 1
        print("Wrong!", attempts, "attempts left")
else:
    print("Game over! Number was:", secret)