import random

def guess(difficulty):

    # Define the number range based on difficulty
    if difficulty == 1:
        # Easy: range 1-10
        number_range = (1, 10)
        print("Easy mode: Guess a number between 1 and 10.")  # Added message for each difficulty
    elif difficulty == 2:
        # Medium: range 1-20
        number_range = (1, 20)
        print("Medium mode: Guess a number between 1 and 20.")
    elif difficulty == 3:
        # Hard: range 1-50
        number_range = (1, 50)
        print("Hard mode: Guess a number between 1 and 50.")
    elif difficulty == 4:
        # Very Hard: range 1-100
        number_range = (1, 100)
        print("Very Hard mode: Guess a number between 1 and 100.")
    elif difficulty == 5:
        # Extreme: range 1-1000
        number_range = (1, 1000)
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

if __name__ == '__main__':
    # Example usage (assuming difficulty 1)
    guess(1)



