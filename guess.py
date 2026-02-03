import random

print("Welcome to Guess the Number Game!")
print()

randomNumber = random.randint(1, 100)

guessNumber = int(input("Guess the number between 1 - 100: "))

while guessNumber != randomNumber:

    if guessNumber < 1 or guessNumber > 100:
        print("The number is not between 1 and 100.")
    elif guessNumber > randomNumber:
        print("Too High!")
    else:
        print("Too Low!")

    guessNumber = int(input("Guess the number between 1 - 100: "))

print(f"The number {guessNumber} is correct, congratulations!")
