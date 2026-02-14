import random

words = ["rainbow", "computer", "science", "programming",
         "python", "mathematics", "player", "condition",
         "reverse", "water", "board", "geeks"]

randomGuess = random.choice(words)

print("Welcome to the Character Guessing Game!")
name = input("Enter your name: ")
print(f"Good luck {name}!")
print("Guess the Characters")

guesses_left = 12
display = ["_"] * len(randomGuess)

while guesses_left > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    yourGuess = input("Enter your character guess: ").lower()

    if yourGuess in randomGuess:
        for i in range(len(randomGuess)):
            if randomGuess[i] == yourGuess:
                display[i] = yourGuess
        print("Correct!")
    else:
        guesses_left -= 1
        print("Wrong! Guesses left:", guesses_left)

if "_" not in display:
    print("\nCongratulations! You guessed the word:", randomGuess)
else:
    print("\nGame Over! The word was:", randomGuess)
