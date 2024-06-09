from time import sleep
from Score import add_score
import os


def welcome(name):
    # Return a welcome message using an f-string
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find a variety of cool games to play.\n"


# Get player's name and print the welcome message
name = input("What is your name? ")
print(welcome(name))


def read_current_score():
    if not os.path.exists("Scores.txt"):
        with open("Scores.txt", "w") as file:
            file.write("0")

    try:
        with open("Scores.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0


def load_game():
    current_score = read_current_score()
    print(f"Current score: {current_score}")

    # Display game options for the user to choose from
    print("Choose a game:")
    print("1. Memory Game")
    print("2. Guessing Game")
    print("3. Currency Roulette")

    # Loop until the user enters a valid game choice (1-3).
    while True:
        try:
            game_choice = int(input("Enter game number (1-3): "))
            if 1 <= game_choice <= 3:
                break  # Exit the loop if a valid difficulty is entered
            else:
                print("Invalid game choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Loop until the user enters a valid difficulty level (1-5).
    while True:
        try:
            difficulty = int(input("Choose game difficulty (1-5): "))
            if 1 <= difficulty <= 5:
                break
            else:
                print("Invalid difficulty level. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Run the chosen game
    if game_choice == 1:
        if play_memory_game(difficulty):
            add_score(difficulty)
    elif game_choice == 2:
        if play_guessing_game(difficulty):
            add_score(difficulty)
    elif game_choice == 3:
        if play_currency_roulette(difficulty):
            add_score(difficulty)

    new_score = read_current_score()
    print(f"New score: {new_score}")

    return game_choice, difficulty


# MemoryGame
import random


def play_memory_game(difficulty):
    # Define difficulty levels with sequences of different lengths and maximum numbers
    difficulty_levels = {
        1: {"sequence_length": 3, "max_number": 5},  # Easy
        2: {"sequence_length": 4, "max_number": 7},  # Medium
        3: {"sequence_length": 5, "max_number": 10},  # Hard
        4: {"sequence_length": 6, "max_number": 12},  # Very Hard
        5: {"sequence_length": 8, "max_number": 15},  # Extreme
    }

    # Check if chosen difficulty is valid, default to medium if not
    if difficulty not in difficulty_levels:
        print("Invalid difficulty! Defaulting to medium (3).")
        difficulty = 3

    # Extract sequence parameters based on chosen difficulty
    sequence_length = difficulty_levels[difficulty]["sequence_length"]
    max_number = difficulty_levels[difficulty]["max_number"]

    # Print difficulty information
    print(f"Difficulty: {difficulty} (Sequence Length: {sequence_length}, Maximum Number: {max_number})")

    # Generate random number sequence
    numbers = [random.randint(1, max_number) for _ in range(sequence_length)]

    # Show the sequence to the player
    print("Remember this sequence:", numbers)
    print(f"Get ready! The sequence will disappear in {sequence_length} seconds...")
    sleep(sequence_length)  # Wait for the specified duration

    # Get player's guess
    guess = input("Enter the sequence you saw, separated by spaces: ")

    # Convert guess to list of numbers
    guessed_sequence = list(map(int, guess.split()))

    # Check if guess is correct
    if guessed_sequence == numbers:
        print("You got it right!")
        return True
    else:
        print("Oops! The correct sequence was:", numbers)
        return False

    # Print the message after the game logic is complete
    print(f"Playing Memory Game at difficulty {difficulty}")


# GuessGame
def play_guessing_game(difficulty):
    # Define the number range based on difficulty
    if difficulty == 1:
        number_range = (1, 10)  # Easy
        print("Easy mode: Guess a number between 1 and 10.")
    elif difficulty == 2:
        number_range = (1, 20)  # Medium
        print("Medium mode: Guess a number between 1 and 20.")
    elif difficulty == 3:
        number_range = (1, 50)  # Hard
        print("Hard mode: Guess a number between 1 and 50.")
    elif difficulty == 4:
        number_range = (1, 100)  # Very Hard
        print("Very Hard mode: Guess a number between 1 and 100.")
    elif difficulty == 5:
        number_range = (1, 1000)  # Extreme
        print("Extreme mode: Guess a number between 1 and 1000.")
    else:
        # Invalid difficulty, default to medium
        print("Invalid difficulty! Defaulting to medium (2).")
        number_range = (1, 20)

    # Generate random number within the chosen range
    random_number = random.randint(*number_range)  # Use unpacking

    # Game loop
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f"Guess a number between {number_range[0]} and {number_range[1]}: "))
            if guess < random_number:
                print("Sorry, guess again. Too low.")
            elif guess > random_number:
                print("Sorry, guess again. Too high.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Yay, congrats. You have guessed the number {random_number} correctly!")
    return True


# CurrencyRoulette
def play_currency_roulette(difficulty):
    USD_TO_ILS_RATE = 3.5  # Exchange rate between USD and ILS
    MIN_AMOUNT = 1  # Minimum amount in USD
    MAX_AMOUNT = 100  # Maximum amount in USD

    # Define difficulty levels with names and ranges
    DIFFICULTY_LEVELS = {
        1: {"name": "Easy", "range": (0.1 * MAX_AMOUNT, MAX_AMOUNT)},
        2: {"name": "Medium", "range": (0.25 * MAX_AMOUNT, MAX_AMOUNT)},
        3: {"name": "Hard", "range": (0.5 * MAX_AMOUNT, MAX_AMOUNT)},
        4: {"name": "Very Hard", "range": (0.75 * MAX_AMOUNT, MAX_AMOUNT)},
        5: {"name": "Expert", "range": (MIN_AMOUNT, MAX_AMOUNT)},
    }

    # Function to generate a random amount in USD based on difficulty
    def generate_random_amount(difficulty):
        # Get the minimum and maximum values for the chosen difficulty
        min_value, max_value = DIFFICULTY_LEVELS[difficulty]["range"]

        # Use the 'random.uniform' function to generate a random float within the range
        return random.uniform(min_value, max_value)

    # Function to convert USD amount to ILS
    def convert_to_ils(amount):
        # Multiply the USD amount by the exchange rate to get the ILS amount
        return amount * USD_TO_ILS_RATE

    # Function to play the currency conversion guessing game
    def play_game(difficulty):
        # Generate a random USD amount based on the difficulty
        amount
