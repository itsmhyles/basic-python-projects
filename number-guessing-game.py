import random

max_number = 100
random_number = random.randint(1, max_number)
count = 0

while True:
    guess = int(input(f"Guess a number between 1 and {max_number}: "))
    if guess == random_number:
        print(f"Congratulations! You guessed correctly! It took you {count}: guesses but I guess not bad")
        break
    elif guess < random_number:
        print("Too low! Try again.")
        count +=1
    else:
        print("Too high! Try again.")
        count +=1

