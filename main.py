import os
import time
import random

# ==========================================
#             COIN FLIP: LUCKY STREAK
# ==========================================

# Clears the terminal screen.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Displays text one character at a time.
def singleTyping(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)


# ==========================================
#                COIN ART
# ==========================================

def show_coin(side):
    if side == "HEADS":
        print("       .-----------.")
        print("      /  _________  \\")
        print("     |  /         \\  |")
        print("     | |   HEADS   | |")
        print("     |  \\_________/  |")
        print("      \\             /")
        print("       '-----------'")
    else:
        print("       .-----------.")
        print("      /  _________  \\")
        print("     |  /         \\  |")
        print("     | |   TAILS   | |")
        print("     |  \\_________/  |")
        print("      \\             /")
        print("       '-----------'")


# ==========================================
#             MAIN MENU
# ==========================================

clear_screen()

singleTyping("-------------------------------------\n", 0.02)
singleTyping("       Coin Flip: Lucky Streak\n", 0.04)
singleTyping("-------------------------------------\n", 0.02)
singleTyping("           .-------.\n")
singleTyping("          /         \\\n")
singleTyping("         |  HEADS    |\n")
singleTyping("         |  or TAILS |\n")
singleTyping("          \\         /\n")
singleTyping("           '-------'\n\n")
# singleTyping("1. Play The Game\n")
# singleTyping("2. Credits\n")

choice = input("\n Type Start to begin the game or Credits to see them \n> ").strip().title()

# ==========================================
#                PLAY GAME
# ==========================================

