from messages import welcome, menu
from game_logic import game

if __name__ == "__main__":

    print(welcome())
    print(menu())
    try:

        choice_menu = int(input("Enter your choice: "))
    except:
        print("Invalid input. Please enter a number.")
    else:
        if choice_menu == 1:
            game(10, "Easy")

        elif choice_menu == 2:
            game(5, "Medium")

        elif choice_menu == 3:
            game(3, "Hard")