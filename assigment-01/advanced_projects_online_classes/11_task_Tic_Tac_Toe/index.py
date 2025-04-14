import time
import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_player_move():
    while True:
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter values between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    print("Welcome to Tic-Tac-Toe!")
    time.sleep(1)
    
    while True:
        print_board(board)
        print(f"Player {players[turn]}'s turn")
        
        row, col = get_player_move()
        if board[row][col] == " ":
            board[row][col] = players[turn]
            
            if check_winner(board, players[turn]):
                print_board(board)
                print(f"Player {players[turn]} wins!")
                break
            
            if is_full(board):
                print_board(board)
                print("It's a tie!")
                break
            
            turn = 1 - turn  # Switch turn
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()