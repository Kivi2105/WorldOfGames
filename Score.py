import os

# Define the points for winning
POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5


def add_score(difficulty):
    score = POINTS_OF_WINNING(difficulty)
    try:
        with open("Scores.txt", "r") as file:
            current_score = int(file.read())
    except (FileNotFoundError, ValueError):
        current_score = 0

    new_score = current_score + score

    with open("Scores.txt", "w") as file:
        file.write(str(new_score))
