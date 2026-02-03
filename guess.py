import random

print("Welcome to Guess the Number Game!")
print()

randomNumber = random.randint(1, 100)
life = 100

while life > 0:
    guessNumber = int(input("Guess the number between 1 - 100: "))
    while guessNumber != randomNumber:
        if guessNumber < 1 or guessNumber > 100:
            print("The number is not between 1 and 100.")
        elif guessNumber > randomNumber:
            print("Too High!")
        else:
            print("Too Low!")

        life -= 1
        print(f"You have {life} more guesses left.")

        if life == 0:
            print("You don't have any more chances!")
            break

        guessNumber = int(input("Guess the number between 1 - 100: "))


    if randomNumber == guessNumber:
        print(f"Congratulations! The number {guessNumber} is correct.")
        break