if choice == 'Start':

    clear_screen()

    singleTyping("Flipping into a world of luck...", 0.05)
    time.sleep(1)

    # Player statistics
    coins = 0
    total_flips = 0
    heads_count = 0
    tails_count = 0

    # Upgrade variables
    multiplier = 1.0
    multiplier_level = 0
    multiplier_cost = 10

    luck_level = 0
    luck_cost = 25

    # Prestige variables
    prestige_points = 0
    prestige_requirement = 1000

    # Main game loop
    running = True

    while running:
        clear_screen()

        # Calculate the permanent prestige bonus.
        prestige_bonus = 1 + (prestige_points * 0.10)

        print("-------------------------------------")
        print("        COIN FLIP: LUCKY STREAK")
        print("-------------------------------------")
        print("              .-------.")
        print("             /         \\")
        print("            |   COIN    |")
        print("             \\         /")
        print("              '-------'")
        print()
       
        # Display player statistics.
        print(f"Coins: {coins}")
        print(f"Total Flips: {total_flips}")
        print(f"Heads: {heads_count}")
        print(f"Tails: {tails_count}")
        print(f"Multiplier: x{multiplier:.1f}")
        print(f"Luck Level: {luck_level}")
        print(f"Prestige Points: {prestige_points}")
        print(f"Prestige Bonus: x{prestige_bonus:.2f}")
        print(f"Prestige At: {prestige_requirement} coins")

        # Show result percentages after the first flip.
        if total_flips > 0:
            print(
                f"Heads Rate: "
                f"{heads_count / total_flips * 100:.1f}%"
            )
            print(
                f"Tails Rate: "
                f"{tails_count / total_flips * 100:.1f}%"
            )

        print("\n-------------------------------------")
        print("            LUCKY SHOP")
        print("-------------------------------------")
        print("1. Flip the Coin")
        print(
            f"2. Multiplier Upgrade - Level {multiplier_level}"
            f" - Cost: {multiplier_cost} coins"
        )
        print(
            f"3. Luck Upgrade - Level {luck_level}"
            f" - Cost: {luck_cost} coins"
        )
        print("4. View Statistics")
        print("5. Prestige")
        print("6. Reset Game")
        print("7. Quit")

        command = input("\nChoose an option\n> ").strip().lower()

        # ----------------------------------
        # OPTION 1: FLIP THE COIN
        # ----------------------------------
        if command == "1":

            clear_screen()
            # Controls how fast the text goes by in the terminal
            singleTyping("Flipping the coin", 0.15)
            singleTyping("...\n\n", 0.25)

            # Choose heads or tails randomly.
            result = random.choice(["HEADS", "TAILS"])

            # Update flip statistics.
            total_flips += 1

            if result == "HEADS":
                heads_count += 1
            else:
                tails_count += 1

            # Calculate the reward.
            reward = max(
                1,
                int(multiplier * prestige_bonus)
            )

            # Luck upgrades provide a chance for bonus coins.
            lucky_chance = min(10 + luck_level * 5, 50)

            print("-------------------------------------")
            print(f"          YOU GOT {result}!")
            print("-------------------------------------")

            show_coin(result)

            coins += reward
            print(f"\nYou earned {reward} coins!")

            # Check whether the player got a lucky bonus.
            if random.randint(1, 100) <= lucky_chance:
                bonus = reward * 3
                coins += bonus
                print(f"LUCKY FLIP! Bonus +{bonus} coins!")

            input("\nPress Enter to continue...")

        # ----------------------------------
        # OPTION 2: MULTIPLIER UPGRADE
        # ----------------------------------
        elif command == "2":

            if coins >= multiplier_cost:
                coins -= multiplier_cost
                multiplier_level += 1
                multiplier += 0.5

                # Each new upgrade costs more.
                multiplier_cost = int(multiplier_cost * 1.5)

                print("\nMultiplier upgraded!")
                print(f"New multiplier: x{multiplier:.1f}")
            else:
                print("\nNot enough coins!")

            time.sleep(1.2)

        # ----------------------------------
        # OPTION 3: LUCK UPGRADE
        # ----------------------------------
        elif command == "3":

            if coins >= luck_cost:
                coins -= luck_cost
                luck_level += 1

                # Increase the next upgrade price.
                luck_cost = int(luck_cost * 1.6)

                print("\nLuck upgraded!")
                print("Your chance of a bonus is higher!")
            else:
                print("\nNot enough coins!")

            time.sleep(1.2)

        # ----------------------------------
        # OPTION 4: VIEW STATISTICS
        # ----------------------------------
        elif command == "4":

            clear_screen()
            print("========== STATISTICS ==========")
            print(f"Total flips: {total_flips}")
            print(f"Heads: {heads_count}")
            print(f"Tails: {tails_count}")
            print(f"Coins: {coins}")

            if total_flips > 0:
                print(
                    f"Heads: "
                    f"{heads_count / total_flips * 100:.1f}%"
                )
                print(
                    f"Tails: "
                    f"{tails_count / total_flips * 100:.1f}%"
                )
            else:
                print("Flip the coin to begin!")

            print("================================")
            input("\nPress Enter to return to the shop...")

        # ----------------------------------
        # OPTION 5: PRESTIGE
        # ----------------------------------
        elif command == "5":

            if coins >= prestige_requirement:

                # Prestige increases permanent bonus points.
                prestige_points += 1

                # Reset coins and upgrades.
                coins = 0
                multiplier = 1.0
                multiplier_level = 0
                multiplier_cost = 10

                luck_level = 0
                luck_cost = 25

                # Make the next prestige more difficult.
                prestige_requirement *= 2

                print("\nPRESTIGE SUCCESSFUL!")
                print(f"Prestige points: {prestige_points}")
                print("Your permanent bonus has increased!")
            else:
                print(
                    f"\nYou need {prestige_requirement} coins "
                    f"to prestige!"
                )

            time.sleep(1.8)

        # ----------------------------------
        # OPTION 6: RESET THE GAME
        # ----------------------------------
        elif command == "6":

            confirm = input(
                "Reset all progress? Type yes to confirm: "
            ).strip().lower()

            if confirm == "yes":
                coins = 0
                total_flips = 0
                heads_count = 0
                tails_count = 0

                multiplier = 1.0
                multiplier_level = 0
                multiplier_cost = 10

                luck_level = 0
                luck_cost = 25

                prestige_points = 0
                prestige_requirement = 1000

                print("\nGame reset successfully!")
                time.sleep(1)
            else:
                print("\nReset cancelled.")
                time.sleep(1)

        # ----------------------------------
        # OPTION 7: QUIT
        # ----------------------------------
        elif command == "7" or command == "quit":

            clear_screen()
            singleTyping("The coin stops spinning...\n", 0.04)
            singleTyping("Thanks for playing Lucky Streak!\n", 0.04)
            running = False

        # ----------------------------------
        # INVALID INPUT
        # ----------------------------------
        else:
            print("\nInvalid option! Choose 1-7.")
            time.sleep(1)

elif choice == 'Credits':
    " "