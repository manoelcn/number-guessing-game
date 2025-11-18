def welcome():
    return f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.\n"

def menu():
    return f"Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n"

def level_message(level):
    return f"\nGreat! You have selected the {level} difficulty level.\nLet's start the game!\n"