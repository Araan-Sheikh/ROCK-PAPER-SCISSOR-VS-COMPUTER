import random
import time
from colorama import Fore, Back, Style

def main():
    print(Fore.CYAN + "Welcome to Rock Paper Scissors!" + Style.RESET_ALL)
    time.sleep(1)
    input("Press Enter to continue")
    
    play_game = True
    bot_score = 0
    user_score = 0

    while play_game:
        time.sleep(1)
        cpu_choice = random.choice(["Rock", "Paper", "Scissors"])
        user_choice = input(Fore.GREEN + "Rock, Paper or Scissors? " + Style.RESET_ALL).capitalize()

        print(f"\nYou chose {user_choice}")
        print(f"Opponent chose {cpu_choice}")
        time.sleep(1)

        if user_choice == cpu_choice:
            print(Fore.YELLOW + "You tied!" + Style.RESET_ALL)
        elif (
            (user_choice == "Rock" and cpu_choice == "Scissors") or
            (user_choice == "Paper" and cpu_choice == "Rock") or
            (user_choice == "Scissors" and cpu_choice == "Paper")
        ):
            print(Fore.GREEN + "You won!" + Style.RESET_ALL)
            user_score += 1
        else:
            print(Fore.RED + "You lost." + Style.RESET_ALL)
            bot_score += 1

        print("\nLeaderboard")
        print(f"Your score: {user_score}")
        print(f"Opponent score: {bot_score}")
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != "y":
            print(Fore.CYAN + "Okay, bye!" + Style.RESET_ALL)
            play_game = False

if __name__ == "__main__":
    main()
