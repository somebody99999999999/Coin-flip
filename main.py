import os
import time
import random

# Just removes the dumb text that just appears at the top of the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# ==========================================
#             COIN FLIP: JACKPOT
# ==========================================

# Clears the terminal screen.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Displays text one character at a time.
def slowTyping(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)


# ==========================================
#     How the coin looks on both sides
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
#          MAIN MENU - TITLE SCREEN
# ==========================================

clear_screen()

slowTyping("-------------------------------------\n", 0.02)
slowTyping("       Coin Flip: Jackpot\n", 0.04)
slowTyping("-------------------------------------\n", 0.02)
slowTyping("           .-------.\n")
slowTyping("          /         \\\n")
slowTyping("         |  HEADS    |\n")
slowTyping("         |  or TAILS |\n")
slowTyping("          \\         /\n")
slowTyping("           '-------'\n\n")


choice = input("\nType Start to begin the game or Credits to see them \n\n> ").strip().title()

# ==========================================
#                PLAY GAME
# ==========================================

if choice == 'Start':

    clear_screen()

    slowTyping("Beginning the game...", 0.05)
    time.sleep(1)

    # Player statistics - stats
    coins = 0
    total_flips = 0
    heads_count = 0
    tails_count = 0

    # Upgrade variables - Upgrades
    multiplier = 1.5
    multiplier_level = 0
    multiplier_cost = 5

    jackpot_level = 0
    jackpot_cost = 15

    # Prestige variables - Prestige
    prestige_points = 0
    prestige_requirement = 1000

    # Main game loop - The whole game
    running = True

    while running:
        clear_screen()

        # Calculate the permanent prestige bonus.
        prestige_bonus = 1 + (prestige_points * 0.10)

        print("-------------------------------------")
        print("        COIN FLIP: JACKPOT")
        print("-------------------------------------")
        print("              .-------.")
        print("             /         \\")
        print("            |   COIN    |")
        print("             \\         /")
        print("              '-------'")
        print()
       
        # Display the players stats.
        print(f"Coins: {coins}")
        print(f"Total Flips: {total_flips}")
        print(f"Heads: {heads_count}")
        print(f"Tails: {tails_count}\n")
        print(f"Multiplier: x{multiplier:.1f}")
        print(f"Jackpot Level: {jackpot_level}\n")
        print(f"Prestige Points: {prestige_points}")
        print(f"Prestige Bonus: x{prestige_bonus:.2f}")
        print(f"You Can Prestige At: {prestige_requirement} coins\n")

        # Show the result percentages after the first flip.
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
        print("            THE SHOP")
        print("-------------------------------------")
        print("1. Flip the Coin")
        print(
            f"2. Multiplier Upgrade - Level {multiplier_level}"
            f" - Cost: {multiplier_cost} coins"
        )
        print(
            f"3. Jackpot Upgrade - Level {jackpot_level}"
            f" - Cost: {jackpot_cost} coins"
        )
        print("4. View Stats")
        print("5. Prestige")
        print("6. Reset Game")
        print("7. Quit")

        command = input("\nChoose an option\n> ").strip().lower()

        # ----------------------------------
        #      OPTION 1: FLIP THE COIN
        # ----------------------------------
        if command == "1":

            clear_screen()
            
            # Controls how fast the text goes by in the terminal - the 0.20 and beyond
            slowTyping("Flipping the coin now", 0.20)
            slowTyping("...\n\n", 0.25)

            # Choose heads or tails randomly.
            result = random.choice(["HEADS", "TAILS"])

            # Update the flip statistics - stats
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

            # Jackpot upgrades provides a better chance for bonus coins - extra coins.
            jackpot_chance = min(10 + jackpot_level * 5, 50)

            print("-------------------------------------")
            print(f"          IT LANDED ON {result}!")
            print("-------------------------------------")

            show_coin(result)

            coins += reward
            print(f"\nYou earned {reward} coins!")

            # Check whether the player got a jackpot bonus.
            if random.randint(1, 100) <= jackpot_chance:
                bonus = reward * 3
                coins += bonus
                print(f"JACKPOT! Bonus +{bonus} coins!")

            input("\nPress Enter to continue...")

        # ----------------------------------
        #    OPTION 2: MULTIPLIER UPGRADE
        # ----------------------------------
        elif command == "2":

            if coins >= multiplier_cost:
                coins -= multiplier_cost
                multiplier_level += 1
                multiplier += 1.5

                # How each new upgrade costs more.
                multiplier_cost = int(multiplier_cost * 2)

                print("\nMultiplier upgraded!")
                print(f"New multiplier: x{multiplier:.1f}")
            else:
                print("\nNot enough coins!")

            time.sleep(1.2)

        # ----------------------------------
        #    OPTION 3: JACKPOT UPGRADES
        # ----------------------------------
        elif command == "3":

            if coins >= jackpot_cost:
                coins -= jackpot_cost
                jackpot_level += 1


                jackpot_cost = int(jackpot_cost * 3)

                print("\nJackpot upgraded!")
                print("Your chance of a bonus is now higher!")
            else:
                print("\nNot enough coins!")

            time.sleep(1.2)

        # ----------------------------------
        #     OPTION 4: VIEW STATISTICS
        # ----------------------------------
        elif command == "4":

            clear_screen()
            print("========== STATISTICS ==========")
            print(f"Total flips: {total_flips}\n")
            print(f"Heads: {heads_count}")
            print(f"Tails: {tails_count}\n")
            print(f"Current Coins: {coins}\n")

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
                print("You must flip the coin to begin!")

            print("================================")
            input("\nPress Enter to return to the shop...")

        # ----------------------------------
        #        OPTION 5: PRESTIGE
        # ----------------------------------
        elif command == "5":

            if coins >= prestige_requirement:

                # Prestige increases permanent bonus points.
                prestige_points += 1.5

                # Reset coins and upgrades.
                coins = 0
                multiplier = 1.5
                multiplier_level = 0
                multiplier_cost = 10

                jackpot_level = 0
                jackpot_cost = 25

                # Make the next prestige more difficult.
                prestige_requirement *= 1.5

                print("\nPRESTIGE SUCCESSFUL!")
                print(f"Prestige points: {prestige_points}")
                print("Your permanent bonus has increased!")

            else:
                print(
                    f"\nYou need {prestige_requirement} coins "
                    f"to prestige!"
                )

            time.sleep(1.44)

        # ----------------------------------
        #     OPTION 6: RESET THE GAME
        # ----------------------------------
        elif command == "6":

            confirm = input("Reset all progress? Type yes to confirm: ").strip().lower()
            
            if confirm == "yes":
                coins = 0
                total_flips = 0
                heads_count = 0
                tails_count = 0

                multiplier = 1.5
                multiplier_level = 0
                multiplier_cost = 5

                jackpot_level = 0
                jackpot_cost = 15

                prestige_points = 0
                prestige_requirement = 1000

                print("\nGame reset successfully!")
                time.sleep(1.35)
            else:
                print("\nReset cancelled.")
                time.sleep(1.25)

        # --------------------------------
        #          OPTION 7: QUIT
        # --------------------------------
        elif command == "7":

            clear_screen()
            slowTyping("The coin stops spinning...\n", 0.04)
            slowTyping("\nThanks for playing Jackpot!\n\n", 0.04)
            
            # Just stops the main game from running
            running = False


        # --------------------------------
        #          INVALID INPUT
        # --------------------------------
        else:
            print("\nInvalid option!\nYou need to Choose from 1-7.")

            time.sleep(2)


# ----------------------------------
#            CREDITS
# ----------------------------------
elif choice == 'Credits':
    os.system('cls||clear')
    slowTyping("-----------\n", delay=0.05)
    slowTyping("Credits", delay=0.1)
    slowTyping("\n-----------", delay=0.05)
    slowTyping("\nDeveloper - Eduardo R", delay=0.05)
    slowTyping("\nPast names - LUCKY STREAK\n\n", delay=0.05)
    # slowTyping("\nI had gotten the inspiration for this project from Brian Le's Honey The Bunny Game \nSo I'll just like to thank him for the idea and the inspiration", delay=0.09)