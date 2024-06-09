import random

# Define exchange rate (for example) and amount ranges
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
    """
    This function generates a random USD amount within the specified range for the chosen difficulty.

    Args:
        difficulty (int): The chosen difficulty level (1-5).

    Returns:
        int: A random USD amount within the difficulty's range.
    """

    # Get the minimum and maximum values for the chosen difficulty
    min_value, max_value = DIFFICULTY_LEVELS[difficulty]["range"]

    # Use the 'random.randint' function to generate a random integer within the range
    # and convert the values to integers for consistency
    return random.randint(int(min_value), int(max_value))


# Function to convert USD amount to ILS
def convert_to_ils(amount):
    """
    This function converts a USD amount to ILS using the defined exchange rate.

    Args:
        amount (float): The amount in USD.

    Returns:
        float: The equivalent amount in ILS.
    """

    # Multiply the USD amount by the exchange rate to get the ILS amount
    return amount * USD_TO_ILS_RATE


# Function to play the currency conversion guessing game
def play_game(difficulty):
    """
    This function conducts the currency conversion guessing game for the chosen difficulty.

    Args:
        difficulty (int): The chosen difficulty level (1-5).
    """

    # Generate a random USD amount based on the difficulty
    amount_usd = generate_random_amount(difficulty)

    # Convert the USD amount to ILS
    amount_ils = convert_to_ils(amount_usd)

    # Ask the user for their guess in ILS
    guess = int(input("Enter your guess for the amount in ILS: "))

    # Check if the guess is correct
    if guess == amount_ils:
        print(f"You guessed correctly! The amount is {amount_ils} ILS in difficulty {DIFFICULTY_LEVELS[difficulty]['name']}.")
    else:
        print(f"You guessed incorrectly. The amount is {amount_ils} ILS in difficulty {DIFFICULTY_LEVELS[difficulty]['name']}.")

def run_difficulty():
    # Get user input for difficulty level in a loop until valid
    while True:
        try:
            difficulty = int(input("Choose difficulty level (1-5): "))
            # Check if the chosen difficulty exists in the dictionary
            if difficulty in DIFFICULTY_LEVELS:
                break
            else:
                print("Invalid difficulty level. Please choose between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Start the game with the chosen difficulty
    play_game(difficulty)
