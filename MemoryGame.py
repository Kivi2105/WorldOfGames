import random
from time import sleep

def play_memory_game(difficulty):


    # Define difficulty levels
    difficulty_levels = {
        1: {"sequence_length": 1, "max_number": 5},
        2: {"sequence_length": 1, "max_number": 7},
        3: {"sequence_length": 1, "max_number": 10},
        4: {"sequence_length": 1, "max_number": 12},
        5: {"sequence_length": 1, "max_number": 15},
    }

    # Define a dictionary to store sequence parameters for different difficulty levels
    difficulty_levels = {
        1: {"sequence_length": 4, "max_number": 5},
        2: {"sequence_length": 6, "max_number": 10},
        3: {"sequence_length": 8, "max_number": 15},
    }

    # Set a difficulty level (assuming it's not defined elsewhere in the code)
    difficulty = 4

    # Check if the chosen difficulty is valid (i.e., exists in the dictionary)
    if difficulty not in difficulty_levels:
        print("Invalid difficulty! Defaulting to medium (3).")
        difficulty = 3  # Use the default medium difficulty if the chosen one is invalid

    # Extract sequence parameters based on the chosen (or default) difficulty
    sequence_length = difficulty_levels[difficulty]["sequence_length"]
    max_number = difficulty_levels[difficulty]["max_number"]

    # Print the sequence parameters for the chosen difficulty
    print(f"Sequence length: {sequence_length}, Maximum number: {max_number}")

    # Create an empty list to store random numbers
    numbers = []

    # Loop to generate random numbers and add them to the list
    for i in range(sequence_length):
        # Generate a random number between 1 and max_number (inclusive)
        number = random.randint(1, max_number)
        # Add the random number to the list
        numbers.append(number)

    # Show the sequence to the player and wait for the screen to clear
    print("Remember this sequence:", numbers)
    print(f"Get ready! The sequence will disappear in {sequence_length} seconds...")
    sleep(sequence_length)

    # Ask the player to guess the sequence
    guess = input("Enter the sequence you saw, separated by spaces: ")

    # Convert the player's guess into a list of numbers
    guessed_sequence = list(map(int, guess.split()))

    # Check if the guess is correct
    if guessed_sequence == numbers:
        print("You got it right!")
    else:
        print("Oops! The correct sequence was:", numbers)

    # Example usage (play the game with difficulty 1)
    play_memory_game(1)
import random
from time import sleep

def play_memory_game(difficulty):

    # Define difficulty levels (using a single dictionary)
    difficulty_levels = {
        1: {"sequence_length": 3, "max_number": 5},  # Easy - Shorter sequence, lower range
        2: {"sequence_length": 4, "max_number": 7},  # Medium - Moderate sequence, moderate range
        3: {"sequence_length": 5, "max_number": 10},  # Hard - Longer sequence, higher range
        4: {"sequence_length": 6, "max_number": 12},  # Very Hard - Even longer sequence, higher range
        5: {"sequence_length": 8, "max_number": 15},  # Extreme - Longest sequence, highest range
    }

    # Check if chosen difficulty is valid
    if difficulty not in difficulty_levels:
        print("Invalid difficulty! Defaulting to medium (3).")
        difficulty = 3

    # Extract sequence parameters based on chosen difficulty
    sequence_length = difficulty_levels[difficulty]["sequence_length"]
    max_number = difficulty_levels[difficulty]["max_number"]

    # Print difficulty information
    print(f"Difficulty: {difficulty} (Sequence Length: {sequence_length}, Maximum Number: {max_number})")

    # Generate random number sequence
    numbers = []
    for i in range(sequence_length):
        number = random.randint(1, max_number)
        numbers.append(number)

    # Show the sequence to the player
    print("Remember this sequence:", numbers)
    print(f"Get ready! The sequence will disappear in {sequence_length} seconds...")
    sleep(sequence_length)

    # Get player's guess
    guess = input("Enter the sequence you saw, separated by spaces: ")

    # Convert guess to list of numbers
    guessed_sequence = list(map(int, guess.split()))

    # Check if guess is correct
    if guessed_sequence == numbers:
        print("You got it right!")
    else:
        print("Oops! The correct sequence was:", numbers)

# Example usage (play the game with difficulty 2)
play_memory_game(2)
