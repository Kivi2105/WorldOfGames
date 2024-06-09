#Generating random numbers: You can use the random() and randint() functions to generate random numbers.
import random

# Imports the os module, which provides access to operating system functions.
import os

# Imports the sleep function from the time module for pausing the program execution.
from time import sleep

# The number of numbers in the sequence to remember.
sequence_length = 5
# The upper limit of the random numbers (1-10).
max_number = 10

# This line initializes an empty list to store the generated random numbers.
numbers = []

# This loop generates the random sequence using a `for` loop.
for sequence_index in range(sequence_length):
    # Generate a random number within the specified range.
    random_number = random.randint(1, max_number)
    # Add the generated number to the `numbers` list.
    numbers.append(random_number)

# Print the generated sequence to the user.
print("Remember this sequence: ", numbers)

# Tell the user the screen will be cleared in 5 seconds.
print("Your screen will be cleared in 5 seconds...")

# Clear the screen using the appropriate command based on the OS (commented out)
sleep(5)
os.system('cls')

# This loop prints 10 empty lines to effectively clear the screen (alternative approach).
for i in range(10):
    print()

# Ask the user to guess the sequence.
guess = input("What is the sequence? Enter numbers separated by spaces: ")

# Convert the user's guess into a list of integers.
guessed_sequence = list(map(int, guess.split()))

# Check if the user's guess is correct.
if guessed_sequence == numbers:
    print("That is correct!")
else:
    print("That is incorrect! The correct sequence is: ", numbers)
