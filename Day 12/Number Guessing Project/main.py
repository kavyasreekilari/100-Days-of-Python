import art
import random
print(art.logo)

# using global variables
# attempts = 0
# try_again = True

# global constants
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

# def guess_again(attempts):
#     global try_again
#     if attempts > 0:
#         try_again = True
#         print("Guess again.")
#     else:
#         print("You've run out of guesses, you lose.")

def choose_difficulty(difficulty):
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif difficulty == 'hard':
        return HARD_LEVEL_ATTEMPTS

def check_answer(user_guess, answer, turns):
    # if user_guess == answer:
    #     print(f"You got it! The answer was {answer}")
    #     try_again = False
    # global try_again
    if user_guess > answer:
        print("Too high.")
        return turns - 1
    elif user_guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")



def guessing_game():
    # global attempts
    # global try_again
    # local variable
    difficulty = ' '
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking if a number between 1 and 100.")
    turns = choose_difficulty(difficulty)

    answer = random.randint(1, 100)
    guess = 0

    while guess != answer:

        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


guessing_game()
