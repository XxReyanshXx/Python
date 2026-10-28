
import random

def roll_dice():
    return random.randint(1, 6)

while True:
    print("\n1. Roll the Dice")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        number = roll_dice()
        print("You rolled:", number)
    elif choice == 2:
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice! Try again.")
