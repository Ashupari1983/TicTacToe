
import random
from colorama import Fore, Style, init

init(autoreset=True)

def display_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f"\n {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f"\n {board[6]} | {board[7]} | {board[8]}\n")

def player_choice():
    symbol = input(f"{Fore.CYAN}Choose X or O: ").upper()
    while symbol not in ["X", "O"]:
        symbol = input(f"{Fore.CYAN}Choose X or O: ").upper()
    return symbol, "O" if symbol == "X" else "X"

def player_move(board, symbol):
    while True:
        try:
            move = int(input(f"{Fore.CYAN}Enter position (1-9): "))-1
            if move in range(9) and board[move].isdigit():
                board[move] = symbol
                break
            print(f"{Fore.RED}Invalid move! Try again.")
        except ValueError:
            print(f"{Fore.RED}Enter a number between 1 to 9.")

def check_win(board, symbol):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(all(board[i]== symbol for i in row)for row in wins)

def ai_move(board, ai, player):
    for symbol in [ai, player]:
        for i in range(9):
            if board[i].isdigit():
                test = board.copy()
                test[i] = symbol
                if check_win (test,symbol):
                    board[i] = ai
                    return
    board[random.choice([i for i in range(9) if board[i].isdigit()])] = ai

def tictactoe():
        print(f"{Fore.GREEN}Welcome to Tic-Tac-Toe!")
        name = input(f"{Fore.CYAN}Enter your name: ")

        while True:
            board = list("123456789")
            player, ai = player_choice()
            turn = player

            while True:
                display_board(board)

                if turn == player:
                    player_move(board, player)
                else:
                    ai_move(board, ai, player)
                    print(f"{Fore.MAGENTA}AI played!")

                if check_win(board,turn):
                    display_board(board)
                    print(f"{Fore.YELLOW}{name if turn == player else "AI"} wins!")
                    break

                if all(not cell.isdigit() for cell in board):
                    display_board(board)
                    print(f"{Fore.YELLOW}It's a tie!")
                    break

                turn = ai if turn == player else player

            if input(f"{Fore.CYAN}Play again? (yes/no): ").lower() != "yes":
                print(f"{Fore.GREEN}Thank you for playing!")
                break


if __name__ == "__main__":
    tictactoe()
