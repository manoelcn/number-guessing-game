import random
from messages import level_message

def game(limit, level):
    print(level_message(level))
    number = random.randint(98, 100)
    attempts = 0

    while attempts < limit:
        try:
            guess = int(input("Enter your guess: "))
        except:
            print("Invalid input. Please enter a whole number. Try again.\n")
            continue

        attempts += 1
        
        if guess < number:
            print(f"Incorrect! The number is greater than {guess}.\n")
        elif guess > number:
            print(f"Incorrect! The number is less than {guess}.\n")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break

    else:
        print(f"Game Over! You ran out of attempts.\nThe number I was thinking of was {number}.")