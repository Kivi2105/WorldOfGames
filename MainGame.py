# Import necessary functions from the Live module
from Live import welcome, load_game, play_memory_game, play_guessing_game, play_currency_roulette

# Print a welcome message using the welcome function
print(welcome("Player"))

# Get the user's game choice and difficulty level using the load_game function
game_choice, difficulty = load_game()

# Call the appropriate play function based on the user's choice
if game_choice == 1:
    # If the user chose Memory Game, play it with the specified difficulty
    play_memory_game(difficulty)
elif game_choice == 2:
    # If the user chose Guessing Game, play it with the specified difficulty
    play_guessing_game(difficulty)
elif game_choice == 3:
    # If the user chose Currency Roulette, play it with the specified difficulty
    play_currency_roulette(difficulty)
