import random


# Generates a roll of the dice.
def roll_dice(sides: int):
    while True:
        user_input = input("Would you like to roll the dice? (y/n) ")
        dice_number = random.randint(1, sides)
        if user_input == "y":
            print(f"You have rolled a {dice_number}")
        elif user_input == "n":
            break
        else:
            print("Invalid input.")


# Allows player to play again.
def keep_playing():
    while True:
        replay = input("Play again? (y/n) ".lower())
        if replay == "y":
            return True
        elif replay == "n":
            return False
        else:
            print("Invalid input")


# main game loop.
def main():
    dice = 6
    while True:
        roll_dice(dice)
        if keep_playing() == False:
            break
    print("\nThank you for playing \n")


main()
