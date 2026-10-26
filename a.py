
import random
from colorama import Fore, Style, init

init(autoreset=True)

def move():
    return random.choice(["rock", "paper", "scissors"])

def rps():
    print(f"{Fore.CYAN}Welcome to Rock Paper Scissors!")
    print(f"{Fore.YELLOW}Would you like to start?")
    ans = input(f"{Fore.WHITE}Yes/No: ").lower()

    if ans == "yes":
        game()
    else:
        print(f"{Fore.RED}Okay, Goodbye!")

def game():
    while True:
        player_move = input(
            f"{Fore.CYAN}Enter your move (rock/paper/scissors): "
        ).lower()

        if player_move not in ["rock", "paper", "scissors"]:
            print(f"{Fore.RED}Please enter a valid move.")
            continue

        x = move()
        print(f"{Fore.MAGENTA}AI's move: {Fore.YELLOW}{x}")

        if x == player_move:
            print(f"{Fore.YELLOW}It's a tie!")

        elif (x == "rock" and player_move == "scissors") or (x == "scissors" and player_move == "paper") or (x == "paper" and player_move == "rock"):
            print(f"{Fore.RED}AI wins!")

        else:
            print(f"{Fore.GREEN}You win!")

        a = input(f"{Fore.CYAN}Play again? (yes/no): ").lower()

        if a == "yes":
            continue
        else:
            print(f"{Fore.GREEN}It was fun playing with you!")
            break

if __name__ == "__main__":
    rps()
