from art import logo
import random

def game_mechanic(nummber, difficulty):
    if difficulty == "hard":
        attemps_remaining = 5
    else:
        attemps_remaining = 10
    nummber_guesed = False
    while attemps_remaining != 0 and nummber_guesed != True:
        print(f"You have {attemps_remaining} attempts reamining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < nummber:
            print(f"Too low.\nGuess again.")
            attemps_remaining -= 1
        elif guess > nummber:
            print(f"To high.\nGuess again.")
            attemps_remaining -= 1
        else:
            nummber_guesed = True
    if nummber_guesed == True:
        print(f"You got it! The answer was {nummber}")
    else:
        print(f"You lose, you ran out of attemps")

def game():
    print(logo)
    nummber = random.randint(1, 100)
    print(f"Welcome to the Number Guessing game!?\nI'm thinking of a number between 1 and 100\nPssst, the correct answer is {nummber}")
    difficulty_level = input("Choose a difficulty. Tyoe 'easy' or 'hard':").lower()
    game_mechanic(nummber=nummber, difficulty=difficulty_level)

game()