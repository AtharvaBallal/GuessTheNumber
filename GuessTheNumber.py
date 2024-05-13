import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100.")

HARD = 5
EASY = 10
NUMBER = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

def guess(num):
    guess = int(input("Make a guess:"))
    con = False

    while not con and num > 1:

        if guess < NUMBER:
            print("Too Low")
            guess = int(input("guess again."))
            num -= 1
        elif guess > NUMBER:
            print("Too High")
            guess = int(input("guess again."))
            num -= 1
        elif guess == NUMBER:
            print(f"You got it! The answer was {NUMBER}")
            con = True


if difficulty == "hard":
    print(f"You have {HARD} attempts remaining to guess the number")
    guess(HARD)
elif difficulty == "easy":
    print(f"You have {EASY} attempts remaining to guess the number")
    guess(EASY)
else:
    print("Chose option correctly. Restart the game!")
